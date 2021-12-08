function countInstances(string, letter) {
  return string.split(letter).length - 1;
}

function polindrom(str){
  for (var i = 0; i < str.length; i++) {
    if   (countInstances(str,str.charAt(i)) % 2 !== 0)
    {
      return false
    }
  }
  return true
};
console.log('Task 2 rearange to be polindrom')
console.log(polindrom('abbab'))