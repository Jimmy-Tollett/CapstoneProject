/**
 * Preload script for Electron
 * This script runs before the web page loads and can safely expose
 * specific Node.js/Electron APIs to the renderer process
 */

const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electron', {
    // Example: You can add IPC methods here if needed later
    // send: (channel, data) => {
    //     // Whitelist channels
    //     let validChannels = ['toMain'];
    //     if (validChannels.includes(channel)) {
    //         ipcRenderer.send(channel, data);
    //     }
    // },
    // receive: (channel, func) => {
    //     let validChannels = ['fromMain'];
    //     if (validChannels.includes(channel)) {
    //         ipcRenderer.on(channel, (event, ...args) => func(...args));
    //     }
    // },

    // Basic information
    platform: process.platform,
    version: process.versions.electron
});

console.log('Preload script loaded');
