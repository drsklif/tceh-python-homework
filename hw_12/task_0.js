'use strict';

function random_array_generator(size, values) {
  if(size <= 0) {
    console.log('Incorrect array size!');
    return null;
  }
  if (values == null || values.length <= 0) {
    console.log('Array of possible values is empty!');
    return null;
  }

  var
    arr = [],
    cnt = values.length;

  for (var i = 0; i < size; i++) {
    arr.push(values[Math.floor(Math.random() * cnt)]);
  }

  return arr;
}

var
  array1 = random_array_generator(50, [123, 'abc']),
  array2 = [];

console.log('Random array:');
console.log(array1);

for (var i in array1) {
  array2.push(isNaN(array1[i]) ? 8 : array1[i]);
}

console.log('\nModified array:');
console.log(array2);
