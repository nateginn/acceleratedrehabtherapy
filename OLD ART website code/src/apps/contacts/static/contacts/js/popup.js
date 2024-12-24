(function ($) {

    $(document).ready(function () {
        if (window.location.pathname == '/') {
            showContactPopup();
        }
        return false;
    });

    // $(document).on('click', '.open-message-popup', function () {
    //     showContactPopup();
    //     return false;
    // });


    function showContactPopup() {
        /** @namespace window.ajax_views.contacts.popup */

        return $.ajax({
            url: window.ajax_views.contacts.popup,
            type: 'GET',
            success: function (response) {
                $.popup({
                    classes: 'message-popup',
                    content: response
                }).show();
                if (!($(".pop-up").hasClass("pop-up--active"))) {
                    $.popup().destroy();
                }
            }
        });
    }

})
(jQuery);