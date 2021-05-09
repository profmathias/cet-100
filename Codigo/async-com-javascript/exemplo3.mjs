const promise = new Promise(function (resolve, reject) {
  const numero = Math.floor((Math.random()*2));
  if(numero === 0) {
    resolve("Ok!");
  }
  else {
    reject("Falha!")
  }
})

promise.then((value) => console.log(value))
       .catch((motivo) => console.log(motivo));

console.log("Promise Executando...")
