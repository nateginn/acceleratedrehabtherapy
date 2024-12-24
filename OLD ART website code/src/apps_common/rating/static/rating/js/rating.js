(function($) {

    /** @namespace window.ajax_views.rating.vote */

    var query;
    $(document).on('click', '.rating__star', function() {
        var rating = parseInt(window.localStorage.getItem('rating-value'));
        if (!isNaN(rating)) {
            return false;
        }

        var $star = $(this);
        var $list = $star.closest('.rating__stars');
        var starIndex = $list.find('.rating__star').index($star.get(0));
        if (starIndex < 0) {
            return false;
        }

        if (query) {
            query.abort();
        }
        query = $.ajax({
            url: window.ajax_views.rating.vote,
            type: 'POST',
            dataType: 'json',
            data: {
                rating: starIndex + 1
            },
            success: function(response) {
                if (response.rating) {
                    window.localStorage.setItem('rating-value', response.rating);
                    $list.addClass('rating__stars--vote-' + response.rating);
                }
            }
        });
    }).ready(function() {
        var rating = parseInt(window.localStorage.getItem('rating-value'));
        if (!isNaN(rating)) {
            $('.rating__stars').addClass('rating__stars--vote-' + rating);
        }
    });

})(jQuery);
