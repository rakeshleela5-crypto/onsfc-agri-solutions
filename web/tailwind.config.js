/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        sacred: {
          gold: "#D4AF37",
          amber: "#D97706",
          vermilion: "#DC2626",
          saffron: "#EA580C"
        },
        agri: {
          green: "#15803D",
          dark: "#0F291E",
          emerald: "#059669",
          soil: "#78350F",
          paddy: "#FBBF24"
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['Merriweather', 'serif']
      }
    },
  },
  plugins: [],
}
