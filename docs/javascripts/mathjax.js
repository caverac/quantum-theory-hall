window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    macros: {
      // Custom quantum mechanics macros
      bra: ["\\langle #1 |", 1],
      ket: ["| #1 \\rangle", 1],
      braket: ["\\langle #1 | #2 \\rangle", 2],
      expval: ["\\langle #1 \\rangle", 1],
    },
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  MathJax.typesetPromise();
});
