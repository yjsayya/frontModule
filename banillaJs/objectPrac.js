

/** 
 * => DOM이 모두 로드가 되면 그 때 실행되어야 하는 메서드를 넣어두면 된다!!
 * 
 * 1. [바닐라 js] document.addEventListener("DOMContentLoaded", function() { });
 * 2. [jQuery] $(function() {});
 * 3. [jQuery] $(document).ready() {}
 */ 


let mtSend = {
  init() {
    let this_ = this;
    mtSend.campId = 0;
    mtSend.schdId = 0;
    mtSend.targetList = [];
  },
  helloWorld() {
    console.log("hello world");
  },

  /** [Step 3] */
  
}

let directMapObject = {
  "01011112222" : ['사람이름1','변수내용1-1','변수내용1-2','변수내용1-3','변수내용1-4','변수내용1-5'],
  "01033334444" : ['사람이름2','변수내용2-1','변수내용2-2','변수내용2-3','변수내용2-4','변수내용2-5'],
  "01055556666" : ['사람이름3','변수내용3-1','변수내용3-2','변수내용3-3','변수내용3-4','변수내용3-5'],
  "01077778888" : ['사람이름4','변수내용4-1','변수내용4-2','변수내용4-3','변수내용4-4','변수내용4-5'],
}

// idx 뽑아내기
for (let idx in Object.keys(directMapObject)) {
  console.log(idx);
}
console.log(" ");
// ele 뽑애기
for (let key of Object.keys(directMapObject)) {
  console.log("key : " + key);
}
console.log(" ");
// idx, ele 뽑아내기
for (let [idx,key] of Object.keys(directMapObject).entries()) {
  console.log("idx : " + idx);
  console.log("key : " + key);
  console.log("value : " + directMapObject[key]);
}

// 