/** Konfiguracja Tailwinda dla skompilowanego CSS-a (preview/static/css/tailwind.css).
 *
 * Aby przegenerować plik:
 *   tailwindcss -c tailwind.config.js -i tailwind.input.css -o static/css/tailwind.css --minify
 *
 * Standalone CLI: https://github.com/tailwindlabs/tailwindcss/releases
 */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./preview/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        sage:       "#4A7C59",
        "sage-dark":"#2F5740",
        leaf:       "#A8C686",
        cream:      "#F6F4EE",
        ink:        "#1F2A24",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
    },
  },
};
