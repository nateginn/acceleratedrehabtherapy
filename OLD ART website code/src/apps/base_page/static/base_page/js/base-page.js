(function ($) {

    $(document).ready(function () {
        if($("#content") !== undefined){
            if($('#content').height() < 504){
                $('.base-header__wrapper').addClass('no-pseudo');
            }
        }

        if (document.querySelector('.main-slider')) {

            var slides = document.querySelectorAll('.main-slider__image');
            var currentSlide = 0;
            var slideInterval = setInterval(nextSlide, 3000);

            function nextSlide() {
                // slides[currentSlide].className = 'main-slider__image';
                // currentSlide = (currentSlide + 1) % slides.length;
                // slides[currentSlide].className = 'main-slider__image isShow';

                slides[currentSlide].classList.remove('isShow');
                currentSlide = (currentSlide + 1) % slides.length;
                slides[currentSlide].classList.add('isShow');
            }
        } else {
            return false;
        }

        ticker();

        function ticker() {
            if ($('#tickerText').length) {

                var text = null;
                var wrap = $('.main-slider__title');
                var template = $('#tickerText');
                var templText = $('.main-slider__ticker', template[0].content);
                var newCoord = {};
                var interval;
                var percentOne;
                var flagText = true;

                wrap.append(templText.clone());

                function anim() {

                    text = $('.main-slider__ticker');

                    percentOne = parseInt(text.width()) * 1 / 100;
                    $('.main-slider__progress-bar span').width(-(parseInt(text.css('left')) / percentOne) + '%');

                    $('.main-slider__ticker').offset(function (i, coord) {
                        newCoord.left = coord.left - 1;
                        return newCoord;
                    });


                    if ((parseInt(text.last().css('left')) + parseInt(text.last().width())) === $(window).width()) {
                        wrap.append(templText.clone());
                        // $('.scene__text:last-child').css('left', (parseInt(text.width() / 2)) + 10%);

                        $('.main-slider__ticker:last-child').css('left', parseInt(text.last().css('left')) + parseInt(text.width()) + 300 + 'px');

                    } else if (parseInt(text.css('left')) === -10 && flagText) {
                        wrap.append(templText.clone());
                        $('.main-slider__ticker:last-child').css('left', parseInt(text.css('left')) + parseInt(text.width()) + 300 + 'px');
                        flagText = false;
                    }

                    if (parseInt(text.css('left')) < -(parseInt(text.width()) + 200)) {
                        text.remove(':first-child');
                    }

                }

                function raf(fn) {
                    requestAnimationFrame(function () {
                        requestAnimationFrame(function () {
                            fn();
                        })
                    })
                }


                function restartAnim() {
                        clearInterval(interval);
                        $('.main-slider__ticker').removeAttr('style');
                        if ($('.main-slider__ticker').length > 1) {
                            $('.main-slider__ticker').not(':eq(0)').remove();
                        }
                        interval = setInterval(anim, 10);
                }


                function setup_for_width(mql) {
                    if (mql.matches) {
                        interval = setInterval(anim, 10);

                        $('body').on('mouseenter', '.main-slider__ticker', function () {
                            clearInterval(interval);
                        });

                        $('body').on('mouseleave', '.main-slider__ticker', function () {
                            interval = setInterval(anim, 10);
                        });

                        $(window).bind('resize', restartAnim);

                    } else {
                        $(window).unbind('resize');
                        clearInterval(interval);
                        $('body').unbind('mouseenter mouseleave');
                        $('.main-slider__ticker').removeAttr('style');
                        if ($('.main-slider__ticker').length > 1) {
                            $('.main-slider__ticker').not(':eq(0)').remove();
                        }
                    }
                }

                var mql = window.matchMedia("screen and (min-width: 768px)");

                mql.addListener(setup_for_width);

                setup_for_width(mql);

            } else {
                return
            }
        }

    });
})(jQuery);