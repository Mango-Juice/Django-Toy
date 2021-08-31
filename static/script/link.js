import {init, share, copy} from './base/share.js';

init();

var invite = document.getElementById("share_link").innerText;
var result = document.getElementById("result_link").innerText;

document.getElementById("share_btn").addEventListener('click', function () {
    share('🎉 약속에 초대합니다!\n\n약속 시간을 정할 수 있도록 아래 버튼을 눌러 약속에 참여하지 못하는 시간을 알려주세요!', invite);
});

document.getElementById("copy_btn").addEventListener('click', function() { 
    copy(`🎉 약속에 초대합니다!\n\n약속 시간을 정할 수 있도록 약속에 참여하지 못하는 시간을 등록해주세요!\n\n시간 등록: ${invite}\n실시간 결과: ${result}`); 
});