//-------ФИКСАЦИЯ НАВБАРА-------//
// Получаем элементы
const navbar = document.getElementById('navbar');
const sloganSection = document.querySelector('.container.otst'); // Селектор для раздела "Слоган"

// Функция для отслеживания прокрутки
window.addEventListener('scroll', () => {
    // Получаем положение на странице
    const sloganBottom = sloganSection.getBoundingClientRect().bottom;

    // Если прокручено до конца раздела Слоган, фиксируем navbar
    if (sloganBottom <= 0) {
        navbar.classList.add('fixed-navbar');
    } else {
        navbar.classList.remove('fixed-navbar');
    }
});


//-------ПАРАЛЛАКС НА БЛОКАХ-------//
