// 
function getCSRFToken(){
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content')
}

// 
function showRegisterForm(){
    document.querySelector(".section-register").style.display = 'flex'
    document.querySelector(".section-login").style.display = 'none'
    document.querySelector(".section-confirm").style.display = 'none'
}

function showConfirmForm() {
    document.querySelector(".section-register").style.display = 'none'
    document.querySelector(".section-confirm").style.display = 'flex'
    document.querySelector(".section-login").style.display = 'none'
}

function showLoginForm(){
    document.querySelector(".section-register").style.display = 'none'
    document.querySelector(".section-login").style.display = 'flex'
    document.querySelector('.section-login nav').lastElementChild.style.cssText = 'border-bottom: 2px solid #543C52'
}

function focusNext(currentInput, nextIndex) {
    const nodes = document.querySelectorAll(`.digits input`);

    if (currentInput.value.length === 1) {
        if (nextIndex < nodes.length) {
            nodes[nextIndex].focus();
        }
    }
    else if (currentInput.value.length === 0) {
        if(nextIndex > 1) {
            nodes[nextIndex - 2].focus();
        }
    }
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

document.getElementById('register_form').addEventListener('submit', (e) => {
    e.preventDefault();

    let sForm = e.target;
    let sFormData = new FormData(sForm);

    fetch(sForm.action, {method: "POST", headers: {
        'X-CSRFToken': getCSRFToken()
        },
        body: sFormData
    }).then(
        (r) => {
            r.json().then((res) => {
                if(res.success) {
                    showConfirmForm();
                }
                else {
                    alert(res);
                }
            });
        }
    ).catch((e) => {
        alert(e);
    });
});

document.getElementById('login_form').addEventListener('submit', (e) => {
    e.preventDefault();

    let sForm = e.target;
    let sFormData = new FormData(sForm);

    fetch(sForm.action, {method: "POST", headers: {
        'X-CSRFToken': getCSRFToken()
        },
        body: sFormData
    }).then(
        (r) => {
            r.json().then((res) => {
                if(res.success) {
                    window.location.href = res.next;
                }
                else {
                    alert(res);
                }
            });
        }
    ).catch((e) => {
        alert("Невозможно войти. Проверьте правильность введенных данных.");
    });
});

document.getElementById('confirm_form').addEventListener('submit', (e) => {
    e.preventDefault();

    let sForm = e.target;
    let sFormData = new FormData(sForm);

    fetch(sForm.action, {method: "POST", headers: {
        'X-CSRFToken': getCSRFToken()
        },
        body: sFormData
    }).then(
        (r) => {
            r.json().then((res) => {
                if(res.success) {
                    alert("Аккаунт активирован!");
                    window.location.href = res.next;
                }
                else {
                    alert(res.errors);
                }
            });
        }
    ).catch((e) => {
        alert(e);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    let inputs = Array.from(document.querySelectorAll(`.digits input`));

    inputs.forEach((input) => {
        input.addEventListener('input', (e) => {
            if(e.target.value.length > 1) {
                e.target.value = e.target.value.slice(0, 1);
            }

            const currentIndex = inputs.indexOf(input);
            focusNext(input, currentIndex + 1);
        });
    });
});