#!/usr/bin/env node

'use strict';

import express from 'express';


const app = express();
app.use(express.json());
let bancoDeDados = [];


app.get('/usuarios', (req, resp) => {
  resp.send(bancoDeDados);
});

app.post('/usuarios', (req, resp) => {
  bancoDeDados.push(req.body.username);
  resp.sendStatus(201);
})

const server = app.listen(3000, '0.0.0.0', () => {
  console.log("Aplicação Iniciada com Sucesso!")
})

