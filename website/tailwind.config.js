module.exports = {
  mode: "jit",
  purge: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        "pants-blue": "#70d1fe",
        "skin-yellow": "#fed90f",
        "stubble-brown": "#d1b271",
        "shoe-black": "#424f46",
        "donut-pink": "#ff66ff",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
