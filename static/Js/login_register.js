

    document.querySelector('body').addEventListener('mousemove', eyeball);

    function eyeball(event) {
      var eyes = document.querySelectorAll('.eye');
      eyes.forEach(function (eye) {
        let x = eye.getBoundingClientRect().left + (eye.clientWidth / 2);
        let y = eye.getBoundingClientRect().top + (eye.clientHeight / 2);
        let radian = Math.atan2(event.pageX - x, event.pageY - y);
        let rot = (radian * (180 / Math.PI) * -1) + 270;
        eye.style.transform = "rotate(" + rot + "deg)";
      });
    }

    const swapBtn = document.getElementById('swapBtn');
    if (swapBtn) {
      swapBtn.addEventListener('click', function () {
        const centralbox = document.querySelector('.centralbox');
        const face = document.querySelector('.face');
        const formBox = document.querySelector('.form-box');

        if (centralbox.firstElementChild === face) {
          centralbox.insertBefore(formBox, face);
        } else {
          centralbox.insertBefore(face, formBox);
        }
      });
    }
