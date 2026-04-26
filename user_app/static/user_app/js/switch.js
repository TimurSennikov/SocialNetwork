function setupButtons() {
    let register = document.querySelectorAll(".register");
    let login = document.querySelectorAll(".login");

    let register_form = document.querySelector(".section-register");
    let login_form = document.querySelector(".section-register");

    for(let reg of register) {
        reg.addEventListener("click", () => {
            register_form.style.display = "block";
            login_form.style.display = "none";

            console.log("1");
        });
    }

    for(let log of login) {
        log.addEventListener("click", () => {
            register_form.style.display = "none";
            login_form.style.display = "block";

            console.log("2");
        });
    }
}

document.addEventListener("DOMContentLoaded", () => {setupButtons();});