document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('header');
    header.addEventListener('click', function () {
        alert('Вы нажали на заголовок!');
    });
});
