(function ($) {
    'use strict';

    /*
        Требует:
            jquery.fitvids.js, slider.js
    */


    /*
        Вырезает дочерние текстовые DOM-узлы из элемента.
     */
    var cut_description = function (element) {
        var i = 0;
        var child;
        var description = '';
        var childs = element.childNodes;
        while (child = childs[i]) {
            if (child.nodeType === 3) {
                description += child.data;
                element.removeChild(child);
            } else if (child.tagName === 'BR') {
                if (description) {
                    // пропускаем первые BR
                    description += child.outerHTML;
                }
                element.removeChild(child);
            } else if (child.tagName === 'SPAN') {
                var text = cut_description(child);
                if (text) {
                    description += text;
                }
                element.removeChild(child);
            } else {
                i++
            }
        }

        return $.trim(description).replace(/[\n\r]+/g, '<br>');
    };

    /*
        Получение текста из base64 в data-аттрибуте
     */
    var decode_description = function ($element) {
        var description = $element.data('description') || '';
        if (!description) {
            return '';
        }

        description = decodeURIComponent(atob(description));
        return $.trim(description).replace(/[\n\r]+/g, '<br>');
    };


    /*
        Обработка текстовых блоков
     */
    window.prepareTextBlocks = function ($blocks) {
        $blocks.each(function () {
            var $text_block = $(this);

            // оборачивание таблиц
            $text_block.find('table').each(function () {
                $(this).wrap(
                    $('<div>').addClass('page-table')
                )
            });

            // описание к одиночной картинке, добавленной через перетаскивание
            $text_block.find('.simple-photo').each(function () {
                var $image = $(this);
                var $block = $image.parent();
                var description = cut_description($block.get(0)) || decode_description($image);
                if (!description) return;

                $block.append(
                    $('<span>').addClass('object-description').html(description)
                );
            });

            // описание к одиночной картинке, добавленной через загрузчик
            $text_block.find('.single-image').each(function () {
                var $block = $(this);
                var $image = $block.find('img').first();
                var description = cut_description($block.get(0)) || decode_description($image);
                if (!description) return;

                $block.replaceWith(
                    $('<figure>').addClass($block.attr('class')).append(
                        $image,
                        $('<figcaption>').addClass('object-description').html(description)
                    )
                );
            });

            // описание к видео
            $text_block.find('.page-video').each(function () {
                var description = cut_description(this);
                if (!description) return;

                $(this).append(
                    $('<span>').addClass('object-description').html(description)
                )
            }).fitVids();

// Слайдеры с описанием
            $text_block.find('.page-images.multi-image').each(function () {
                var $block = $(this);

                var $swiper_container_wrapper = $('<div>').addClass('swiper-container-wrapper');
                var $swiper_container = $('<div>').addClass('swiper-container');
                var $swiper_wrapper = $('<div>').addClass('swiper-wrapper');
                var $swiper_ui = $('<div>').addClass('swiper-ui');
                var $swiper_slides = $block.find('img').map(function () {
                    var $image = $(this);
                    var $slide = $('<div>').addClass('swiper-slide');
                    var description = decode_description($image);
                    $slide.append($image);
                    if (description) {
                        $slide.append($('<div>').addClass('item-description').html(description));
                    }
                    return $slide.get(0);
                });
                var $swiper_pagination = $('<div>').addClass('swiper-pagination');

                $swiper_container.append(
                    $swiper_wrapper.append($swiper_slides)
                );

                $swiper_container_wrapper.append(
                    $swiper_container,
                    $swiper_pagination,
                    $('<div>').addClass('swiper-button-next'),
                    $('<div>').addClass('swiper-button-prev')
                );

                $block.empty().append(
                    $swiper_container_wrapper
                );

                var swiper = new Swiper($swiper_container, {
                    threshold: 10,
                    autoHeight: true,
                    slidesPerView: 'auto',

                    pagination: {
                        el: $swiper_pagination,
                        clickable: true,
                    },
                    navigation: {
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev',
                    }
                });
                $block.on('click', '.swiper-slide', function () {
                    swiper.slideNext();
                });
            });
        });
    };

    $(document).ready(function () {
        prepareTextBlocks($('.text-styles'));
    });

})(jQuery);
