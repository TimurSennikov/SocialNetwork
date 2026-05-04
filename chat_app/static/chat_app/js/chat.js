const url = `ws://${window.location.host}/chat/`
const chatSocket = new WebSocket(url)

chatSocket.onmessage = function(event){
    const data = JSON.parse(event.data)
    console.log(data.type)
    if (data.type == 'chat'){
        console.log(2)
        const text = document.createElement('h4')
        text.innerHTML = data.message
        document.querySelector('body').append(text)
    }
}

const form = document.querySelector("form")
const input = form.querySelector("input")
form.addEventListener("submit", (event) =>{ 
    event.preventDefault()
    chatSocket.send(JSON.stringify({
        message: input.value
    }))
    input.value = ""
})