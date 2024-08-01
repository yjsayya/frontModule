
// Promise 객체 사용방법 
function doPromise(arr) {
   return new Promise((resolve, reject) => {
      let sum = 0;
      for (ele of arr) {
         sum += ele;
      }
      console.log("sum : " + sum);
      if (sum > 15)
         return resolve("success");
      else
         return reject("error");
   });
}

let arr = [1,2,3,4,5,6,7];
doPromise(arr)
   .then((success) => {
      console.log(success);
   })
   .catch((fail) => {
      console.log(fail);
   })
   .finally(() => {
      console.log("finish");
   });


// 출처: https://iamnotokay.tistory.com/241
