#!/usr/bin/env node

function later(delay) {
  return new Promise(function (resolve, reject) {
    setTimeout(() => resolve(10), delay);
  });
}

const pr = new Promise(function (resolve, reject) {
  setTimeout(() => resolve(10), 5000);
  reject("Error Promise");
});

pr.catch((err) => console.log("Detectado " + err));

// console.log(await pr);
// let x = await later(3000);
// console.log(x);
// async function asyncFn() {
//   return 10;
// }
//
//
// let y = asyncFn();
// console.log(y instanceof Promise);
// y.then((value => console.log(value)));

//
//
// console.log("starting...");
// let x = later(5000)
//   .then(() => console.log("callback 1"))
//   .then(() => console.log("callback 2"));
// console.log("ending...");
// x.then(() => console.log("callback 3"));
// console.log("awaiting...");
// await x;
// x.then(() => console.log("callback 4"));
