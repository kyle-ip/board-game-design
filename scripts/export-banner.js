#!/usr/bin/env node
/** Regenerate banner.png from banner.svg (requires @resvg/resvg-js). */
const { Resvg } = require("@resvg/resvg-js");
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const fontPath = path.join(root, "assets/fonts/Fredoka-SemiBold.woff2");
const svg = fs.readFileSync(path.join(root, "assets/banner.svg"), "utf8");

const resvg = new Resvg(svg, {
  fitTo: { mode: "width", value: 1280 },
  font: {
    loadSystemFonts: true,
    fontFiles: [fontPath],
    defaultFontFamily: "Fredoka",
  },
});

fs.writeFileSync(path.join(root, "assets/banner.png"), resvg.render().asPng());
console.log("Wrote assets/banner.png");
