(function ($) {

    $(document).ready(function () {
        var ourMission = new Swiper('.our-mission__slider', {
            pagination: {
                el: '.our-mission__pagination',
                autoHeight: true,
                clickable: true,
            },
        });
    });

})(jQuery);