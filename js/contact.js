// 1. regex validation for email

// 1. setup 
const emailInput = document.getElementById('email');
const submitButton = document.getElementById('submit');
const errorElement = document.getElementById('error');

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
  
submitButton.addEventListener('click', (event) => {
    event.preventDefault(); 
    const emailValue = emailInput.value;
  
    if (validateEmail(emailValue)) {
      errorElement.textContent = '';
      // Proceed with form submission or other actions
      console.log('Email is valid');
    } else {
      errorElement.textContent = 'Please enter a valid email address.';
    }
  });




