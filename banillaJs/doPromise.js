let scripts = document.getElementsByTagName('script');
let myScript = scripts[ scripts.length - 1 ];

let queryString = myScript.src.replace(/^[^\?]+\??/,'');

let params = parseQuery(queryString);

function parseQuery ( query ) {
   let Params = new Object ();
   if (!query) 
    return Params; // return empty object
   let Pairs = query.split(/[;&]/);
   for (let i = 0; i < Pairs.length; i++ ) {
      let KeyVal = Pairs[i].split('=');
      if ( ! KeyVal || KeyVal.length != 2 ) {
        continue;
      }
      let key = unescape(KeyVal[0]);
      let val = unescape(KeyVal[1]);
      val = val.replace(/\+/g, ' ');
      Params[key] = val;
   }
   return Params;
}


// 출처: https://iamnotokay.tistory.com/241 [I am not Okay:티스토리]