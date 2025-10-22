/**
 * Air Traffic Control System Frontend
 * Main JavaScript application for the ATC dashboard
 *
 * This class handles all frontend functionality including:
 * - Interactive map display using Leaflet.js
 * - Real-time aircraft data visualization
 * - User interactions (clicking aircraft, filtering, etc.)
 * - Periodic data refresh from backend API
 *
 * Author: Andrew Moore
 * Course: Capstone Project - FAA ATC System
 */

class ATCSystem {
    /**
     * Constructor - Initialize all instance variables
     * Using a class-based approach keeps all state and methods encapsulated
     */
    constructor() {
        // Leaflet map instance - will be initialized in initMap()
        this.map = null;

        // Map data structure to store aircraft markers
        // Key: aircraft ID (unique identifier)
        // Value: object containing {marker: L.marker, aircraft: data object}
        // Using a Map instead of object for better performance with frequent lookups/deletions
        this.aircraftMarkers = new Map();

        // Currently selected aircraft object (null if none selected)
        this.selectedAircraft = null;

        // setInterval handle for periodic data refresh
        // Stored so we can clear it later to prevent memory leaks
        this.refreshInterval = null;

        // Connection status flag for the backend API
        this.isConnected = false;

        // Configuration object - centralized settings for easy modification
        this.config = {
            refreshRate: 5000, // Update aircraft data every 5 seconds (5000ms)
            mapCenter: [32.8998, -97.0403], // DFW Airport coordinates (lat, lon)
            mapZoom: 9, // Initial zoom level (9 shows ~50 mile radius)
            maxAircraftAge: 30000 // Consider data stale after 30 seconds (not currently used but planned)
        };
    }

    /**
     * Initialize the ATC System
     * This is the main entry point called when the page loads
     * Using async/await to handle asynchronous data loading
     */
    async init() {
        try {
            console.log('Initializing ATC System...');

            // Step 1: Initialize the Leaflet map with our configuration
            this.initMap();

            // Step 2: Set up event listeners for user controls (buttons, sliders, checkboxes)
            this.initControls();

            // Step 3: Update UI to show we're connecting
            this.updateConnectionStatus(false, 'Initializing...');

            // Step 4: Load initial aircraft data from the backend
            // Using 'await' here because we want to wait for data before continuing
            await this.loadAircraftData();

            // Step 5: Start the automatic refresh timer (every 5 seconds)
            this.startPeriodicUpdates();

            // Step 6: Update UI to show successful connection
            this.updateConnectionStatus(true, 'Connected (Mock Data)');
            console.log('ATC System initialized successfully');

        } catch (error) {
            // If anything goes wrong during initialization, log the error and update UI
            console.error('Failed to initialize ATC System:', error);
            this.updateConnectionStatus(false, 'Connection Failed');
        }
    }

    /**
     * Initialize the Leaflet map
     * Sets up the interactive map with tile layers and event listeners
     * Leaflet.js is a popular open-source JavaScript library for interactive maps
     */
    initMap() {
        // Create the Leaflet map instance
        // L.map('map') targets the <div id="map"> element in index.html
        // setView() positions the map at DFW Airport with zoom level 9
        this.map = L.map('map').setView(this.config.mapCenter, this.config.mapZoom);

        // Add tile layer (the actual map imagery)
        // Tiles are 256x256 pixel images that make up the map
        // {z} = zoom level, {x}/{y} = tile coordinates
        // We try local tiles first for offline capability
        const tileLayer = L.tileLayer('/tiles/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors, © CARTO',
            maxZoom: 19, // Maximum zoom level supported
            // errorTileUrl: transparent 1x1 pixel as fallback for missing tiles
            errorTileUrl: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=='
        });

        // Intelligent fallback system: if local tiles don't exist, switch to online tiles
        // This allows the app to work both offline (with pre-downloaded tiles) and online
        tileLayer.on('tileerror', () => {
            console.warn('Local tile not found, using online tiles');
            // Only add online tiles once to avoid duplicate layers
            if (!this.onlineTileLayerAdded) {
                this.map.removeLayer(tileLayer); // Remove the failing local tile layer
                // Add CartoDB dark theme tiles from CDN
                // CartoDB provides free map tiles with a dark aesthetic suitable for ATC
                L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                    attribution: '© OpenStreetMap contributors, © CARTO',
                    maxZoom: 19
                }).addTo(this.map);
                this.onlineTileLayerAdded = true; // Flag to prevent adding multiple times
            }
        });

        // Add the tile layer to the map
        tileLayer.addTo(this.map);

        // Set up event listener for clicking anywhere on the map
        // Clicking the map (not on a marker) will deselect any selected aircraft
        this.map.on('click', () => {
            this.deselectAircraft();
        });

        console.log('Map initialized');
    }

    /**
     * Initialize UI controls and event listeners
     * Sets up all interactive controls in the sidebar (refresh button, filters, etc.)
     * Using event listeners to respond to user interactions
     */
    initControls() {
        // Refresh button - allows user to manually reload aircraft data
        const refreshBtn = document.getElementById('refreshData');
        if (refreshBtn) {
            // Arrow function maintains 'this' context so we can call class methods
            refreshBtn.addEventListener('click', () => {
                this.loadAircraftData();
            });
        }

        // Altitude filter slider - filters aircraft by minimum altitude
        const altitudeFilter = document.getElementById('altitudeFilter');
        const altitudeValue = document.getElementById('altitudeValue'); // Display the current value
        if (altitudeFilter && altitudeValue) {
            // 'input' event fires continuously as the slider moves (vs 'change' which fires on release)
            altitudeFilter.addEventListener('input', (e) => {
                const value = e.target.value; // Get the slider's current value (0-50000)
                altitudeValue.textContent = value; // Update the displayed value in the UI
                this.filterAircraftByAltitude(parseInt(value)); // Filter markers on the map
            });
        }

        // Show paths checkbox - placeholder for future flight path visualization
        const showPaths = document.getElementById('showPaths');
        if (showPaths) {
            // 'change' event fires when checkbox is toggled
            showPaths.addEventListener('change', (e) => {
                this.toggleFlightPaths(e.target.checked); // Pass true/false to toggle method
            });
        }

        console.log('Controls initialized');
    }

    /**
     * Load aircraft data from the API
     * Fetches current aircraft positions from the Flask backend
     * Using async/await for cleaner asynchronous code (vs callbacks or .then() chains)
     */
    async loadAircraftData() {
        try {
            // Fetch data from the backend API endpoint
            // fetch() returns a Promise, await pauses execution until the response arrives
            const response = await fetch('/api/aircraft');

            // Check if the HTTP request was successful (status 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Parse the JSON response body into a JavaScript array
            // The backend returns an array of aircraft objects
            const aircraftData = await response.json();

            // Update the map with the new aircraft data
            this.updateAircraftOnMap(aircraftData);

            // Update the statistics panel (total aircraft count, last update time)
            this.updateStatistics(aircraftData);

            console.log(`Loaded ${aircraftData.length} aircraft`);

        } catch (error) {
            // If the fetch fails (network error, server down, etc.), log it and update UI
            console.error('Failed to load aircraft data:', error);
            this.updateConnectionStatus(false, 'Data Load Failed');
        }
    }

    /**
     * Update aircraft markers on the map
     * Clears all existing markers and redraws them with fresh data
     * Using a "clear and redraw" approach for simplicity (vs updating individual markers)
     */
    updateAircraftOnMap(aircraftData) {
        // Clear existing markers from the map
        // Using forEach to iterate through the Map values
        this.aircraftMarkers.forEach(({marker}) => {
            this.map.removeLayer(marker); // Remove the marker from the Leaflet map
        });
        this.aircraftMarkers.clear(); // Clear the Map data structure

        // Add new markers for each aircraft in the updated data
        aircraftData.forEach(aircraft => {
            this.addAircraftMarker(aircraft);
        });
    }

    /**
     * Add a single aircraft marker to the map
     * Creates a custom icon, popup, and click handler for each aircraft
     */
    addAircraftMarker(aircraft) {
        // Create custom icon using a div element (instead of default pin icon)
        // L.divIcon allows us to use HTML/CSS for full styling control
        const markerIcon = L.divIcon({
            className: 'aircraft-marker', // CSS class for styling (see style.css)
            html: '✈', // Airplane emoji as the icon
            iconSize: [20, 20], // Width and height in pixels
            iconAnchor: [10, 10] // Point of the icon which corresponds to marker's location (center)
        });

        // Create the Leaflet marker at the aircraft's coordinates
        const marker = L.marker([aircraft.latitude, aircraft.longitude], {
            icon: markerIcon,
            title: aircraft.callsign // Tooltip text on hover
        });

        // Create HTML content for the popup that appears when clicking the marker
        const popupContent = this.createAircraftPopup(aircraft);
        marker.bindPopup(popupContent); // Attach popup to the marker

        // Add click event listener to the marker
        marker.on('click', (e) => {
            // Stop propagation prevents the map's click event from also firing
            // Without this, clicking a marker would immediately deselect it
            e.originalEvent.stopPropagation();
            this.selectAircraft(aircraft, marker); // Call select method with aircraft data and marker
        });

        // Add the marker to the map so it becomes visible
        marker.addTo(this.map);

        // Store reference to both the marker and aircraft data for later access
        // This allows us to update, remove, or style the marker later
        this.aircraftMarkers.set(aircraft.id, {
            marker: marker,
            aircraft: aircraft
        });
    }

    /**
     * Create popup content for aircraft
     * Generates HTML string for the popup that appears when clicking a marker
     * Using template literals (backticks) for easy multiline HTML
     */
    createAircraftPopup(aircraft) {
        return `
            <div class="aircraft-popup">
                <div class="callsign">${aircraft.callsign}</div>
                <div class="details">
                    <strong>Type:</strong> ${aircraft.aircraft_type}<br>
                    <strong>Altitude:</strong> ${aircraft.altitude.toLocaleString()} ft<br>
                    <strong>Speed:</strong> ${aircraft.speed} kts<br>
                    <strong>Heading:</strong> ${aircraft.heading}°<br>
                    <strong>Position:</strong> ${aircraft.latitude.toFixed(4)}, ${aircraft.longitude.toFixed(4)}
                </div>
            </div>
        `;
    }

    /**
     * Select an aircraft and show detailed information
     * Highlights the marker and populates the info panel in the sidebar
     */
    selectAircraft(aircraft, marker) {
        // First, deselect any previously selected aircraft
        // This ensures only one aircraft is selected at a time
        this.deselectAircraft();

        // Store the selected aircraft in instance variable for later reference
        this.selectedAircraft = aircraft;

        // Update the marker's visual appearance to show it's selected
        // getElement() returns the actual DOM element of the marker
        const markerElement = marker.getElement();
        if (markerElement) {
            // Add 'selected' class which changes color to red (see style.css)
            markerElement.classList.add('selected');
        }

        // Update the sidebar info panel with detailed aircraft information
        this.updateAircraftInfoPanel(aircraft);

        console.log(`Selected aircraft: ${aircraft.callsign}`);
    }

    /**
     * Deselect currently selected aircraft
     * Removes highlighting and clears the info panel
     */
    deselectAircraft() {
        // Only do something if there's actually an aircraft selected
        if (this.selectedAircraft) {
            // Remove the 'selected' class from all markers
            // We iterate through all markers because we don't know which one is selected
            this.aircraftMarkers.forEach(({marker}) => {
                const markerElement = marker.getElement();
                if (markerElement) {
                    markerElement.classList.remove('selected'); // Remove red highlighting
                }
            });

            // Clear the selected aircraft reference
            this.selectedAircraft = null;

            // Reset the info panel to default "Select an aircraft" message
            this.clearAircraftInfoPanel();
        }
    }

    /**
     * Update the aircraft information panel
     * Populates the sidebar panel with detailed aircraft data
     * Using innerHTML to dynamically generate HTML content
     */
    updateAircraftInfoPanel(aircraft) {
        const infoPanel = document.getElementById('aircraftInfo');
        if (infoPanel) {
            // Replace the panel content with formatted aircraft details
            // toLocaleString() adds comma separators to numbers (e.g., 25000 -> 25,000)
            // toFixed(4) limits coordinates to 4 decimal places for readability
            infoPanel.innerHTML = `
                <div class="aircraft-detail">
                    <span class="label">Callsign:</span>
                    <span class="value">${aircraft.callsign}</span>
                </div>
                <div class="aircraft-detail">
                    <span class="label">Aircraft:</span>
                    <span class="value">${aircraft.aircraft_type}</span>
                </div>
                <div class="aircraft-detail">
                    <span class="label">Altitude:</span>
                    <span class="value">${aircraft.altitude.toLocaleString()} ft</span>
                </div>
                <div class="aircraft-detail">
                    <span class="label">Speed:</span>
                    <span class="value">${aircraft.speed} kts</span>
                </div>
                <div class="aircraft-detail">
                    <span class="label">Heading:</span>
                    <span class="value">${aircraft.heading}°</span>
                </div>
                <div class="aircraft-detail">
                    <span class="label">Position:</span>
                    <span class="value">${aircraft.latitude.toFixed(4)}, ${aircraft.longitude.toFixed(4)}</span>
                </div>
            `;
        }
    }

    /**
     * Clear the aircraft information panel
     * Resets the panel to show the default "no selection" message
     */
    clearAircraftInfoPanel() {
        const infoPanel = document.getElementById('aircraftInfo');
        if (infoPanel) {
            // Reset to default prompt message
            infoPanel.innerHTML = '<p>Select an aircraft to view details</p>';
        }
    }

    /**
     * Filter aircraft by minimum altitude
     * Shows/hides markers based on whether they meet the altitude threshold
     * This allows controllers to focus on specific altitude ranges
     */
    filterAircraftByAltitude(minAltitude) {
        // Iterate through all aircraft markers
        this.aircraftMarkers.forEach(({marker, aircraft}) => {
            // Check if this aircraft's altitude meets the minimum threshold
            if (aircraft.altitude >= minAltitude) {
                marker.addTo(this.map); // Show the marker (or keep it visible)
            } else {
                this.map.removeLayer(marker); // Hide the marker
            }
        });
    }

    /**
     * Toggle flight path visibility
     * Placeholder for future feature to show historical flight paths
     * This would draw polylines showing where aircraft have been
     */
    toggleFlightPaths(show) {
        // TODO: Implement flight path visualization
        // Would require backend to store historical position data
        // Would use L.polyline() to draw paths on the map
        console.log(`Flight paths ${show ? 'enabled' : 'disabled'}`);
    }

    /**
     * Update connection status indicator
     * Updates the colored dot and status text in the header
     * Provides visual feedback about backend connectivity
     */
    updateConnectionStatus(connected, message) {
        const statusDot = document.getElementById('connectionStatus');
        const statusText = document.getElementById('statusText');

        if (statusDot) {
            // toggle() adds/removes the 'connected' class based on the boolean parameter
            // 'connected' class makes the dot green, absence makes it red (see style.css)
            statusDot.classList.toggle('connected', connected);
        }

        if (statusText) {
            // Update the status message (e.g., "Connected", "Initializing...", "Connection Failed")
            statusText.textContent = message;
        }

        // Store connection state for use in periodic updates
        this.isConnected = connected;
    }

    /**
     * Update statistics display
     * Shows the total number of aircraft and last update timestamp
     * Called every time we successfully load new aircraft data
     */
    updateStatistics(aircraftData) {
        const totalAircraft = document.getElementById('totalAircraft');
        const lastUpdate = document.getElementById('lastUpdate');

        if (totalAircraft) {
            // Display the count of aircraft currently in the data
            totalAircraft.textContent = aircraftData.length;
        }

        if (lastUpdate) {
            // Display current time in user's local format (e.g., "2:34:56 PM")
            lastUpdate.textContent = new Date().toLocaleTimeString();
        }
    }

    /**
     * Start periodic data updates
     * Sets up an interval timer to automatically refresh aircraft data
     * Prevents stale data by fetching new positions every 5 seconds
     */
    startPeriodicUpdates() {
        // setInterval() executes the callback function repeatedly at specified intervals
        this.refreshInterval = setInterval(() => {
            // Only fetch data if we're successfully connected
            // This prevents error spam if the backend is down
            if (this.isConnected) {
                this.loadAircraftData();
            }
        }, this.config.refreshRate); // 5000ms = 5 seconds

        console.log(`Started periodic updates every ${this.config.refreshRate}ms`);
    }

    /**
     * Stop periodic data updates
     * Clears the interval timer to prevent memory leaks
     * Important to call this when the component is destroyed
     */
    stopPeriodicUpdates() {
        if (this.refreshInterval) {
            // clearInterval() stops the timer created by setInterval()
            clearInterval(this.refreshInterval);
            this.refreshInterval = null; // Clear the reference
            console.log('Stopped periodic updates');
        }
    }

    /**
     * Cleanup when the system is destroyed
     * Properly disposes of resources to prevent memory leaks
     * Should be called before navigating away or closing the app
     */
    destroy() {
        // Stop the periodic update timer
        this.stopPeriodicUpdates();

        // Remove the Leaflet map and all its event listeners
        if (this.map) {
            this.map.remove(); // Leaflet's built-in cleanup method
        }

        console.log('ATC System destroyed');
    }
}

// Make ATCSystem available globally by attaching it to the window object
// This allows index.html to access it via: window.atcSystem = new ATCSystem()
// Without this, the class would only be accessible within this file's scope
window.ATCSystem = ATCSystem;