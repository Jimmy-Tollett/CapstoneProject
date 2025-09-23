/**
 * Playwright Configuration for Air Traffic Control Map UI E2E Tests
 * 
 * Configures Playwright for testing the web-based map interface
 * including browser settings, test discovery, and reporting
 */

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  // Test directory
  testDir: './tests/e2e_ui',
  
  // Test file patterns
  testMatch: '**/*.spec.ts',
  
  // Run tests in files in parallel
  fullyParallel: true,
  
  // Fail the build on CI if you accidentally left test.only in the source code
  forbidOnly: !!process.env.CI,
  
  // Retry on CI only
  retries: process.env.CI ? 2 : 0,
  
  // Opt out of parallel tests on CI
  workers: process.env.CI ? 1 : undefined,
  
  // Reporter configuration
  reporter: [
    ['html', { open: 'never', outputFolder: 'test-results/playwright-report' }],
    ['junit', { outputFile: 'test-results/junit-report.xml' }],
    ['list']
  ],
  
  // Global test timeout
  timeout: 30 * 1000, // 30 seconds
  
  // Global expect timeout
  expect: {
    timeout: 5 * 1000 // 5 seconds
  },
  
  // Shared settings for all projects
  use: {
    // Base URL for the application under test
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    
    // Browser context options
    viewport: { width: 1280, height: 720 },
    
    // Collect trace on retry
    trace: 'on-first-retry',
    
    // Record video on failure
    video: 'retain-on-failure',
    
    // Take screenshot on failure
    screenshot: 'only-on-failure',
    
    // Browser navigation timeout
    navigationTimeout: 15 * 1000,
    
    // Action timeout
    actionTimeout: 10 * 1000,
    
    // Ignore HTTPS errors for development
    ignoreHTTPSErrors: true,
    
    // Accept downloads
    acceptDownloads: false,
    
    // Color scheme preference
    colorScheme: 'light',
    
    // Locale for testing
    locale: 'en-US',
    
    // Timezone
    timezoneId: 'UTC'
  },

  // Configure projects for major browsers
  projects: [
    {
      name: 'chromium',
      use: { 
        ...devices['Desktop Chrome'],
        // Additional Chrome-specific settings
        launchOptions: {
          args: [
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--disable-features=VizDisplayCompositor'
          ]
        }
      },
    },

    {
      name: 'firefox',
      use: { 
        ...devices['Desktop Firefox'],
        // Firefox-specific settings
        launchOptions: {
          firefoxUserPrefs: {
            'security.tls.insecure_fallback_hosts': 'localhost'
          }
        }
      },
    },

    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },

    // Mobile testing
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },

    // Tablet testing
    {
      name: 'iPad',
      use: { ...devices['iPad Pro'] },
    }
  ],

  // Global setup and teardown
  globalSetup: require.resolve('./global-setup'),
  globalTeardown: require.resolve('./global-teardown'),

  // Web server configuration for local testing
  webServer: {
    command: 'npm run dev', // Command to start the development server
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120 * 1000, // 2 minutes
    
    // Environment variables for the web server
    env: {
      NODE_ENV: 'test',
      API_BASE_URL: 'http://localhost:8000',
      WEBSOCKET_URL: 'ws://localhost:8000/ws'
    }
  },

  // Test output directory
  outputDir: 'test-results/playwright-artifacts',

  // Test metadata
  metadata: {
    'test-type': 'e2e-ui',
    'application': 'air-traffic-control-map',
    'environment': process.env.NODE_ENV || 'test'
  }
});