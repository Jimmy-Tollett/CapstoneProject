const { app, BrowserWindow, dialog } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const http = require('http');

let mainWindow;
let flaskProcess;
const FLASK_PORT = 5001;
const FLASK_HOST = '127.0.0.1';

// Determine if we're in development mode
const isDev = process.argv.includes('--dev');

/**
 * Check if Flask server is running
 */
function checkFlaskServer() {
    return new Promise((resolve) => {
        const options = {
            host: FLASK_HOST,
            port: FLASK_PORT,
            path: '/health',
            timeout: 1000
        };

        const req = http.get(`http://${FLASK_HOST}:${FLASK_PORT}/health`, (res) => {
            resolve(res.statusCode === 200);
        });

        req.on('error', () => resolve(false));
        req.on('timeout', () => {
            req.destroy();
            resolve(false);
        });
    });
}

/**
 * Wait for Flask server to be ready
 */
async function waitForFlask(maxAttempts = 30) {
    console.log('Waiting for Flask server to start...');

    for (let i = 0; i < maxAttempts; i++) {
        const isRunning = await checkFlaskServer();
        if (isRunning) {
            console.log('Flask server is ready!');
            return true;
        }
        await new Promise(resolve => setTimeout(resolve, 500));
    }

    return false;
}

/**
 * Start Flask backend server
 */
function startFlaskServer() {
    return new Promise((resolve, reject) => {
        console.log('Starting Flask server...');

        // Determine the path to app.py
        let appPath;
        if (app.isPackaged) {
            // In production, Flask app is in resources/app
            appPath = path.join(process.resourcesPath, 'app', 'app.py');
        } else {
            // In development, use the current directory
            appPath = path.join(__dirname, '..', 'app.py');
        }

        console.log('Flask app path:', appPath);
        console.log('Current directory:', __dirname);

        // Check if we need to activate venv
        const isWindows = process.platform === 'win32';
        let pythonCmd = 'python3';

        // On macOS/Linux in development, try to use venv python
        if (!app.isPackaged && !isWindows) {
            const venvPython = path.join(__dirname, '..', 'venv', 'bin', 'python');
            try {
                if (require('fs').existsSync(venvPython)) {
                    pythonCmd = venvPython;
                    console.log('Using venv python:', venvPython);
                }
            } catch (e) {
                console.log('Venv not found, using system python');
            }
        }

        // Spawn Flask process
        flaskProcess = spawn(pythonCmd, [appPath], {
            cwd: path.dirname(appPath),
            env: {
                ...process.env,
                FLASK_ENV: isDev ? 'development' : 'production',
                PYTHONUNBUFFERED: '1'
            }
        });

        flaskProcess.stdout.on('data', (data) => {
            console.log(`Flask: ${data.toString()}`);
        });

        flaskProcess.stderr.on('data', (data) => {
            console.error(`Flask Error: ${data.toString()}`);
        });

        flaskProcess.on('error', (error) => {
            console.error('Failed to start Flask:', error);
            reject(error);
        });

        flaskProcess.on('close', (code) => {
            console.log(`Flask process exited with code ${code}`);
        });

        // Wait a bit for Flask to start
        setTimeout(() => resolve(), 2000);
    });
}

/**
 * Create the main application window
 */
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1400,
        height: 900,
        minWidth: 1000,
        minHeight: 600,
        title: 'ATC System',
        backgroundColor: '#1a1a1a',
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js')
        },
        icon: path.join(__dirname, '..', 'static', 'icon.png') // Optional: add an icon
    });

    // Load the Flask application
    mainWindow.loadURL(`http://${FLASK_HOST}:${FLASK_PORT}`);

    // Open DevTools in development mode
    if (isDev) {
        mainWindow.webContents.openDevTools();
    }

    // Handle window close
    mainWindow.on('closed', () => {
        mainWindow = null;
    });

    // Handle loading errors
    mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription) => {
        console.error('Failed to load:', errorCode, errorDescription);

        if (errorCode === -102) { // Connection refused
            dialog.showErrorBox(
                'Connection Error',
                'Failed to connect to Flask server. The application will close.'
            );
            app.quit();
        }
    });

    console.log('Main window created');
}

/**
 * Initialize the application
 */
async function initialize() {
    try {
        // Start Flask server
        await startFlaskServer();

        // Wait for Flask to be ready
        const flaskReady = await waitForFlask();

        if (!flaskReady) {
            console.error('Flask server failed to start in time');
            dialog.showErrorBox(
                'Server Error',
                'Failed to start the backend server. Please check the logs.'
            );
            app.quit();
            return;
        }

        // Create the window
        createWindow();

    } catch (error) {
        console.error('Initialization error:', error);
        dialog.showErrorBox(
            'Initialization Error',
            `Failed to initialize application: ${error.message}`
        );
        app.quit();
    }
}

/**
 * Cleanup on application quit
 */
function cleanup() {
    console.log('Cleaning up...');

    if (flaskProcess) {
        console.log('Terminating Flask process...');
        flaskProcess.kill('SIGTERM');

        // Force kill after 2 seconds if not terminated
        setTimeout(() => {
            if (flaskProcess && !flaskProcess.killed) {
                console.log('Force killing Flask process...');
                flaskProcess.kill('SIGKILL');
            }
        }, 2000);
    }
}

// App event handlers
app.whenReady().then(initialize);

app.on('window-all-closed', () => {
    cleanup();
    // On macOS, applications typically stay open until user quits explicitly
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    // On macOS, re-create window when dock icon is clicked and no windows are open
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

app.on('before-quit', cleanup);

app.on('will-quit', cleanup);

// Handle any uncaught exceptions
process.on('uncaughtException', (error) => {
    console.error('Uncaught exception:', error);
    cleanup();
});
