// all function calling
let loading = document.querySelector('#page');
showPassword = document.querySelector('#showpwd');
inputPassword = document.querySelector('#pwd');

LoadAllFunction()

function LoadAllFunction(){
    window.addEventListener('load',loads);
    showPassword.addEventListener('click',showMyPassword);
}

// show password
 function showMyPassword(e) {
    if (inputPassword.type === 'password') {
        inputPassword.type = 'text'
    } else {
        inputPassword.type = 'password'
    }
    e.preventDefault();
}

// view loader function
function loads(){
    setTimeout(() =>{
        loading.classList.add('loader')
    },2000)
}
