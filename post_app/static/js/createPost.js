import { getCSRFToken } from "../../../static/js/getCSRFToken.js"

function removeFileFromList(element, list, name) {
    let dt = new DataTransfer();

    let a = Array.from(list).filter((file) => {return file.name !== name});

    if(a.length > 0) {
        a.forEach((file) => dt.items.add(file));
    }

    element.files = dt.files;
}

document.getElementById('show-modal-create').addEventListener(
    'click',
    function (){
        document.querySelector(".modal-create-post").style.display = 'flex';
        document.getElementById('id_content').value = document.getElementById('post-content').value;
    }
)

document.getElementById('id_images').addEventListener('change', (e) => {
    let files = e.target.files

    let imageList = document.getElementById('image_list')

    while (imageList.firstChild) {
        imageList.removeChild(imageList.firstChild)
    }

    Array.from(files).forEach(file => {
        let url = URL.createObjectURL(file)

        let imgCont = document.createElement('div')
        imgCont.classList.add('image-item')

        let removeBtn = document.createElement('img')
        removeBtn.src = '/static/icons/exit.svg'
        removeBtn.alt = 'Remove'
        removeBtn.classList.add('remove-image')

        removeBtn.addEventListener('click', () => {
            removeFileFromList(e.target, files, file.name)
            imgCont.remove()
        });

        let img = document.createElement("img")
        img.src = url

        imgCont.appendChild(img)
        imgCont.appendChild(removeBtn)
        imageList.appendChild(imgCont)
    });
});


document.querySelector('.close-modal').addEventListener(
    'click',
    function (){
        document.querySelector(".modal-create-post").style.display = 'none'
    }
)

document.getElementById('add-link').addEventListener(
    'click',
    function (){
        let linkDiv = document.createElement('div');
        linkDiv.classList.add('link-item');

        let input =  document.createElement('input')
        input.type = 'url'
        input.name = 'links'
        input.placeholder = 'https://www.instagram.com/world.it.academy'

        let remove_input = document.createElement('h3');
        remove_input.textContent = '×';
        remove_input.classList.add('remove-link');
        remove_input.addEventListener('click', () => {
            input.remove();
            remove_input.remove();
        });

        document.getElementById('links-list').insertBefore(linkDiv, document.getElementById('links-list').firstChild);
        linkDiv.appendChild(input)
        linkDiv.appendChild(remove_input)   
    }
)

document.getElementById('post-create-form').addEventListener(
    'submit',
    function (event){
        event.preventDefault()
        const form = event.target
        const formData = new FormData(form)

        fetch(form.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: formData
        })
        .then(async response => {
            const data = await response.json()

            if (!response.ok) {
                throw data
            }
            return data
        })
        .then(data => {
            if (data.redirect_url){
                window.location.href = data.redirect_url
            }
        });
    }
)