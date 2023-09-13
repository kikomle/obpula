/** @type {import('tailwindcss').Config} */
const plugin = require('tailwindcss/plugin')

module.exports = {
  content: [
      "./templates/**/*.html",
      "./static/src/**/*.js",
      "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    plugin(function({ addComponents }) {
      addComponents({
        '.button_incorrect': {
          backgroundColor: '#ff0000',
          color: '#ffffff',
          padding: '.5rem 1rem',
          borderRadius: '.25rem',
          '&:hover': {
            backgroundColor: '#ff0000',
            color: '#ffffff',
          },
        },
        '.button_correct': {
          backgroundColor: '#00ff00',
          color: '#ffffff',
          padding: '.5rem 1rem',
          borderRadius: '.25rem',
          '&:hover': {
            backgroundColor: '#00ff00',
            color: '#ffffff',
          },
        },
    })
  })

  ],      
}