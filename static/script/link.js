import {init, share, copy} from './base/share.js';

init();

var invite = document.getElementById("share_link").innerText;
var result = document.getElementById("result_link").innerText;

document.getElementById("share_btn").addEventListener('click', function () {
    share('π μ½μμ μ΄λν©λλ€!\n\nμ½μ μκ°μ μ ν  μ μλλ‘ μλ λ²νΌμ λλ¬ μ½μμ μ°Έμ¬νμ§ λͺ»νλ μκ°μ μλ €μ£ΌμΈμ!', invite);
});

document.getElementById("copy_btn").addEventListener('click', function() { 
    copy(`π μ½μμ μ΄λν©λλ€!\n\nμ½μ μκ°μ μ ν  μ μλλ‘ μ½μμ μ°Έμ¬νμ§ λͺ»νλ μκ°μ λ±λ‘ν΄μ£ΌμΈμ!\n\nμκ° λ±λ‘: ${invite}\nμ€μκ° κ²°κ³Ό: ${result}`); 
});