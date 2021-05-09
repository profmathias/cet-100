const promise = new Promise(function (resolve, reject) {
  const numero = Math.floor((Math.random()*2));
  if(numero === 0) {
    resolve("Ok!");
  }
  else {
    reject("Falha!");
  }
});

promise.then((value) => console.log("Callback 1: Promisse Ok! " + value),
              (erro) => {console.log("Error Callback 1 - " + erro); console.log("Erro capturado no then 1");})
       .then((value) => console.log("Callback 2: Promisse Ok! " + value),
             (erro) => console.log("Error Callback 2 - " + erro))
       .then((value) => console.log("Callback 3: Promisse Ok! " + value),
             (erro) => console.log("Error Callback 3 - " + erro))
       .catch((erro) => console.log("Error Callback 4 - " + erro));
