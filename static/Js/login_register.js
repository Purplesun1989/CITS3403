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
   document.addEventListener('DOMContentLoaded', () => {
      const avatarInput = document.getElementById('avatarInput');
      const preview = document.getElementById('avatarPreview');

      avatarInput.addEventListener('change', () => {
        const file = avatarInput.files[0];
        if (file) preview.src = URL.createObjectURL(file);
      });
    });

function switch_box() {
  document.querySelectorAll('.centralbox').forEach(el => {
    el.style.display = 'none';
  });

  document.querySelectorAll('.register-input-box').forEach(el => {
    el.style.display = 'flex';
  });
}

 document.addEventListener('DOMContentLoaded', () => {
  const registerBtn = document.getElementById('register-btn');
  if(registerBtn){
      registerBtn.addEventListener('click',switch_box)
     }
  if (window.loginError && window.loginError !== 'None') {
    alert(window.loginError);
  }
});




