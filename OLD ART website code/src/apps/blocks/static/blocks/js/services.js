(function ($) {

    $(document).ready(function () {

        // if ($(this).width() < 768) {
        //     $('.service-block__sub-service').hide();
        //     $('.service-block__item').find('.service-block__item-title').click(function (event) {
        //         event.preventDefault();
        //         $(this).siblings('.service-block__sub-service').slideToggle(300);
        //
        //         $(this).toggleClass('arr-menu-mobile');
        //     });
        // // }
        // $(window).resize(function () {
        //     if ($(this).width() < 768) {
        //         if ($('.hui') != undefined) {
        //             $('.service-block__sub-service').addClass('hui');
        //         }
        //     }
        // });


        // function hui(){
        //     $('.service-block__item').find('.service-block__item-title').click(function (event) {
        //         event.preventDefault();
        //
        //         $(this).toggleClass('arr-serv-mobile');
        //     });
        // }

        function setup_for_width_service(mqlserv) {
            if (mqlserv.matches) {

                if ($(window).width() < 768 && $('.service-block__item').hasClass('service-block__item-js') != undefined) {
                    $('.service-block__item').addClass('service-block__item-js');
                }

                $('.service-block__item-title').on('click', function (e) {
                    if ($(window).width() < 768) {
                        e.preventDefault();

                        $(this).toggleClass('arr-menu-mobile');
                        $(this).siblings('.service-block__sub-service').toggleClass('hidden-show');
                    }
                });

            } else {
                if ($(window).width() > 767 && $('.service-block__item').hasClass('service-block__item-js')) {
                    $('.service-block__item').removeClass('service-block__item-js');
                }
            }
        }

        var mqlserv = window.matchMedia("screen and (max-width: 768px)");

        mqlserv.addListener(setup_for_width_service);

        setup_for_width_service(mqlserv);
    });

//меняем картинку
    var itemChangeImg = $('.service-block__item');
    var imgServ = $('.service-block__image');

    function hovItem() {
        itemChangeImg.bind('mouseenter mouseleave');
        itemChangeImg.hover(function () {
            if (+($(this).attr('data-id')) === 10) {
                imgServ.attr('src', '/static/img/Chiropractic.png');
                imgServ.css('left', 'initial');
                imgServ.css('margin-top', 'initial');
            } else if (+($(this).attr('data-id')) === 11) {
                imgServ.attr('src', '/static/img/massage.png');
            } else if (+($(this).attr('data-id')) === 16) {
                imgServ.attr('src', '/static/img/therapy.png');
            } else if (+($(this).attr('data-id')) === 26) {
                imgServ.attr('src', '/static/img/acupuncture.png');
            }

        }, function () {
            imgServ.attr('src', '/static/img/Chiropractic.png');
            imgServ.css('left', 'initial');
            imgServ.css('margin-top', 'initial');
        });
    }

    if ($(window).width() >= 1024) {
        hovItem();
    }

    $(window).resize(function () {
        if (window.innerWidth >= 1024) {
            hovItem();
        } else {
            itemChangeImg.unbind('mouseenter mouseleave');
        }
    });

})(jQuery);