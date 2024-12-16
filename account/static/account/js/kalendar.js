// Обработчик изменений в селекторах года и месяца
document.getElementById('year-selector').addEventListener('change', updateCalendar);
document.getElementById('month-selector').addEventListener('change', updateCalendar);

// Обработчики для стрелок
document.getElementById('prev-month').addEventListener('click', function() {
    changeMonth(-1);  // Переход к предыдущему месяцу
});

document.getElementById('next-month').addEventListener('click', function() {
    changeMonth(1);  // Переход к следующему месяцу
});

function updateCalendar() {
    // Получаем значения выбранных года и месяца
    const year = document.getElementById('year-selector').value;
    const month = document.getElementById('month-selector').value;

    // Формируем новый URL с параметрами года и месяца
    const url = new URL(window.location.href);
    url.searchParams.set('year', year);
    url.searchParams.set('month', month);

    // Перезагружаем страницу с новым URL
    window.location.href = url;
}

function changeMonth(offset) {
    let yearSelector = document.getElementById('year-selector');
    let monthSelector = document.getElementById('month-selector');
    
    let currentYear = parseInt(yearSelector.value);
    let currentMonth = parseInt(monthSelector.value);

    // Вычисляем новый месяц и год
    currentMonth += offset;

    if (currentMonth < 1) {
        currentMonth = 12;
        currentYear -= 1;  // Переход к предыдущему году
    } else if (currentMonth > 12) {
        currentMonth = 1;
        currentYear += 1;  // Переход к следующему году
    }

    // Обновляем значения в селекторах
    yearSelector.value = currentYear;
    monthSelector.value = currentMonth;

    // Обновляем страницу с новыми параметрами
    let newUrl = new URL(window.location.href);
    newUrl.searchParams.set('year', currentYear);
    newUrl.searchParams.set('month', currentMonth);
    window.location.href = newUrl.toString();  // Перезагружаем страницу с новыми параметрами
}
