// 
function getCSRFToken(){
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content')
}

// 
function showRegisterForm(){
    document.querySelector(".section-register").style.display = 'flex'
    document.querySelector(".section-login").style.display = 'none'
}
// 
function showLoginForm(){
    document.querySelector(".section-register").style.display = 'none'
    document.querySelector(".section-login").style.display = 'flex'
}
// 
document.getElementById('register').addEventListener(
    'click',
    function(){
        showRegisterForm()
    }
)
// 
document.getElementById('login').addEventListener(
    'click',
    function(){
        showLoginForm()
    }
)