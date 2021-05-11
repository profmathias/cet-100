function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

async function operacaoLenta(a, b) {
  let resultado = 0;
  console.log("resultado = ", resultado);
  await esperar(2000);
  resultado = a + b;
  console.log("resultado = ", resultado);
  await esperar(2000);
  resultado = resultado * 2;
  console.log("resultado = ", resultado);
  return resultado;
}

operacaoLenta(10, 20).then((value) => console.log(value));
console.log("Aguardando a soma...");
