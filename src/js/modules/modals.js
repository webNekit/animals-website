function modalToggle(){
    const modalToggler = document.querySelectorAll('[data-toggler-modal]');
    const modals = document.querySelectorAll('[data-modal]');
    const overlay = document?.querySelector('[data-overlay]');

    const toggleModal = () => {
        for(let i = 0; i < modals.length; i++) {
            modals[i].classList.toggle('active');
            overlay.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        }
    }

    for(let j = 0; j < modalToggler.length; j++) {
        modalToggler[j].addEventListener('click', toggleModal);
    }
}

export default modalToggle;