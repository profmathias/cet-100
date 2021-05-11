function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

async function somaLenta(a, b) {
  await esperar(5000);
  return a + b;
}

async function variasOperacoes() {
  let x = await somaLenta(10, 20);
  let y = await somaLenta(5, 5);
  let z = await somaLenta(1, 1);

  return x + y + z;
}

let resultado = await variasOperacoes();
console.log(resultado);
console.log("Aguardando a soma...");
