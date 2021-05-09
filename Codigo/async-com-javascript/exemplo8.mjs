function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

async function somaLenta(a, b) {
  await esperar(5000);
  return a + b;
}

somaLenta(10, 20).then((value) => console.log(value));
console.log("Aguardando a soma...");
