let currentSlide = 0;

function moveSlide(direction) {
    const slides = document.querySelectorAll('.carrusel-item');
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    document.querySelector('.carrusel-inner').style.transform = `translateX(-${currentSlide * 100}%)`;
}
