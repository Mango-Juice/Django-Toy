const anims = document.querySelectorAll('.anim');

const animation = function() {
  for (const element of anims) {
    if (!element.classList.contains('show')) {
      if (window.innerHeight > element.getBoundingClientRect().top + 100) {
        element.classList.add('show');
          }
        }
      }
    }

window.addEventListener('load', animation);
window.addEventListener('scroll', animation);