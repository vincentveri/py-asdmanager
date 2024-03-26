/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./flaskr/templates/**/*.html",
    "./flaskr/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")    
  ],
}