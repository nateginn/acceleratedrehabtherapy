(function($) {

    var onLoginHandler = function(response) {
        location.reload();
    };

    var onLogoutHandler = function(response) {
        location.reload();
    };

    // ==================================
    //  Авторизация
    // ==================================

    $(document).on('click', '.open-signin-popup', function() {
        showSignInPopup();
        return false;
    }).on('submit', '#ajax-popup-signin-form', function() {
        $.popup.showPreloader();
        sendSignInForm($(this), function() {
            $.popup.hidePreloader();
        });
        return false;
    });

    function showSignInPopup() {
        /** @namespace window.ajax_views.users.signin */
        $.preloader();

        return $.ajax({
            url: window.ajax_views.users.signin,
            type: 'GET',
            success: function(response) {
                $.popup({
                    classes: 'users-popup',
                    content: response
                }).show();
            }
        });
    }

    function sendSignInForm($form, callback) {
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = new FormData($form.get(0));
        data.append('referer', location.href);

        return $.ajax({
            url: $form.prop('action'),
            type: 'POST',
            data: data,
            dataType: 'json',
            processData: false,
            contentType: false,
            beforeSend: function() {
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if ($.isFunction(callback)) {
                    callback();
                }

                if (response.success) {
                    $form.get(0).reset();
                    onLoginHandler(response);
                } else {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                }
            },
            complete: function() {
                $form.removeClass('sending');
            }
        });
    }


    // ==================================
    //  Выход из профиля
    // ==================================

    $(document).on('click', '.open-signout-popup', function() {
        showSignOutPopup();
        return false;
    });

    function showSignOutPopup() {
        /** @namespace window.ajax_views.users.signout */
        $.preloader();

        return $.ajax({
            url: window.ajax_views.users.signout,
            type: 'POST',
            success: function(response) {
                $.popup().hide();
                onLogoutHandler(response);
            }
        });
    }

    // ==================================
    //  Регистрация
    // ==================================

    $(document).on('click', '.open-signup-popup', function() {
        showSignUpPopup();
        return false;
    }).on('submit', '#ajax-popup-signup-form', function() {
        $.popup.showPreloader();
        sendSignUpForm($(this), function() {
            $.popup.hidePreloader();
        });
        return false;
    });

    function showSignUpPopup() {
        /** @namespace window.ajax_views.users.signup */
        $.preloader();

        return $.ajax({
            url: window.ajax_views.users.signup,
            type: 'GET',
            success: function(response) {
                $.popup({
                    classes: 'users-popup',
                    content: response
                }).show();
            }
        });
    }

    function sendSignUpForm($form, callback) {
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = new FormData($form.get(0));
        data.append('referer', location.href);

        return $.ajax({
            url: $form.prop('action'),
            type: 'POST',
            data: data,
            dataType: 'json',
            processData: false,
            contentType: false,
            beforeSend: function() {
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if ($.isFunction(callback)) {
                    callback();
                }

                if (response.success) {
                    $form.get(0).reset();
                    onLoginHandler(response);
                } else {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                }
            },
            complete: function() {
                $form.removeClass('sending');
            }
        });
    }


    // ==================================
    //  Сброс пароля
    // ==================================

    $(document).on('click', '.open-reset-password-popup', function() {
        showResetPasswordPopup();
        return false;
    }).on('submit', '#ajax-popup-reset-password-form', function() {
        $.popup.showPreloader();
        sendResetPasswordForm($(this), function() {
            $.popup.hidePreloader();
        });
        return false;
    });

    function showResetPasswordPopup() {
        /** @namespace window.ajax_views.users.reset */
        $.preloader();

        return $.ajax({
            url: window.ajax_views.users.reset,
            type: 'GET',
            success: function(response) {
                $.popup({
                    classes: 'users-popup',
                    content: response
                }).show();
            }
        });
    }

    function sendResetPasswordForm($form, callback) {
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = new FormData($form.get(0));
        data.append('referer', location.href);

        return $.ajax({
            url: $form.prop('action'),
            type: 'POST',
            data: data,
            dataType: 'json',
            processData: false,
            contentType: false,
            beforeSend: function() {
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if ($.isFunction(callback)) {
                    callback();
                }

                if (response.success) {
                    $form.get(0).reset();

                    $.popup({
                        classes: 'users-popup',
                        content: response.message
                    }).show();
                } else {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                }
            },
            complete: function() {
                $form.removeClass('sending');
            }
        });
    }


    // ==================================
    //  Смена пароля
    // ==================================

    $(document).on('click', '.open-reset-confirm-popup', function() {
        showResetConfirmPopup();
        return false;
    }).on('submit', '#ajax-popup-reset-confirm-form', function() {
        $.popup.showPreloader();
        sendResetConfirmForm($(this), function() {
            $.popup.hidePreloader();
        });
        return false;
    });

    function showResetConfirmPopup() {
        /** @namespace window.ajax_views.users.reset_confirm */
        $.preloader();

        return $.ajax({
            url: window.ajax_views.users.reset_confirm,
            type: 'GET',
            success: function(response) {
                $.popup({
                    classes: 'users-popup',
                    content: response
                }).show();
            }
        });
    }

    function sendResetConfirmForm($form, callback) {
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = new FormData($form.get(0));
        data.append('referer', location.href);

        return $.ajax({
            url: $form.prop('action'),
            type: 'POST',
            data: data,
            dataType: 'json',
            processData: false,
            contentType: false,
            beforeSend: function() {
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if ($.isFunction(callback)) {
                    callback();
                }

                if (response.success) {
                    $form.get(0).reset();
                    $.popup().hide();
                } else {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                }
            },
            complete: function() {
                $form.removeClass('sending');
            }
        });
    }

})(jQuery);
