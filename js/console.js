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

output +=
  "\n%cScience is not only compatible with spirituality; it is a profound source of spirituality.\n\n%c- Carl Sagan";
console.log(
  output,
  "display:block;text-align:center;color:#1b1b1b",
  "display:block;margin:0 auto;width:300px;text-align:center;color:#bf3211;",
  "display:block;margin:0 auto;width:300px;text-align:right;color:#1b1b1b;"
);
