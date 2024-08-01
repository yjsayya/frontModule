/** Cookie에 접근하는 방법 */

// 1. 현재 cookie에 접근하기
// cookieName과 같은 쿠키가 없는 경우 undefined 반환
function getCookie(cookieName) {
  let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + cookieName.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


// 2. cookie 설정하기
function setCookie(name, value, options = {}) {
  options = {
      path: '/',
      ...options
  };
  if (options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
  for (let optionKey in options) {
      updatedCookie += "; " + optionKey;
      let optionValue = options[optionKey];
      if (optionValue !== true) {
          updatedCookie += "=" + optionValue;
      }
  }

  document.cookie = updatedCookie;
}

// 쿠키 삭제하기
// -- 쿠키 만료일을 과거로 설정해버리면 됨
function deleteCookie(cookieName) {
  setCookie(cookieName, "", {'max-age': -1});
}

// 예시

// 사용 예시
setCookie('username', 'JohnDoe', { expires: new Date(2024, 11, 31) });
let username = getCookie('username');
console.log(username);  // 'JohnDoe' 출력