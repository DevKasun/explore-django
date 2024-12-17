/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    "@tailwindcss/typography",
    "@tailwindcss/forms",
  ],
}

