    // Инициализация Quill.js редактора с плейсхолдером
    var quill = new Quill('#editor', {
        theme: 'snow',
        modules: {
            toolbar: '#toolbar' // Привязка панели инструментов
        },
        placeholder: 'Текст заметки' // Установка плейсхолдера
    });

    // Синхронизация содержимого редактора с текстовой областью
    var form = document.querySelector('form');
    form.onsubmit = function() {
        var content = document.querySelector('#content');
        content.value = quill.root.innerHTML; // Получить HTML содержимое
    };

    // Обработчик, чтобы меню всегда появлялись сверху
    document.addEventListener('DOMContentLoaded', function () {
        // Находим все выпадающие меню Quill
        const pickers = document.querySelectorAll('.ql-picker');

        pickers.forEach(picker => {
            // Следим за открытием выпадающего меню
            picker.addEventListener('click', function() {
                const options = picker.querySelector('.ql-picker-options');

                if (options) {
                    // Всегда позиционируем меню сверху
                    options.style.top = 'auto';
                    options.style.bottom = '100%'; // Позиционируем меню сверху
                    options.style.left = '0'; // Выравнивание по левому краю
                }
            });
        });
    });

    