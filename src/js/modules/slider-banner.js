import Swiper from 'swiper/bundle';

function bannerSlider(){
    const swiper = new Swiper('.swiper', {
        loop: true,
        slidesPerView: 1,
        autoplay: {
            delay: 5000,
          },
        navigation: {
          nextEl: '.banner__slider-buttonsTarget--next',
          prevEl: '.banner__slider-buttonsTarget--prev',
        },
      });
}
export default bannerSlider;