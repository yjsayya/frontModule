let input = '이윤종	01025234917	ㅁㅈㄷㄹ	ㅁㅈㄷㄹ	ㅁㅈㄷㄹ	ㄴㅇㄹ	ㅇㄴ n 이윤종	01025234917	ㅁㅈㄷㄹ	ㅁㅈㄷㄹ	ㅁㅈㄷㄹ	ㄴㅇㄹ	ㅇ이윤종	01025234917	ㅁㅈㄷㄹ	ㅁㅈㄷㄹ	ㅁㅈㄷㄹ	ㄴㅇㄹ	ㅇㄴ'



function getVarArray(content) {
  let varArray = [];
  let splitArray = content.split('#{');
  delete splitArray[0];

  for(let elem of splitArray){
    if(!elem) continue;
    let variable = elem.substring(0, elem.indexOf('}'));
    varArray.push(variable);
  }

  const set = new Set(varArray);
  return [...set];
}

let str = "테스트 작성 #{이름}#{변수1}#{변수3}"

console.log(getVarArray(str))

li = getVarArray(str)
for (idx in li) {
  console.log(li[idx]);
}


li = [1,2,3,4,5,6,7]

li.splice(1,1);