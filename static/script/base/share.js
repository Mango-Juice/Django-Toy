function init(){
    Kakao.init('bef070e8a579dd8fb28ff791fc6a240b');
}

function share(text, url){
    Kakao.Link.sendDefault({
      objectType: 'text',
      text: text
        ,
      link: {
        mobileWebUrl: url,
        webUrl: url,
      },
    });
}

function copy(text){
    const textArea = document.createElement('textarea');
    document.body.appendChild(textArea);
    textArea.value = text;
    textArea.select();
    textArea.setSelectionRange(0, 99999);
    document.execCommand('copy');
    textArea.setSelectionRange(0, 0);
    document.body.removeChild(textArea);
    alert("클립보드에 복사가 완료되었습니다.");
}

export {init, share, copy};