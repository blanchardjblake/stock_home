const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {},
    baseUrl: 'https://fa22-team-d.herokuapp.com/',
    viewportHeight: 900,
    viewportWidth: 1024,
  },
});
