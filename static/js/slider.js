$(document).ready(function() {
    $('#carouselOne').owlCarousel({
        items: 1,
        loop:true, //Зацикливаем слайдер
        margin:50, //Отступ от элемента справа в 50px
        nav:false, //Отключение навигации
        autoplay:true, //Автозапуск слайдера
        smartSpeed:1000, //Время движения слайда
        autoplayTimeout:4000, //Время смены слайда
        responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
});
$(document).ready(function() {
    $('#carouselTwo').owlCarousel({
        items: 1,
        loop:true, //Зацикливаем слайдер
        margin:50, //Отступ от элемента справа в 50px
        nav:false, //Отключение навигации
        autoplay:true, //Автозапуск слайдера
        smartSpeed:1000, //Время движения слайда
        autoplayTimeout:4000, //Время смены слайда
        responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
});

$(document).ready(function() {
    $('#carouselThri').owlCarousel({
        items: 1,
        loop:true, //Зацикливаем слайдер
        margin:50, //Отступ от элемента справа в 50px
        nav:false, //Отключение навигации
        autoplay:true, //Автозапуск слайдера
        smartSpeed:1000, //Время движения слайда
        autoplayTimeout:4000, //Время смены слайда
        responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
});