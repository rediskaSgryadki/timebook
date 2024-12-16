//-------ФИКСАЦИЯ НАВБАРА-------//
// Получаем элемент навбара
const navbar = document.getElementById('navbar');

// Устанавливаем высоту прокрутки, после которой фиксируется navbar (например, 100 пикселей)
const scrollThreshold = 100;

// Функция для отслеживания прокрутки
window.addEventListener('scroll', () => {
    // Получаем текущую позицию прокрутки
    const scrollPosition = window.scrollY || document.documentElement.scrollTop;

    // Если прокрутка больше установленного порога, фиксируем navbar
    if (scrollPosition >= scrollThreshold) {
        navbar.classList.add('fixed-navbar');
    } else {
        navbar.classList.remove('fixed-navbar');
    }
});


