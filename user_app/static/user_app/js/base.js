function detectCurrentPage() {
    let links = document.querySelectorAll(".page-link");

    for(let link of links) {
        if(link.href == window.location.href) {
            link.style.background = "rgba(0.5, 0.5, 0.5, 0.5)";
        }
    }
}