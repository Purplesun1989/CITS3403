// data_entry.js for script

function showForm(formId) {

    const allForms = document.querySelectorAll('.review-form');
    allForms.forEach(form => form.style.display = 'none');
  
    const formToShow = document.getElementById(formId);
    formToShow.style.display = 'block';
  }