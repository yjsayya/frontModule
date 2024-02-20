

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