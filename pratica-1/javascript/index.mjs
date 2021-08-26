import express from 'express';


const app = express()

app.get('/hello', (req, res) => {
  if(req.query.name) {
    res.send(`Hello ${req.query.name}!`)
  }
  else {
    res.send('Hello World!')
  }
});

app.get('/clientes', (req, res) => {
  res.send(['Mathias', 'José', 'Thiago'])
});

app.post('/', (req, res) => {
  res.send('Hello Post!')
});

app.listen(process.env.PORT | 8000, () => {
  console.log('App Started...');
})
