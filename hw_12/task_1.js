'use strict';

function generate_random_array(size, max_value) {
  if(size <= 0) {
    console.log('Incorrect array size!');
    return null;
  }
  if(max_value <= 0) {
    console.log('max_value must be positive!');
    return null;
  }

  var arr = [];
  for (var i = 0; i < size; i++) {
    arr.push(Math.floor(Math.random() * max_value));
  }
  return arr;
}

function sort(arr) {
  console.log('Original array: ' + arr);
  var arr_sorted = arr.slice().sort(function(a, b) { return a - b; });
  console.log('Sorted array: ' + arr_sorted);

  var cnt = 0;
  for (var i = 0; i < arr.length; i++) {
    if(arr[i] != arr_sorted[i]) cnt++;
  }
  return cnt;
}

var
  arr = generate_random_array(10, 32),
  cnt = sort(arr);

console.log('Changed order items count: ' + cnt);
