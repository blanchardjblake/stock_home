const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {},
    baseUrl: 'http://127.0.0.1:8000/',
    viewportHeight: 900,
    viewportWidth: 1024,
  },
});
