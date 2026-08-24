#!/usr/bin/env node
/** Regenerate PNG exports from SVG assets (requires @resvg/resvg-js). */
const { Resvg } = require("@resvg/resvg-js");
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const fontPath = path.join(root, "assets/fonts/Fredoka-SemiBold.woff2");

function exportSvg(relativeSvg, relativePng, width, needsFont = false) {
  const svg = fs.readFileSync(path.join(root, relativeSvg), "utf8");
  const options = { fitTo: { mode: "width", value: width } };
  if (needsFont) {
    options.font = {
      loadSystemFonts: true,
      fontFiles: [fontPath],
      defaultFontFamily: "Fredoka",
    };
  }
  const png = new Resvg(svg, options).render().asPng();
  fs.writeFileSync(path.join(root, relativePng), png);
  console.log("Wrote", relativePng);
}

exportSvg("assets/banner.svg", "assets/banner.png", 1280, true);
exportSvg("assets/banner-square.svg", "assets/banner-square.png", 512);
exportSvg("assets/logo.svg", "assets/logo.png", 512);
