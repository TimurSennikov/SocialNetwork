function showPopup(e) {
    e.preventDefault();

    document.querySelector(".post-popup").style.display = "flex";
    document.getElementById("post_form_text").value = document.getElementById("post_pre_input");
}

function hidePopup(e) {
    e.preventDefault();

    document.querySelector(".post-popup").style.display = "none";
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("post_create_button").addEventListener("click", showPopup);
    document.getElementById("post_popup_close").addEventListener("click", hidePopup);
});