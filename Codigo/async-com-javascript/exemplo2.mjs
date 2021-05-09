#!/usr/bin/env node

"use strict";

import fs from "fs";

fs.readFile("exemplo.in", "utf-8", (err, conteudo) => {
  console.log(conteudo);
})
console.log("Arquivo Lido!")
