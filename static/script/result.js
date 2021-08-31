import {init, share, copy} from './base/share.js';

init();

var result = document.getElementById("result").innerText;
var title = document.getElementById("title").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"");
var value = `${title}의 약속 가능 시간이에요!\n${result}`;
var kakao = value;

if(kakao.length > 200) kakao = kakao.substr(0, 197) + "..."

document.getElementById("share_btn").addEventListener('click', function() { share(kakao, window.location.href); });
document.getElementById("copy_btn").addEventListener('click', function() { copy(value); });