(function ($) {
    'use strict';

    /*
        Базовый класс провайдеров соцкнопок.

        Требует:
            jquery.utils.js
     */

    /** @namespace window.screenX */
    /** @namespace window.screenY */
    /** @namespace window.VK.Share.count */
    /** @namespace window.services.gplus.cb */

    var SocialProvider = Class(Object, function SocialProvider(cls, superclass) {
        cls.DATA_KEY = 'social';
        cls.WINDOW_WIDTH = 600;
        cls.WINDOW_HEIGHT = 400;

        cls.init = function (button) {
            this.$button = $(button).first();
            if (!this.$button.length) {
                return false;
            }

            // отвязывание старого экземпляра
            var old_instance = this.$button.data(this.DATA_KEY);
            if (old_instance) {
                old_instance.destroy();
            }

            var that = this;
            this.$button.on('click.social', function () {
                that.popup($(this).attr('href'));
                return false;
            });

            if (!this.$button.parent().hasClass('no-counter')) {
                this.getShareCount();
            } else {
                this.fetchMeta();
            }
        };

        cls.destroy = function () {
            this.$button.off('.social');
            this.$button.removeData(this.DATA_KEY);
        };

        cls.fetchMeta = function () {
            var data = this.$button.data();
            var parent_data = this.$button.parent().data();

            // url
            this.url = data.url || parent_data.url;
            if (!this.url) {
                this.url = $('meta[property="og:url"]').attr('content');
            }
            if (!this.url) {
                this.url = location.href;
            }

            // title
            this.title = data.title || parent_data.title;
            if (!this.title) {
                this.title = $('meta[property="og:title"]').attr('content');
            }
            if (!this.title) {
                this.title = $('title').text();
            }

            // image
            this.image = data.image || parent_data.image;
            if (!this.image) {
                this.image = $('meta[property="og:image"]').attr('content');
            }

            // description
            this.description = data.description || parent_data.description;
            if (!this.description) {
                this.description = $('meta[property="og:description"]').attr('content');
            }
            if (!this.description) {
                this.description = $('meta[name="description"]').text();
            }
        };

        cls.getShareCount = function () {
            this.fetchMeta();
            return '';
        };

        cls._shareCountScript = function (url) {
            var script = document.createElement('script'),
                head = document.head;

            script.type = 'text/javascript';
            script.src = url;

            head.appendChild(script);
            head.removeChild(script);
        };

        cls.shareCountFetched = function (count) {
            if (typeof count !== 'undefined') {
                var $counter = this.$button.find('.counter');
                if ($counter.length) {
                    $counter.text(count)
                } else {
                    this.$button.append(
                        $('<span>').addClass('counter').text(count)
                    );
                }
            }
        };

        cls.popup = function (url, winId, width, height) {
            var browser_left = typeof window.screenX !== 'undefined' ? window.screenX : window.screenLeft,
                browser_top = typeof window.screenY !== 'undefined' ? window.screenY : window.screenTop,
                browser_width = typeof window.outerWidth !== 'undefined' ? window.outerWidth : document.body.clientWidth,
                browser_height = typeof window.outerHeight !== 'undefined' ? window.outerHeight : document.body.clientHeight,
                popup_width = width || this.WINDOW_WIDTH,
                popup_height = height || this.WINDOW_HEIGHT,
                top_position = browser_top + Math.round((browser_height - popup_height) / 2),
                left_position = browser_left + Math.round((browser_width - popup_width) / 2);

            var win = window.open(
                url,
                winId || this.__name__,
                'width=' + popup_width + ', ' +
                'height=' + popup_height + ', ' +
                'top=' + top_position + ', ' +
                'left=' + left_position
            );

            if (!win) {
                return location.href = url;
            }

            win.focus();

            return win;
        }
    });

    /*
        Провайдер Facebook
     */
    window.FacebookProvider = Class(SocialProvider, function FacebookProvider(cls, superclass) {
        cls.getShareCount = function () {
            superclass.getShareCount.call(this);

            var that = this;
            window.social_facebook = function (data) {
                if (data && data.length) {
                    that.shareCountFetched(data[0]['total_count']);
                }
            };

            this._shareCountScript('https://api.facebook.com/method/links.getStats?urls=' + encodeURIComponent(this.url) + '&format=json&callback=social_facebook');
        };
    });

    /*
        Провайдер Twitter
     */
    window.TwitterProvider = Class(SocialProvider, function TwitterProvider(cls, superclass) {
        cls.WINDOW_WIDTH = 600;
        cls.WINDOW_HEIGHT = 300;
    });

    /*
        Провайдер LinkedIn
    */
    window.LinkedInProvider = Class(SocialProvider, function LinkedInProvider(cls, superclass) {
        cls.WINDOW_WIDTH = 600;
        cls.WINDOW_HEIGHT = 500;

        cls.getShareCount = function () {
            superclass.getShareCount.call(this);

            var that = this;
            window.social_linkedIn = function (data) {
                that.shareCountFetched(data['count']);
            };

            this._shareCountScript('https://www.linkedin.com/countserv/count/share?url=' + encodeURIComponent(this.url) + '&callback=social_linkedIn');
        };
    });

    /*
        Провайдер Pinterest
    */
    window.PinterestProvider = Class(SocialProvider, function PinterestProvider(cls, superclass) {
        cls.WINDOW_WIDTH = 760;
        cls.WINDOW_HEIGHT = 600;

        cls.getShareCount = function () {
            superclass.getShareCount.call(this);

            var that = this;
            window.social_pinterest = function (data) {
                that.shareCountFetched(data['count']);
            };

            this._shareCountScript('https://widgets.pinterest.com/v1/urls/count.json?url=' + encodeURIComponent(this.url) + '&callback=social_pinterest');
        };
    });

    /*
        Facebook SDK
     */
    window.fbsdk = (function (d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0],
            fb_app_id = d.documentElement.dataset.fbAppId,
            sdk = window.fbsdk || {};
        if (d.getElementById(id)) return sdk;
        js = d.createElement(s);
        js.id = id;
        js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.2&appId=" + fb_app_id + "&autoLogAppEvents=1";
        fjs.parentNode.insertBefore(js, fjs);
        return sdk;
    }(document, "script", "facebook-sdk"));

    /*
        Twitter SDK
     */
    window.twttr = (function (d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0],
            t = window.twttr || {};
        if (d.getElementById(id)) return t;
        js = d.createElement(s);
        js.id = id;
        js.src = "https://platform.twitter.com/widgets.js";
        fjs.parentNode.insertBefore(js, fjs);

        t._e = [];
        t.ready = function (f) {
            t._e.push(f);
        };

        return t;
    }(document, "script", "twitter-wjs"));

    $(document).ready(function () {
        // $('.social-fb').each(function() {
        //     window.FacebookProvider(this);
        // });
        // $('.social-tw').each(function() {
        //     window.TwitterProvider(this);
        // });
        // $('.social-li').each(function() {
        //     window.LinkedInProvider(this);
        // });
        // $('.social-pn').each(function() {
        //     window.PinterestProvider(this);
        // });

        $('.share-block__linked-in').each(function () {
            window.LinkedInProvider(this);
        });
    });

})(jQuery);