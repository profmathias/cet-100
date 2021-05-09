const promise = new Promise(function (resolve, reject) {
  const numero = Math.floor((Math.random()*2));
  if(numero === 0) {
    resolve("Ok!");
  }
  else {
    reject("Falha!");
  }
})

promise.then((value) => console.log("Callback 1: Promisse Ok!"))
       .then((value) => console.log("Callback 2: Promisse Ok!"))
       .then((value) => console.log("Callback 3: Promisse Ok!"))
       .catch((motivo) => console.log(motivo));

