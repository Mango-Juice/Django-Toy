Kakao.init('bef070e8a579dd8fb28ff791fc6a240b');

var result = document.getElementById("result").innerText;
var title = document.getElementById("title").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"");
var value = `${title}의 약속 가능 시간이에요!\n${result}`;
var kakao = value;

if(kakao.length > 200) kakao = kakao.substr(0, 197) + "..."

document.getElementById("share_btn").addEventListener('click', function () {
    Kakao.Link.sendDefault({
      objectType: 'text',
      text: kakao
        ,
      link: {
        mobileWebUrl:
          window.location.href,
        webUrl:
          window.location.href,
      },
    });
});

document.getElementById("copy_btn").addEventListener('click', function () {
    const textArea = document.createElement('textarea');
    document.body.appendChild(textArea);
    textArea.value = value;
    textArea.select();
    textArea.setSelectionRange(0, 99999);
    document.execCommand('copy');
    textArea.setSelectionRange(0, 0);
    document.body.removeChild(textArea);
    alert("클립보드에 복사가 완료되었습니다.")
});