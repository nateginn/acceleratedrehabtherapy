(function ($) {
    $(document).ready(function () {
            if (document.querySelector('.map-block__slider') != null) {
                var mapSlider = new Swiper('.map-block__slider', {
                    spaceBetween: 150,
                    autoHeight: true,
                    touchRatio: 0,
                    pagination: {
                        el: '.map-block__pagination',
                        type: 'fraction',
                    },
                    navigation: {
                        nextEl: '.map-block__next',
                        prevEl: '.map-block__prev',
                    },
                    breakpoints: {
                        1100: {
                            spaceBetween: 100,
                        },

                        1023: {
                            spaceBetween: 63,
                        },

                        850: {
                            spaceBetween: 20,
                        },

                        767: {
                            spaceBetween: 50,
                            touchRatio: 1,
                            slidesPerView: 2,
                        },

                        549: {
                            slidesPerView: 1,
                            touchRatio: 1,
                        }
                    },
                });
            }

            var gmap,
                media_query = 768;

            // получение точки по jQuery-объекту адреса
            var pointByAddr = function ($address) {
                var addr_data = $address.data();
                return GMapPoint(addr_data.lat, addr_data.lng);
            };
            var markerCenter = function (map, block) {
                // if ($.winWidth() < media_query) {
                //     // map.panBy(0 , -$('.overlay').outerHeight() / 10);
                //     map.panBy(0, 110);
                // } else {
                //     map.panBy(-(block.outerWidth() + block.offset().left) / 4, 0);
                // }
                // if ($.winWidth() < media_query) {
                //     map.panBy(-(block.outerWidth() / 2 , 0 + block.offset().left) / 35, -30);
                // } else {
                map.panBy(-(block.outerWidth() / 2 , 0 + block.offset().left) / 35, -30);
                // }
            };

            // клик на адрес
            $('.address__btn').on('click', function () {
                var $address = $(this).parent(),
                    $balloonText = $address.find('.address__js'),
                    $block = $('#addresses');
                var point = pointByAddr($address);
                var lat = parseFloat($address.data('lat'));
                var lng = parseFloat($address.data('lng'));

                if (point && gmap) {
                    gmap.center(point);

                    // маркер по центру непокрытой области
                    markerCenter(gmap, $block);

                    var marker = gmap.markers[0];
                    if (marker) {
                        marker.position(point);

                        setTimeout(function () {
                            balloonContent = $balloonText.text();
                            gmap.balloon.content(balloonContent);
                            marker.openBalloon();
                        }, 200)
                    }

                    $address.addClass('active').siblings().removeClass('active');
                }

                $(document).ready(function () {
                    if (!isNaN(lat) && !isNaN(lng)) {
                        var $link = $('.js-directionLink');

                        if ($link.length) {
                            var href = 'https://maps.google.com/maps?daddr=' + lat + ',' + lng + '&z=15';

                            $link.attr('href', href);
                        }
                    }
                });
            });

            function initMap() {

                var markerImage = '/static/img/pin.png';

                var pointByAddr = function ($address) {
                    var addr_data = $address.data();
                    return GMapPoint(addr_data.lat, addr_data.lng);
                };
                $(document).ready(function () {

                    function markerPosition() {
                        var marker = this.markers[0];
                        if (marker) {
                            this.center(marker);
                            markerCenter(this, $block);
                        }
                    }

                    var $addresses = $('#addresses').find('.address');
                    if ($addresses.length) {
                        var $first = $addresses.first(),
                            $block = $('#addresses');

                        $('.address:eq(0)').addClass('active');

                        gmap = GMap('#google-map .map', {
                            center: pointByAddr($first),
                            zoom: 17,
                        }).on('ready', function () {

                            this.balloon = GMapBalloon({
                                map: this,
                                autoPan: false
                            });
                            var marker = GMapMarker({
                                position: pointByAddr($first),
                                icon: markerImage
                            }).on('attached', function () {
                                var that = this;
                                setTimeout(function () {
                                    gmap.balloon.content($('.address:eq(0)').find('.address__js').text());
                                    that.openBalloon()
                                }, 1500)
                            });


                            marker.map(this);

                        }).on('resize', markerPosition).on('zoom_changed', markerPosition).on('ready', markerPosition);

                        $(window).blur(function () {
                            $first.find($(".address__btn")).trigger('click');
                        });
                    }


                });
            }

            if (document.querySelector('.map') != null) {
                GMap.ready(initMap);
            }
        }
    );
})(jQuery);