#!/usr/bin/env node

'use strict';

import express from 'express';
import db from './db.mjs';

const app = express();
app.use(express.json());


app.get('/usuarios', (req, resp) => {
  const dados = db.collection("usuarios").find({});
  dados.toArray(
    (err, result) => resp.send(result)
  );
});

app.post('/usuarios', (req, resp) => {
  const collection = db.collection('usuarios');
  collection.insertOne({user: req.body.username})
  resp.sendStatus(201);
})

const server = app.listen(3000, '0.0.0.0', () => {
  console.log("Aplicação Iniciada com Sucesso!")
})

