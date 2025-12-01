# Air Traffic Control System - Desktop Application

## Project Overview
This is the GUI component of the FAA Air Traffic Control System capstone project. The application provides real-time visualization of flight data through interactive maps and dashboards for air traffic controllers.

**Deployment Target**: Red Hat Enterprise Linux (RHEL) Desktop Application

## Current Status: Desktop Application Ready ✅

### What's Been Completed
- ✅ Flask backend with API endpoints
- ✅ Interactive web interface with Leaflet.js map
- ✅ Aircraft position display with mock data
- ✅ Control panel with filters and statistics
- ✅ **Electron desktop wrapper implemented**
- ✅ **Offline map tile support with online fallback**
- ✅ **RHEL packaging configuration (RPM + AppImage)**

### What's Next
- [ ] Connect to real ASTERIX data backend
- [ ] Implement WebSocket for real-time updates
- [ ] Add flight path visualization
- [ ] Enhance UI/UX
- [ ] Security implementation
- [ ] Performance optimization

## Technology Stack

### Desktop Application Layer
- **Desktop Framework**: Electron 28.0.0
- **Packaging**: electron-builder (RPM, AppImage)
- **Platform**: Cross-platform (RHEL primary target)

### Backend
- **Server**: Flask (Python 3.8+)
- **API**: REST endpoints
- **Future**: WebSocket support for real-time data

### Frontend
- **UI Framework**: HTML5/CSS3/JavaScript
- **Mapping**: Leaflet.js
- **Map Tiles**: CartoDB Dark theme (with offline support)
- **Styling**: Custom CSS (dark theme for ATC operations)

## Quick Start

### Prerequisites

#### Required Software
- **Node.js** (v16 or later): [Download](https://nodejs.org/)
- **Python 3** (3.8 or later)
- **npm** (comes with Node.js)

#### For Red Hat Linux Development
```bash
# Install Node.js on RHEL/CentOS/Fedora
sudo dnf install nodejs npm

# Install build tools
sudo dnf groupinstall "Development Tools"

# Install X11 dependencies (if not already installed)
sudo dnf install libX11 libXScrnSaver gtk3
```

### Installation

#### Option 1: Quick Setup Script
```bash
cd frontend
./electron/build-setup.sh
```

#### Option 2: Manual Setup
```bash
# Install Node.js dependencies
npm install

# Install/activate Python virtual environment
source venv/bin/activate  # or create with: python3 -m venv venv
pip install -r requirements.txt
```

### Running the Application

#### Development Mode (with DevTools)
```bash
npm run dev
```
This will:
- Start Flask backend on port 5001
- Launch Electron window with Chrome DevTools open
- Enable hot-reload for debugging

#### Production Mode
```bash
npm start
```
Runs the application without DevTools.

#### Web-only Mode (Original Flask)
```bash
source venv/bin/activate
python app.py
# Open browser to http://localhost:5001
```

## Building for Distribution

### Build for Linux (Recommended)
```bash
# Build both RPM and AppImage
npm run build:linux
```

Output files will be in `dist/` directory:
- `dist/*.rpm` - For RHEL/Fedora/CentOS
- `dist/*.AppImage` - Universal Linux portable executable

### Build Specific Formats
```bash
npm run build:rpm        # RPM package only
npm run build:appimage   # AppImage only
```

## Installing on Red Hat Linux

### RPM Installation
```bash
# Install the RPM package
sudo rpm -i dist/atc-system-*.rpm

# Or using dnf (recommended)
sudo dnf install dist/atc-system-*.rpm

# Run the application
atc-system
```

### AppImage (No Installation)
```bash
# Make executable
chmod +x dist/ATC-System-*.AppImage

# Run directly
./dist/ATC-System-*.AppImage
```

## Project Structure

```
frontend/
├── electron/
│   ├── main.js              # Electron main process (launches Flask + window)
│   ├── preload.js           # Security preload script
│   └── build-setup.sh       # Setup script
├── app.py                   # Flask backend entry point
├── templates/
│   ├── index.html           # Main dashboard
│   └── base.html            # Base template
├── static/
│   ├── css/
│   │   └── style.css        # Custom ATC dark theme
│   ├── js/
│   │   └── app.js           # Main application JavaScript
│   └── assets/              # (Future: images, icons)
├── tiles/                   # (Optional) Offline map tiles
├── venv/                    # Python virtual environment
├── package.json             # Node.js/Electron configuration
├── requirements.txt         # Python dependencies
├── README.md                # Original planning document
├── ELECTRON_README.md       # Electron-specific documentation
└── README_COMBINED.md       # This file
```

## How It Works

### Architecture Overview

1. **Electron Main Process** (`electron/main.js`)
   - Spawns Flask as a subprocess on port 5001
   - Creates native application window (1400x900)
   - Manages application lifecycle
   - Handles cleanup on exit

2. **Flask Backend** (`app.py`)
   - Serves HTML templates and static files
   - Provides REST API endpoints (`/api/aircraft`)
   - Serves map tiles (`/tiles/{z}/{x}/{y}.png`)
   - Generates mock aircraft data (for development)
   - Health check endpoint (`/health`)

3. **Frontend** (`static/js/app.js`)
   - ATCSystem class manages the application state
   - Leaflet.js handles map rendering
   - Fetches aircraft data every 5 seconds
   - Displays aircraft markers with popups
   - Control panel for filtering and statistics
   - Tries local map tiles first, falls back to online

### Map Tile Strategy

The application uses a smart fallback system:
1. **Attempts to load local tiles** from `/tiles/{z}/{x}/{y}.png`
2. **Falls back to online tiles** from CartoDB if local not found
3. **Works offline** if tiles are pre-downloaded (optional)

## Setting Up Offline Maps (Optional)

For fully offline operation, you can pre-download map tiles.

### Download Map Tiles

1. Create tiles directory:
```bash
mkdir -p tiles
```

2. Download tiles using a tile downloader:
   - [MOBAC (Mobile Atlas Creator)](https://mobac.sourceforge.io/) - GUI tool
   - [Tile Proxy](https://github.com/mapbox/tile-proxy) - CLI tool
   - [OpenMapTiles](https://openmaptiles.org/) - Self-hosted solution

3. Organize tiles in this structure:
```
tiles/
  └── {z}/         # Zoom level (e.g., 9)
      └── {x}/     # X coordinate
          └── {y}.png  # Y coordinate tile
```

4. Recommended zoom levels for your area:
   - DFW Airport region: zoom 8-11
   - Tiles needed: ~500-2000 files per zoom level

### Using Online Tiles (Current Default)

No setup required. The application will automatically use CartoDB's dark theme tiles when local tiles aren't available. Requires internet connection.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard page |
| `/api/aircraft` | GET | Returns JSON array of aircraft data |
| `/health` | GET | Health check (returns `{"status": "ok"}`) |
| `/tiles/{z}/{x}/{y}.png` | GET | Serves map tiles (local or 404) |

### Aircraft Data Format
```json
[
  {
    "id": 1,
    "callsign": "AAL123",
    "latitude": 32.8998,
    "longitude": -97.0403,
    "altitude": 25000,
    "speed": 450,
    "heading": 270,
    "aircraft_type": "B737",
    "timestamp": 1728779123
  }
]
```

## Features

### Current Features ✅
- **Interactive Map**: Pan, zoom, and click aircraft for details
- **Aircraft Markers**: Real-time position display with custom icons
- **Information Panel**: Detailed aircraft info on selection
- **Filters**: Altitude filter slider
- **Statistics**: Total aircraft count, last update time
- **Connection Status**: Visual indicator in header
- **Refresh Control**: Manual data refresh button
- **Dark Theme**: Professional ATC-style interface

### Planned Features 🚧
- Real-time updates via WebSocket
- Flight path visualization with history trails
- Aircraft movement animation
- Search/filter by callsign
- Alert system for conflicts
- Connection to real ASTERIX backend
- User authentication
- Multi-sector support
- Performance optimizations for 100+ aircraft

## Development

### Development Workflow

1. **Make changes** to Flask/HTML/CSS/JS files
2. **Restart the app** to see changes (`npm run dev`)
3. **Use DevTools** for debugging (Ctrl+Shift+I / Cmd+Option+I)
4. **Check Flask logs** in the terminal for backend issues

### File Watching (Optional)
Currently, hot-reload is not enabled. You must restart the app after changes.

To add hot-reload (future enhancement):
- Use `nodemon` for Electron
- Use Flask's debug mode (already enabled in dev)
- Configure file watchers

### Testing

#### Manual Testing
```bash
# Test Flask backend directly
source venv/bin/activate
python app.py
# Visit http://localhost:5001

# Test Electron wrapper
npm run dev
```

#### Automated Testing (Future)
Planned test suites:
- Unit tests for Flask API endpoints
- Integration tests for WebSocket communication
- End-to-end tests for UI workflows
- Performance tests for data handling

## Troubleshooting

### Flask Won't Start

**Symptom**: Electron window shows "Failed to start Flask server"

**Solutions**:
1. Check Python dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Verify port 5001 is available:
   ```bash
   lsof -i :5001  # Kill any process using the port
   ```
3. Test Flask manually:
   ```bash
   python3 app.py
   ```

### Window Opens but Shows Connection Error

**Symptom**: "Failed to connect to Flask server" in Electron window

**Solutions**:
1. Check Flask logs in terminal for errors
2. Ensure venv is activated or system Python has Flask
3. Increase wait time in `electron/main.js` line ~178 (currently 30 attempts)

### Build Fails on Linux

**Symptom**: Build errors during `npm run build`

**Solutions**:
```bash
# Install required development tools
sudo dnf groupinstall "Development Tools"
sudo dnf install rpm-build

# Clean and retry
rm -rf node_modules dist
npm install
npm run build
```

### Map Doesn't Load

**Symptom**: Gray map or missing tiles

**Solutions**:
1. Check internet connection (needed for online tiles)
2. Open DevTools (`npm run dev`) and check console for errors
3. Verify tiles directory structure if using offline tiles
4. Check Flask logs for tile serving errors

### Electron App Won't Launch

**Symptom**: Nothing happens when running `npm start`

**Solutions**:
```bash
# Verify Node.js and npm are installed
node --version
npm --version

# Reinstall dependencies
rm -rf node_modules
npm install

# Try running with verbose logging
npm run dev  # Shows more detailed logs
```

## Performance Notes

- **Startup Time**: ~2-3 seconds (Flask initialization)
- **Memory Usage**: ~150-200MB (Electron + Flask + Chromium)
- **Bundle Size**: ~150-200MB (includes Electron runtime)
- **Network**: Minimal (only map tiles if online, aircraft API is local)
- **CPU Usage**: <5% idle, <15% with active map interactions

## Distribution Checklist

Before distributing your application:

- [ ] Test on target RHEL version (8, 9, or 10)
- [ ] Verify all dependencies are bundled correctly
- [ ] Test offline functionality (if using local tiles)
- [ ] Update version in `package.json`
- [ ] Create release notes
- [ ] Test RPM installation and uninstallation
- [ ] Test AppImage on different Linux distros
- [ ] Include screenshots and user documentation
- [ ] Test on clean RHEL installation
- [ ] Verify proper cleanup on uninstall

## Roadmap

### Phase 1: Foundation ✅ (Completed)
- ✅ Flask backend with API endpoints
- ✅ Basic web interface with map display
- ✅ Aircraft positions visible on map
- ✅ Electron desktop wrapper
- ✅ RHEL packaging

### Phase 2: Integration (In Progress)
- [ ] Connect to real ASTERIX data backend
- [ ] Implement WebSocket for real-time updates
- [ ] Animated flight tracking
- [ ] Flight path visualization
- [ ] Enhanced UI/UX controls

### Phase 3: Production (Future)
- [ ] Performance optimization for 100+ aircraft
- [ ] Security implementation (authentication)
- [ ] Production-ready deployment
- [ ] Comprehensive testing
- [ ] Complete documentation
- [ ] User training materials

## Success Metrics

Target performance goals:
- Real-time aircraft position updates (< 1 second delay)
- Smooth map interaction (60 FPS)
- Handle 100+ simultaneous aircraft
- 99% uptime during operations
- <2 second startup time
- <200MB memory footprint

## Future Enhancements

Potential improvements:

1. **Application Features**
   - System tray icon with notifications
   - Application menu (File, View, Help)
   - User preferences storage
   - Multiple sector/airport support
   - Custom alert rules

2. **Technical Improvements**
   - Proper logging system
   - Automatic update mechanism
   - Crash reporting
   - Pre-packaged offline map tiles
   - Code splitting for faster loading

3. **Integration**
   - WebSocket real-time data feed
   - ASTERIX data parser integration
   - Multi-user support
   - Cloud synchronization

## Development Tips

1. **Use DevTools**: `npm run dev` opens Chrome DevTools for debugging
2. **Check Both Logs**: Watch both Electron console and Flask terminal output
3. **Port Conflicts**: Make sure port 5001 is not in use
4. **Hot Reload**: Currently requires app restart after changes
5. **Test Before Building**: Always run `npm start` before building distributables
6. **Clean Builds**: Use `rm -rf dist node_modules && npm install` if builds act weird

## Contributing

(For internal capstone team)

When making changes:
1. Test locally with `npm run dev`
2. Verify Flask backend still works standalone
3. Check both web and desktop versions
4. Update this README if adding features
5. Test build process before committing
6. Document any new dependencies

## Support & Resources

### Documentation
- Original planning: [README.md](README.md)
- Electron setup: [ELECTRON_README.md](ELECTRON_README.md)
- This combined guide: [README_COMBINED.md](README_COMBINED.md)

### External Resources
- [Electron Documentation](https://www.electronjs.org/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Leaflet.js Documentation](https://leafletjs.com/)
- [RHEL Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/)

### Known Issues
- Hot-reload not implemented (requires app restart)
- Mock data only (not connected to real ASTERIX backend)
- No authentication/security yet
- Limited to single user/session

---

**Project**: FAA Air Traffic Control System (Capstone)
**Author**: Andrew Moore
**Last Updated**: October 12, 2025
**Version**: 1.0.0
**Electron Version**: 28.0.0
**Python Version**: 3.13
**Target Platform**: Red Hat Enterprise Linux
