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
      const form = document.getElementById('avatarForm');

      avatarInput.addEventListener('change', () => {
        const file = avatarInput.files[0];
        if (file) preview.src = URL.createObjectURL(file);
      });

      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        try {
          const res = await fetch('/upload_avatar', { method: 'POST', body: formData });
          const data = await res.json();
          if (res.ok) {
            Swal.fire({
              position: 'center',
              icon: 'success',
              title: 'Upload Successful',
              text: 'Your avatar has been updated.',
              timer: 2000,
              showConfirmButton: false
            });
            preview.src = data.url;
          } else throw new Error(data.error || 'Upload failed');
        } catch (err) {
          Swal.fire({ position: 'center', icon: 'error', title: 'Error', text: err.message });
        }
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




