function inverseArray(array) {
  let inverse = [];
  let aLength = array.length - 1;

  for (let x = aLength; x >= 0; x--) {
    inverse.push(array[x]);
  }
  return inverse;
}

//Example

let myArray = ["one", "two", "three"];
console.log(inverseArray(myArray));
