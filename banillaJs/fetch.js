// DOMContentLoaded 이벤트에 함수 할당
document.addEventListener("DOMContentLoaded", function() {
    getPostLists(1,10); // 페이지 로드 후 실행될 함수 호출
});

function getPostLists(currentPage,pageSize) {
  const url = 'http://localhost:8080';
  fetch(url)
      .then(response => {
          return response.json();
      })
      .then(data => {
          console.log(data);
      })
      .catch(error => {
          console.error('오류 발생:', error);
      });
}