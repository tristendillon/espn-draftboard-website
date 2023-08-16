module.exports = {
  // conent == purge??
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "team": "#f7f8fa",
        "pick": {
          "text": "#00131F",
          "number": "#fefeff",
          "position": "#384155",
          "arrow": {
            "complete": "#000004",
            "normal": "#b0b2bd"
          },
          "wr": "#46a2cb",
          "rb": "#73c3a6",
          "te": "#cc8d4a",
          "qb": "#c05e85",
          "k": "#9395d0",
          "d/st": "#9a5f4f"

        },
        "primary": "#030617",
        "secondary": "#21283b",
      },
    },
    fontFamily: {
      Roboto: ["Roboto, sans-serif"],
      'poppins': ['Poppins', 'sans-serif'],
      'muli': ['Muli', 'sans-serif']
    },
    container: {
      padding: "2rem",
      center: true,
    },
    screens: {
      sm: "640px",
      md: "768px",
      ld: "880px"
    },
  },
  plugins: [],
};
