

/** 건별 등록 버튼 핸들러 */
document.getElementById('manualRegBtn')
  .addEventListener('click', () => {
    let manualRegNameInput = document.getElementById('manualRegNameInput');
    let name = manualRegNameInput.value;

    let manualRegEmailInput = document.getElementById('manualRegEmailInput');    
    let emailAddr = manualRegEmailInput.value;

    // 유효성 검사 1 -  
    if (emailAddr == '' || emailAddr == null) {
      alert('건별 등록을 할 경우 이메일 주소는 필수 입력값입니다.');
      return;
    }
    // 유효성 검사 2 - 이메일 형식 검사
    const emailRegExp = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
    if (!emailRegExp.test(emailAddr)) {
      alert('이메일 형식이 올바르지 않습니다.');
      return;
    }
    // 중복 검사

    let recipientsList = document.getElementById('recipList');
    recipientsList.innerHTML = `<div class="recipent-info-bundle flex_row_spcBtwn_cen">
                                    <div class="recipent-info ">
                                      <input id=recipInfo class="recipent-info" type="checkbox" checked />
                                      <label for="recipInfo">${name} : ${emailAddr}</label>
                                    </div>
                                    <button class=recipent-info-deleteBtn>삭제</button>
                                </div>`
    // 다시 초기화
    manualRegNameInput.value = '';
    manualRegEmailInput.value = '';

    manualRegNameInput.focus();
  }
)