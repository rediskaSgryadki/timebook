
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.tooltip-link').forEach(function (element) {
        var tooltip = document.createElement('div');
        tooltip.className = 'tooltip';
        tooltip.textContent = element.getAttribute('data-tooltip');
        element.appendChild(tooltip);

        element.addEventListener('mouseenter', function () {
            tooltip.style.opacity = 1;
            tooltip.style.visibility = 'visible';
        });

        element.addEventListener('mouseleave', function () {
            tooltip.style.opacity = 0;
            tooltip.style.visibility = 'hidden';
        });
    });
});


