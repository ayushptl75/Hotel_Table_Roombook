
// Slider auto-play logic
document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('#mainSlider');
    if (carousel) {
        const bsCarousel = new bootstrap.Carousel(carousel, {
            interval: 2600,
            ride: 'carousel'
        });
    }
});
