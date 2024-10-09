import IMask from "imask";

function phoneMask(){
    const element = document.querySelectorAll('[data-input-phone]');
    for(let i = 0; i < element.length; i++) {
        const maskOptions = {
            mask: '+{7}(000)000-00-00'
        };
        const mask = IMask(element[i], maskOptions);
    }
}

export default phoneMask;