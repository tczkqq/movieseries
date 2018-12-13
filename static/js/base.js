document.querySelector(".burger").addEventListener("click", function () {
    var navs = document.querySelectorAll('.item');
    navs.forEach(nav => nav.classList.toggle('.toggle'));
});
