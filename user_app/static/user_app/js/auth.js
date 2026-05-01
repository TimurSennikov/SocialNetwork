// 
export function getCSRFToken(){
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content')
}

// 
export function showRegisterForm(){
    document.querySelector(".section-register").style.display = 'flex'
    document.querySelector(".section-login").style.display = 'none'
    document.querySelector(".section-confirm").style.display = 'none'
}

function showConfirmForm() {
    document.querySelector(".section-register").style.display = 'none'
    document.querySelector(".section-confirm").style.display = 'flex'
    document.querySelector(".section-login").style.display = 'none'
}

export function showLoginForm(){
    document.querySelector(".section-register").style.display = 'none'
    document.querySelector(".section-login").style.display = 'flex'
    document.querySelector('.section-login nav').lastElementChild.style.cssText = 'border-bottom: 2px solid #543C52'
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

export function renderErrors(containerId, errors){
    let conteinerErrors = document.getElementById(containerId)
    conteinerErrors.innerHTML = ''
    for (let fieldName in errors){
        errors[fieldName].forEach(errorObj => {
            let p = document.createElement('p')
            p.textContent = errorObj.message
            conteinerErrors.appendChild(p)
        })
    }
}
