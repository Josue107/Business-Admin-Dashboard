console.log("I'm working")

const form = document.getElementById('form');
const firstNameInput = document.getElementById('firstName-input');
const companyEmailInput = document.getElementById('companyEmail-input');
const passwordInput = document.getElementById('password-input');
const confirmPasswordInput = document.getElementById('confirmPassword-input');
const errorMessage = document.getElementById('error-message');
const inputs = [firstNameInput, companyEmailInput, passwordInput, confirmPasswordInput];

form.addEventListener('submit', (event) => {
    if(firstNameInput)
        error = verifySignupInputs(inputs);

    else
        error = verifyLoginInputs(companyEmailInput, passwordInput);

    if(error)
        event.preventDefault();
});

function verifySignupInputs(inputs)
{
    let error = false;
    inputs.forEach(input => {
        if(input.value === '' || input.value == null)
        {
            input.parentElement.classList.add('incorrect');
            error = true;
        }
    });  

    // verifying that password and confirm password matches
    if(passwordInput.value !== confirmPasswordInput.value)
    {
        errorMessage.innerText = 'Password and Confirm password do not match!';
        passwordInput.parentElement.classList.add('incorrect');
        confirmPasswordInput.parentElement.classList.add('incorrect');
        error = true;
    }

    else
    {   
        if(passwordInput.value.length < 8)
        {
            errorMessage.innerText = 'Password must be at least 8 characters long';
            passwordInput.parentElement.classList.add('incorrect');
            confirmPasswordInput.parentElement.classList.add('incorrect');
            error = true;
        }
    }

    return error;
}

inputs.forEach(input => {
    input.addEventListener('input', () => {
        if(input.parentElement.classList.contains('incorrect'))
            input.parentElement.classList.remove('incorrect');
        errorMessage.innerText = '';
    });
});