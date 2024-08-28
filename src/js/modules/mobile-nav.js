function mobileNav() {
    const menuBtn = document.querySelector('.header__menu-btn');
    const navbar = document.querySelector('.navbar');
    const menuLinks = document.querySelectorAll('.navbar__menu-link');
    const body = document.body;
    function toggleMenu() {
        navbar.classList.toggle('navbar--open');
        body.classList.toggle('no-scroll');
    }
    menuBtn.addEventListener('click', function() {
        toggleMenu();
    });
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (navbar.classList.contains('navbar--open')) {
                toggleMenu();
            }
        });
    });
}
export default mobileNav;