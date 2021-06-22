// Input: [array]
// Output: [array]
// Constraints:
// does not mutate the array argument
// Edge cases:
// the input array is empty

var randomIndex = (min, max) => {
  return Math.ceil(Math.random() * ((max - 1) - min))
};

var shuffleArray = (arr) => {
  var shuffled = arr.slice();

  for (var i = 0; i < shuffled.length; i++) {
    var thisElem = shuffled[i];

    var swapIndex = randomIndex(0, shuffled.length);
    var swapElem = shuffled[swapIndex];

    shuffled[i] = swapElem;
    shuffled[swapIndex] = thisElem;
  }

  return shuffled;
};

// TESTS
var nums = [1, 2, 3, 4, 5, 6];

var result1 = shuffleArray(nums);
console.log(result1);
// => [3, 5, 6, 4, 1, 2]

var result2 = shuffleArray([]);
console.log(result2);
// => []

var indexResult1 = randomIndex(1, 7);
console.log(indexResult1);
// => n >= 1, n < 7

var indexResult2 = randomIndex(3, 13);
console.log(indexResult2)
// => n >= 3, n < 13
