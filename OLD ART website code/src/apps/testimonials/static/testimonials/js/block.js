(function ($) {

    $(document).ready(function () {
        window.addEventListener('load', function () {
            var $review = $('.testimonials');
            var testimonials = new Swiper('.testimonials__slider', {
                slidesPerView: 2,
                spaceBetween: 18,
                autoHeight:true,

                pagination: {
                    el: '.testimonials__pagination',
                    type: 'fraction',
                },
                navigation: {
                    nextEl: '.testimonials__next',
                    prevEl: '.testimonials__prev',
                },

                breakpoints:{
                    767:{
                       slidesPerView: 1,
                    }
                }
            });

            function rating(wrap, block) {
                if ($(wrap).find(block).length) {

                    var rat = $(wrap).find(block);
                    for (var i = 0; i < rat.length; i++) {
                        var num = rat.eq(i).find('.rating').attr('data-star');
                        var rest = 5 - num;
                        for (var j = 0; j < num; j++) {
                            rat.eq(i).find('.rating').append('<div class="star-active"></div>');
                        }
                        for (var k = 0; k < rest; k++) {
                            rat.eq(i).find('.rating').append('<div class="star-off"></div>');
                        }
                    }
                }
            }

            rating('.testimonials__slider', '.testimonials__slide');

            $review.find('.testimonials__text-wrapper').expander({
                before_expand: function (event, data) {
                    var $button = data.button;
                    timer = setInterval(function () {
                        $button.find('.btn-more').text(gettext('Show less'));
                        testimonials.updateAutoHeight(0);
                    }, 20);
                },
                after_expand: function () {
                    clearInterval(timer);
                },
                before_reduce: function (event, data) {
                    var $button = data.button;
                    timer = setInterval(function () {
                        $button.find('.btn-more').text(gettext('Read more'));
                        testimonials.updateAutoHeight(0);
                    }, 20);
                },
                after_reduce: function () {
                    clearInterval(timer);
                }
            });
        });
    });

})(jQuery);

