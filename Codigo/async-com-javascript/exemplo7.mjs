async function soma(a, b) {
  return a + b;
}

const result = soma(10, 20);
console.log(result instanceof Promise);

result.then((value) => console.log("O resultado é: " + value));

