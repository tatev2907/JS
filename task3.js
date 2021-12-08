const task3 = (arr) => {
  let max = arr[0];
  console.log("max",max)
  let incCount = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= max) {
      incCount = incCount + max - arr[i] + 1;
      max = max + 1;
    } else {
      max = arr[i];
    }
  }
  return incCount;
};
console.log(task3([1,4,2,8,5]))