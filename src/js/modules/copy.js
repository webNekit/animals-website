function copy() {
    document.addEventListener('DOMContentLoaded', () => {
        const copyButton = document.querySelector('[data-control-copy]');
        const textToCopy = document.querySelector('[data-target-copy]');
    
        copyButton.addEventListener('click', () => {
            // Копируем текст в буфер обмена
            navigator.clipboard.writeText(textToCopy.textContent)
                .then(() => {
                    // Добавляем класс для отображения tooltip
                    copyButton.classList.add('is-tooltip');
                    setTimeout(() => {
                        copyButton.classList.remove('is-tooltip');
                    }, 2000);
                })
                .catch(err => {
                    console.error('Ошибка копирования: ', err);
                });
        });
    });    
}

export default copy;