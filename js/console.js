const chars = " .,:;=|iI+hHOE#$-";
let output = "%c";
for (let imag = -1.2; imag <= 1.2; imag += 0.05) {
  for (let real = -2; real <= 1; real += 0.03) {
    let Zr = real;
    let Zi = imag;
    let n = 0;
    for (; n < 16; n++) {
      let Zr2 = Zr * Zr;
      let Zi2 = Zi * Zi;
      if (Zr2 + Zi2 > 4) {
        break;
      }
      Zi = 2 * Zr * Zi + imag;
      Zr = Zr2 - Zi2 + real;
    }
    output += chars.charAt(n);
  }
  output += "\n";
}

output += `\n%c                            By replacing fear of the unknown with curiosity
                             we open ourselves up to an infinite stream of
                             possibility. We can let fear rule our lives or
                            we can become childlike with curiosity, pushing
                           our boundaries, leaping out of our comfort zones,
                                 and accepting what life puts before us.

                                            - Alan Watts\n\n`;
console.log(output, "color: #1b1b1b", "color: #bf3211;");
