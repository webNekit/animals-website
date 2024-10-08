function copy() {
    document.addEventListener('DOMContentLoaded', () => {
        const copyButtons = document.querySelectorAll('[data-control-copy]');
        
        copyButtons.forEach(button => {
            button.addEventListener('click', () => {
                const textToCopy = button.parentElement.querySelector('[data-target-copy]').innerText;

                navigator.clipboard.writeText(textToCopy).then(() => {
                    button.classList.add('is-tooltip', 'active');
                    setTimeout(() => {
                        button.classList.remove('active');
                    }, 2000);
                });
            });
        });
    });
}

export default copy;