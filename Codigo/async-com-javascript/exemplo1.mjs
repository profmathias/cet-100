#!/usr/bin/env node

"use strict";

import fs from "fs";

const conteudo = fs.readFileSync("exemplo.in", "utf-8");
console.log("Arquivo Lido!");
console.log(conteudo);

