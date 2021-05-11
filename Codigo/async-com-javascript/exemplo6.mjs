function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

esperar(5000).then(() => {console.log("Espera Encerrada!"); return esperar(5000)})
  .then(() => console.log("Segundo then!"));
console.log("Aguardando Promise ser resolvida!")
