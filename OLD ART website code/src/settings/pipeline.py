from ._pipeline import PIPELINE, Slider

PIPELINE['STYLESHEETS'].update({
    'critical': {
        'source_filenames': (
            'scss/grid.scss',
            'scss/layout.scss',
            'scss/buttons.scss',

            'header/scss/header.scss',
            'menu/scss/main_menu.scss',
        ),
        'output_filename': 'css_build/critical.css',
    },
    'core': {
        'source_filenames': (
            'scss/forms.scss',
            'scss/preloader.scss',
            'scss/text_styles.scss',
            'scss/popups/popups.scss',
            'scss/popups/preloader.scss',
            'scss/swiper.scss',
            'css/swiper.min.css',
            'footer/scss/footer.scss',
            'scss/toc.scss',

            'blog/scss/block.scss',
            'contacts/scss/block.scss',
            'rating/scss/rating.scss',
            'services/scss/block.scss',
            'social_networks/scss/social_links.scss',
            'google_maps/scss/label.scss',
            'google_maps/scss/balloon.scss',
            'testimonials/scss/block.scss',
            'breadcrumbs/scss/breadcrumbs.scss',

            'blocks/scss/location.scss',
            'blocks/scss/our_team.scss',
            'blocks/scss/share.scss',
            'blocks/scss/appointment.scss',
            'blocks/scss/why_choose_us.scss',
            'blocks/scss/our_mission.scss',
            'blocks/scss/focus_on.scss',
            'blocks/scss/insurances.scss',
            'blocks/scss/partners.scss',
            'blocks/scss/blog.scss',
            'blocks/scss/services.scss',
            'blocks/scss/contacts.scss',
            'contacts/scss/popup.scss',

        ),
        'output_filename': 'css_build/head_core.css',
    },
    'error': {
        'source_filenames': (
            'scss/error_page.scss',
        ),
        'output_filename': 'css_build/error.css',
    },
    'main': {
        'source_filenames': (
            'main/scss/index.scss',
        ),
        'output_filename': 'css_build/main.css',
    },
    'blog': {
        'source_filenames': (
            'blog/scss/index.scss',
        ),
        'output_filename': 'css_build/blog.css',
    },
    'services': {
        'source_filenames': (
            'services/scss/index.scss',
        ),
        'output_filename': 'css_build/services.css',
    },
    'service': {
        'source_filenames': Slider.css + (
            'services/scss/detail.scss',
        ),
        'output_filename': 'css_build/service.css',
    },
    'contacts': {
        'source_filenames': (
            'contacts/scss/index.scss',
        ),
        'output_filename': 'css_build/contacts.css',
    },
    'base_page': {
        'source_filenames': (
            'base_page/scss/index.scss',
            'base_page/scss/critical.scss',
            'paginator/scss/paginator.scss',
        ),
        'output_filename': 'css_build/base_page.css',
    },
})

PIPELINE['JAVASCRIPT'].update({
    'core': {
        'source_filenames': (
            'polyfills/modernizr.js',
            'js/jquery-3.3.1.min.js',
            'js/jquery-ui.min.js',

            'common/js/js.cookie.min.js',
            'common/js/jquery.utils.js',

            'js/popups/jquery.popups.js',
            'js/popups/preloader.js',
            'js/jquery.inspectors.js',
            'js/jquery.scrollTo.js',
            'js/jquery.fitvids.js',
            'js/text_styles.js',
            'js/swiper.min.js',
            'js/expander.js',
            'header/js/header.js',

            'js/jquery.mask.js',
            'attachable_blocks/js/async_blocks.js',
            'rating/js/rating.js',
            'menu/js/main_menu.js',
            'google_maps/js/core.js',
            'google_maps/js/balloon.js',
            'social_networks/js/share_buttons.js',
            'blog/js/block.js',
            'contacts/js/popup.js',
            'services/js/block.js',
            'testimonials/js/block.js',

            'blocks/js/our_mission.js',
            'blocks/js/services.js',
            'blocks/js/contacts.js',
        ),
        'output_filename': 'js_build/core.js',
    },
    'main': {
        'source_filenames': (
            'main/js/index.js',
        ),
        'output_filename': 'js_build/main.js',
    },
    'blog': {
        'source_filenames': (
            'blog/js/index.js',
        ),
        'output_filename': 'js_build/blog.js',
    },
    'service': {
        'source_filenames': (
            'services/js/detail.js',
        ),
        'output_filename': 'js_build/service.js',
    },
    'contacts': {
        'source_filenames': (
            'contacts/js/mask.js',
        ),
        'output_filename': 'js_build/contacts.js',
    },
    'base_page': {
        'source_filenames': (
            'base_page/js/base-page.js',
        ),
        'output_filename': 'js_build/base_page.js',
    },
})
