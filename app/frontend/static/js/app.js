/**
 * Air Traffic Control System Frontend
 * Main JavaScript application for the ATC dashboard
 */

class ATCSystem {
    constructor() {
        this.map = null;
        this.aircraftMarkers = new Map();
        this.selectedAircraft = null;
        this.refreshInterval = null;
        this.isConnected = false;
        
        // Configuration
        this.config = {
            refreshRate: 5000, // 5 seconds
            mapCenter: [35.4676, -97.5164], // Oklahoma City
            mapZoom: 9,
            maxAircraftAge: 30000 // 30 seconds
        };
    }

    /**
     * Initialize the ATC System
     */
    async init() {
        try {
            console.log('Initializing ATC System...');
            
            this.initMap();
            this.initControls();
            this.updateConnectionStatus(false, 'Initializing...');
            
            // Load initial aircraft data
            await this.loadAircraftData();
            
            // Start periodic updates
            this.startPeriodicUpdates();
            
            this.updateConnectionStatus(true, 'Connected (Mock Data)');
            console.log('ATC System initialized successfully');
            
        } catch (error) {
            console.error('Failed to initialize ATC System:', error);
            this.updateConnectionStatus(false, 'Connection Failed');
        }
    }

    /**
     * Initialize the Leaflet map
     */
    initMap() {
        // Initialize map
        this.map = L.map('map').setView(this.config.mapCenter, this.config.mapZoom);

        // Add tile layer (dark theme for ATC)
        // Try local tiles first, fallback to online if not available
        const tileLayer = L.tileLayer('/tiles/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors, © CARTO',
            maxZoom: 19,
            errorTileUrl: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=='
        });

        // Fallback to online tiles if local tiles fail
        tileLayer.on('tileerror', () => {
            console.warn('Local tile not found, using online tiles');
            if (!this.onlineTileLayerAdded) {
                this.map.removeLayer(tileLayer);
                L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                    attribution: '© OpenStreetMap contributors, © CARTO',
                    maxZoom: 19
                }).addTo(this.map);
                this.onlineTileLayerAdded = true;
            }
        });

        tileLayer.addTo(this.map);

        // Add map event listeners
        this.map.on('click', () => {
            this.deselectAircraft();
        });

        console.log('Map initialized');
    }

    /**
     * Initialize UI controls and event listeners
     */
    initControls() {
        // Refresh button
        const refreshBtn = document.getElementById('refreshData');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => {
                this.loadAircraftData();
            });
        }

        // Altitude filter
        const altitudeFilter = document.getElementById('altitudeFilter');
        const altitudeValue = document.getElementById('altitudeValue');
        if (altitudeFilter && altitudeValue) {
            altitudeFilter.addEventListener('input', (e) => {
                const value = e.target.value;
                altitudeValue.textContent = value;
                this.filterAircraftByAltitude(parseInt(value));
            });
        }

        // Show paths checkbox
        const showPaths = document.getElementById('showPaths');
        if (showPaths) {
            showPaths.addEventListener('change', (e) => {
                this.toggleFlightPaths(e.target.checked);
            });
        }

        console.log('Controls initialized');
    }

    /**
     * Load aircraft data from the API
     */
    async loadAircraftData() {
        try {
            const response = await fetch('/api/aircraft');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const aircraftData = await response.json();
            this.updateAircraftOnMap(aircraftData);
            this.updateStatistics(aircraftData);
            
            console.log(`Loaded ${aircraftData.length} aircraft`);
            
        } catch (error) {
            console.error('Failed to load aircraft data:', error);
            this.updateConnectionStatus(false, 'Data Load Failed');
        }
    }

    /**
     * Update aircraft markers on the map
     */
    updateAircraftOnMap(aircraftData) {
        // Remember which aircraft was selected (by ID)
        const selectedId = this.selectedAircraft ? this.selectedAircraft.id : null;

        // Clear existing markers
        this.aircraftMarkers.forEach(({marker}) => {
            this.map.removeLayer(marker);
        });
        this.aircraftMarkers.clear();

        // Reset selection state before adding new markers
        this.selectedAircraft = null;

        // Add new markers
        aircraftData.forEach(aircraft => {
            this.addAircraftMarker(aircraft);

            // Restore selection if this was the selected aircraft
            if (selectedId && aircraft.id === selectedId) {
                const markerData = this.aircraftMarkers.get(aircraft.id);
                if (markerData) {
                    this.selectedAircraft = aircraft;
                    const markerElement = markerData.marker.getElement();
                    if (markerElement) {
                        markerElement.classList.add('selected');
                    }
                    this.updateAircraftInfoPanel(aircraft);
                }
            }
        });
    }

    /**
     * Add a single aircraft marker to the map
     */
    addAircraftMarker(aircraft) {
        // Create custom airplane icon with rotation based on heading
        const heading = aircraft.heading || 0;
        const markerIcon = L.divIcon({
            className: 'aircraft-marker',
            html: `<svg viewBox="0 0 24 24" style="transform: rotate(${heading}deg)">
                <path fill="currentColor" d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/>
            </svg>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14]
        });

        // Create marker
        const marker = L.marker([aircraft.latitude, aircraft.longitude], {
            icon: markerIcon,
            title: aircraft.callsign
        });

        // Create popup content
        const popupContent = this.createAircraftPopup(aircraft);
        marker.bindPopup(popupContent);

        // Add click event
        marker.on('click', (e) => {
            e.originalEvent.stopPropagation();
            this.selectAircraft(aircraft, marker);
        });

        // Add to map and store reference
        marker.addTo(this.map);
        this.aircraftMarkers.set(aircraft.id, {
            marker: marker,
            aircraft: aircraft
        });
    }

    /**
     * Create popup content for aircraft
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
     */
    selectAircraft(aircraft, marker) {
        // Deselect previous aircraft
        this.deselectAircraft();

        // Select new aircraft
        this.selectedAircraft = aircraft;
        
        // Update marker appearance
        const markerElement = marker.getElement();
        if (markerElement) {
            markerElement.classList.add('selected');
        }

        // Update aircraft info panel
        this.updateAircraftInfoPanel(aircraft);

        console.log(`Selected aircraft: ${aircraft.callsign}`);
    }

    /**
     * Deselect currently selected aircraft
     */
    deselectAircraft() {
        if (this.selectedAircraft) {
            // Remove selection styling from marker
            this.aircraftMarkers.forEach(({marker}) => {
                const markerElement = marker.getElement();
                if (markerElement) {
                    markerElement.classList.remove('selected');
                }
            });

            this.selectedAircraft = null;
            this.clearAircraftInfoPanel();
        }
    }

    /**
     * Update the aircraft information panel
     */
    updateAircraftInfoPanel(aircraft) {
        const infoPanel = document.getElementById('aircraftInfo');
        if (infoPanel) {
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
     */
    clearAircraftInfoPanel() {
        const infoPanel = document.getElementById('aircraftInfo');
        if (infoPanel) {
            infoPanel.innerHTML = '<p>Select an aircraft to view details</p>';
        }
    }

    /**
     * Filter aircraft by minimum altitude
     */
    filterAircraftByAltitude(minAltitude) {
        this.aircraftMarkers.forEach(({marker, aircraft}) => {
            if (aircraft.altitude >= minAltitude) {
                marker.addTo(this.map);
            } else {
                this.map.removeLayer(marker);
            }
        });
    }

    /**
     * Toggle flight path visibility
     */
    toggleFlightPaths(show) {
        // This would show/hide flight path lines
        // For now, just log the action
        console.log(`Flight paths ${show ? 'enabled' : 'disabled'}`);
    }

    /**
     * Update connection status indicator
     */
    updateConnectionStatus(connected, message) {
        const statusDot = document.getElementById('connectionStatus');
        const statusText = document.getElementById('statusText');
        
        if (statusDot) {
            statusDot.classList.toggle('connected', connected);
        }
        
        if (statusText) {
            statusText.textContent = message;
        }
        
        this.isConnected = connected;
    }

    /**
     * Update statistics display
     */
    updateStatistics(aircraftData) {
        const totalAircraft = document.getElementById('totalAircraft');
        const lastUpdate = document.getElementById('lastUpdate');
        
        if (totalAircraft) {
            totalAircraft.textContent = aircraftData.length;
        }
        
        if (lastUpdate) {
            lastUpdate.textContent = new Date().toLocaleTimeString();
        }
    }

    /**
     * Start periodic data updates
     */
    startPeriodicUpdates() {
        this.refreshInterval = setInterval(() => {
            if (this.isConnected) {
                this.loadAircraftData();
            }
        }, this.config.refreshRate);
        
        console.log(`Started periodic updates every ${this.config.refreshRate}ms`);
    }

    /**
     * Stop periodic data updates
     */
    stopPeriodicUpdates() {
        if (this.refreshInterval) {
            clearInterval(this.refreshInterval);
            this.refreshInterval = null;
            console.log('Stopped periodic updates');
        }
    }

    /**
     * Cleanup when the system is destroyed
     */
    destroy() {
        this.stopPeriodicUpdates();
        
        if (this.map) {
            this.map.remove();
        }
        
        console.log('ATC System destroyed');
    }
}

// Make ATCSystem available globally
window.ATCSystem = ATCSystem;