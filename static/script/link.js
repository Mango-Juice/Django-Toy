Kakao.init('bef070e8a579dd8fb28ff791fc6a240b');

var invite = document.getElementById("share_link").innerText;
var result = document.getElementById("result_link").innerText;

document.getElementById("share_btn").addEventListener('click', function () {
    Kakao.Link.sendDefault({
      objectType: 'text',
      text: '🎉 약속에 초대합니다!\n\n약속 시간을 정할 수 있도록 아래 버튼을 눌러 약속에 참여하지 못하는 시간을 알려주세요!'
        ,
      link: {
        mobileWebUrl:
          invite,
        webUrl:
          invite,
      },
    });
});

document.getElementById("copy_btn").addEventListener('click', function () {
    const textArea = document.createElement('textarea');
    document.body.appendChild(textArea);
    textArea.value = `🎉 약속에 초대합니다!\n\n약속 시간을 정할 수 있도록 약속에 참여하지 못하는 시간을 등록해주세요!\n\n시간 등록: ${invite}\n실시간 결과: ${result}`;
    textArea.select();
    textArea.setSelectionRange(0, 99999);
    document.execCommand('copy');
    textArea.setSelectionRange(0, 0);
    document.body.removeChild(textArea);
    alert("클립보드에 복사가 완료되었습니다.")
});