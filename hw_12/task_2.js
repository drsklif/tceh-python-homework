'use strict';

for (var i = 1; i <= 100; i++) {
  var to_print = '';
  if (i % 3 == 0) {
    to_print += 'Fizz';
  }
  if (i % 5 == 0) {
    to_print += 'Buzz';
  }
  console.log(to_print ? to_print : i);
}
