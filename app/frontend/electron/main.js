/**
 * Electron Main Process
 * This is the entry point for the Electron desktop application
 *
 * Responsibilities:
 * - Spawn and manage the Flask backend server as a subprocess
 * - Create the native application window
 * - Handle application lifecycle events (startup, shutdown, etc.)
 * - Monitor Flask server health and readiness
 * - Gracefully cleanup resources on exit
 *
 * Electron Architecture:
 * - Main Process: This file (Node.js runtime, system access)
 * - Renderer Process: The web content (browser environment, limited access)
 * - Preload Script: Security bridge between main and renderer
 *
 * Author: Andrew Moore
 * Course: Capstone Project - FAA ATC System
 */

// Import Electron modules
const { app, BrowserWindow, dialog } = require('electron');
// app: Controls application lifecycle
// BrowserWindow: Creates native windows
// dialog: Shows native system dialogs (error boxes, file pickers, etc.)

const path = require('path'); // Node.js path utilities for cross-platform file paths
const { spawn } = require('child_process'); // Spawn child processes (for running Flask)
const http = require('http'); // HTTP client for health checks

// Global variables to track application state
let mainWindow; // Reference to the main BrowserWindow instance
let flaskProcess; // Reference to the Flask subprocess
const FLASK_PORT = 5001; // Port where Flask server runs
const FLASK_HOST = '127.0.0.1'; // Localhost (only accept local connections for security)

// Determine if we're in development mode by checking command line arguments
// Run with: npm run dev (includes --dev flag)
// vs: npm start (no --dev flag)
const isDev = process.argv.includes('--dev');

/**
 * Check if Flask server is running
 * Makes an HTTP GET request to the Flask /health endpoint
 * Returns a Promise that resolves to true if server is up, false otherwise
 */
function checkFlaskServer() {
    return new Promise((resolve) => {
        // Make HTTP GET request to Flask health check endpoint
        // The health endpoint returns status 200 if the server is ready
        const req = http.get(`http://${FLASK_HOST}:${FLASK_PORT}/health`, (res) => {
            // Check if response status is 200 (OK)
            // Any other status code (404, 500, etc.) means server isn't ready
            resolve(res.statusCode === 200);
        });

        // If the request fails (connection refused, network error, etc.)
        // This happens when Flask isn't running yet
        req.on('error', () => resolve(false));

        // If the request takes too long (default Node.js timeout)
        // Destroy the request and report server as not ready
        req.on('timeout', () => {
            req.destroy(); // Cancel the request to free up resources
            resolve(false);
        });
    });
}

/**
 * Wait for Flask server to be ready
 * Polls the Flask server repeatedly until it responds or max attempts reached
 * This is necessary because Flask takes time to initialize after spawning
 *
 * @param {number} maxAttempts - Maximum number of check attempts (default 30)
 * @returns {Promise<boolean>} - True if Flask is ready, false if timeout
 */
async function waitForFlask(maxAttempts = 30) {
    console.log('Waiting for Flask server to start...');

    // Try up to maxAttempts times with 500ms delay between each attempt
    // 30 attempts × 500ms = 15 seconds maximum wait time
    for (let i = 0; i < maxAttempts; i++) {
        const isRunning = await checkFlaskServer(); // Check if Flask responds
        if (isRunning) {
            console.log('Flask server is ready!');
            return true; // Flask is up and running!
        }
        // Wait 500ms before trying again
        // Using Promise with setTimeout for async delay
        await new Promise(resolve => setTimeout(resolve, 500));
    }

    // If we get here, Flask never became ready within the timeout period
    return false;
}

/**
 * Start Flask backend server
 * Spawns Flask as a child process so it runs alongside Electron
 * Handles both development (with venv) and production (packaged) environments
 *
 * @returns {Promise} - Resolves after 2 seconds to allow Flask initialization
 */
function startFlaskServer() {
    return new Promise((resolve, reject) => {
        console.log('Starting Flask server...');

        // Determine the path to app.py based on whether we're packaged or in development
        let appPath;
        if (app.isPackaged) {
            // In production: Electron packages app.py into resources/app directory
            // process.resourcesPath points to the resources folder in the .app/.exe
            appPath = path.join(process.resourcesPath, 'app', 'app.py');
        } else {
            // In development: app.py is one directory up from electron/ folder
            appPath = path.join(__dirname, '..', 'app.py');
        }

        console.log('Flask app path:', appPath);
        console.log('Current directory:', __dirname);

        // Determine which Python executable to use
        const isWindows = process.platform === 'win32';
        let pythonCmd = 'python3'; // Default to system python3

        // On macOS/Linux in development, try to use the virtual environment's Python
        // This ensures Flask dependencies are available
        if (!app.isPackaged && !isWindows) {
            const venvPython = path.join(__dirname, '..', 'venv', 'bin', 'python');
            try {
                // Check if venv Python exists before using it
                if (require('fs').existsSync(venvPython)) {
                    pythonCmd = venvPython;
                    console.log('Using venv python:', venvPython);
                }
            } catch (e) {
                // If venv doesn't exist, fall back to system Python
                console.log('Venv not found, using system python');
            }
        }

        // Spawn the Flask process as a child process
        // spawn() creates a new process without blocking the main thread
        flaskProcess = spawn(pythonCmd, [appPath], {
            cwd: path.dirname(appPath), // Set working directory to where app.py is located
            env: {
                ...process.env, // Inherit all existing environment variables
                FLASK_ENV: isDev ? 'development' : 'production', // Set Flask mode
                PYTHONUNBUFFERED: '1' // Force Python to print output immediately (no buffering)
            }
        });

        // Listen for Flask's standard output (normal logs)
        // This captures Flask's startup messages and request logs
        flaskProcess.stdout.on('data', (data) => {
            console.log(`Flask: ${data.toString()}`);
        });

        // Listen for Flask's error output (warnings and errors)
        // Helps debug Flask issues during development
        flaskProcess.stderr.on('data', (data) => {
            console.error(`Flask Error: ${data.toString()}`);
        });

        // Handle errors spawning the Flask process
        // This fires if Python isn't found or app.py path is wrong
        flaskProcess.on('error', (error) => {
            console.error('Failed to start Flask:', error);
            reject(error); // Reject the Promise to signal failure
        });

        // Listen for Flask process exit
        // Logs the exit code (0 = clean exit, non-zero = error)
        flaskProcess.on('close', (code) => {
            console.log(`Flask process exited with code ${code}`);
        });

        // Wait 2 seconds before resolving to give Flask time to initialize
        // This is a simple delay before we start health checking
        setTimeout(() => resolve(), 2000);
    });
}

/**
 * Create the main application window
 * Sets up the Electron BrowserWindow with proper security settings
 * Loads the Flask web application inside the native window
 */
function createWindow() {
    // Create a new BrowserWindow (native desktop window)
    mainWindow = new BrowserWindow({
        width: 1400,           // Default window width in pixels
        height: 900,           // Default window height in pixels
        minWidth: 1000,        // Minimum width (prevents UI from breaking)
        minHeight: 600,        // Minimum height
        title: 'ATC System',   // Window title (shows in taskbar/dock)
        backgroundColor: '#1a1a1a', // Background color (matches dark theme)
        webPreferences: {
            // Security settings (important for Electron best practices)
            nodeIntegration: false,  // Disable Node.js in renderer process (security)
            contextIsolation: true,  // Isolate preload context from web content (security)
            preload: path.join(__dirname, 'preload.js') // Load preload script for secure IPC
        },
        icon: path.join(__dirname, '..', 'static', 'icon.png') // Optional: app icon
    });

    // Load the Flask application URL into the window
    // This makes the window display the Flask web app as if it were a browser
    mainWindow.loadURL(`http://${FLASK_HOST}:${FLASK_PORT}`);

    // Open Chrome DevTools automatically in development mode
    // DevTools allow us to debug JavaScript, inspect HTML, view console logs, etc.
    if (isDev) {
        mainWindow.webContents.openDevTools();
    }

    // Handle window close event
    // Clean up the reference when window is closed to allow garbage collection
    mainWindow.on('closed', () => {
        mainWindow = null;
    });

    // Handle loading errors (e.g., Flask server not responding)
    // Note: 'event' parameter is required by Electron but not used here
    mainWindow.webContents.on('did-fail-load', (_event, errorCode, errorDescription) => {
        console.error('Failed to load:', errorCode, errorDescription);

        // Error code -102 = ERR_CONNECTION_REFUSED (Flask not running)
        if (errorCode === -102) {
            dialog.showErrorBox(
                'Connection Error',
                'Failed to connect to Flask server. The application will close.'
            );
            app.quit(); // Exit the app since we can't function without Flask
        }
    });

    console.log('Main window created');
}

/**
 * Initialize the application
 * This is the main startup sequence that orchestrates the entire app launch
 * Called when Electron is ready (after app.whenReady() event)
 */
async function initialize() {
    try {
        // Step 1: Start the Flask backend server
        // This spawns Python as a child process
        await startFlaskServer();

        // Step 2: Wait for Flask to actually be ready to accept requests
        // Even though Flask is spawned, it takes time to initialize
        const flaskReady = await waitForFlask();

        // Step 3: Check if Flask became ready within the timeout period
        if (!flaskReady) {
            console.error('Flask server failed to start in time');
            // Show user-friendly error dialog
            dialog.showErrorBox(
                'Server Error',
                'Failed to start the backend server. Please check the logs.'
            );
            app.quit(); // Exit since we can't run without Flask
            return;
        }

        // Step 4: Create the application window now that Flask is running
        // The window will load http://127.0.0.1:5001 and display the UI
        createWindow();

    } catch (error) {
        // Catch any errors during the initialization process
        console.error('Initialization error:', error);
        dialog.showErrorBox(
            'Initialization Error',
            `Failed to initialize application: ${error.message}`
        );
        app.quit(); // Exit on fatal initialization errors
    }
}

/**
 * Cleanup on application quit
 * Gracefully terminates the Flask subprocess to prevent orphaned processes
 * Called when the app is closing to ensure proper cleanup
 */
function cleanup() {
    console.log('Cleaning up...');

    if (flaskProcess) {
        console.log('Terminating Flask process...');
        // SIGTERM = polite request for process to terminate (allows cleanup)
        flaskProcess.kill('SIGTERM');

        // Force kill after 2 seconds if Flask doesn't exit gracefully
        // This prevents the Flask process from becoming an orphan (running without parent)
        setTimeout(() => {
            if (flaskProcess && !flaskProcess.killed) {
                console.log('Force killing Flask process...');
                // SIGKILL = immediate termination (cannot be caught or ignored)
                flaskProcess.kill('SIGKILL');
            }
        }, 2000);
    }
}

// ============================================================================
// Electron Application Event Handlers
// These respond to various application lifecycle events
// ============================================================================

// When Electron is fully initialized and ready to create windows
// This is the main entry point for the application
app.whenReady().then(initialize);

// When all windows are closed
app.on('window-all-closed', () => {
    cleanup(); // Terminate Flask process
    // On macOS, apps typically stay open even when all windows are closed
    // Users quit via Cmd+Q or the menu. Other platforms quit immediately.
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

// macOS-specific: Clicking dock icon when no windows are open
app.on('activate', () => {
    // Re-create the window if none exist
    // This is standard macOS behavior (like clicking Safari in the dock)
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

// Before the app quits (opportunity for cleanup)
app.on('before-quit', cleanup);

// Right before the app actually quits (last chance for cleanup)
app.on('will-quit', cleanup);

// Handle any uncaught JavaScript exceptions
// This prevents the app from silently crashing
process.on('uncaughtException', (error) => {
    console.error('Uncaught exception:', error);
    cleanup(); // Try to cleanup even on unexpected errors
});
