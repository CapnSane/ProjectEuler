// Problem 2

// Each new term in the Fibonacci sequence is
// generated by adding the previous two terms.
// By starting with 1 and 2, the first 10 terms will be:

// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

// By considering the terms in the Fibonacci sequence
// whose values do not exceed four million,
// find the sum of the even-valued terms.

const lim = 4000000;
const seq = [1, 2];

function fibo(lim, seq) {
  let i = 1;
  while (seq[i] < lim) {
    if (seq[i - 1] > lim - seq[i]) {
      break;
    } else {
      seq.push(seq[i - 1] + seq[i]);
      i++;
    }
  }

  let sum = 0;
  for (let i = 0; i < seq.length; i++) {
    if (seq[i] % 2 === 0) {
      sum = sum + seq[i];
    }
  }
  return sum;
}

console.log('The sum of the even-valued terms is:', fibo(lim, seq));
