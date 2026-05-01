import {getCSRFToken, showLoginForm, renderErrors} from './auth.js'

document.getElementById('register-form').addEventListener(
    'submit',
    function(event){
        event.preventDefault()
        const form = event.target
        const formData = new FormData(form)

        fetch(form.action, {
            method : 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: formData
        })
        .then(async response => {
            const data = await response.json()
            if (!response.ok){ 
                throw data 
            }
            return data
        })
        .then(data => {
            let conteinerErrors = document.getElementById('register-errors')
            conteinerErrors.innerHTML = ''
            let p = document.createElement('p')
            p.textContent = data.message
            conteinerErrors.appendChild(p)

            setTimeout(() => {
                form.reset()
                showLoginForm()
            }, 2000)

        })
        .catch(data => {
            if (data.errors){
                renderErrors('register-errors', data.errors)
            }
            console.log(data.errors)
        })
    }
)