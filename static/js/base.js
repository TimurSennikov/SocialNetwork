const url = document.querySelectorAll('.page-link');

for (let link of url) {
    if (link.href === window.location.href) {
        link.style.backgroundColor = '#E9E5EE'
        link.style.cursor = 'default'
        link.addEventListener('click', function(event) {
            event.preventDefault();
        });
    };
};