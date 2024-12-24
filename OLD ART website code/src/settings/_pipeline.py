from collections import namedtuple

# ===============================
#   Наборы скриптов с зависимостями.
#
#   Пример использования:
#       'some_page': {
#           'source_filenames': PopupGallery.css + (
#           ...
#           ),
#           ...
#       }
# ===============================

# Слайдер
Slider = namedtuple('Slider', ['css', 'js'])(
    css=(
        'css/swiper.min.css',
        'scss/swiper.scss',
    ),
    js=(
        'js/swiper.min.js',
    )
)


PIPELINE = {
    'PIPELINE_ENABLED': True,
    'COMPILERS': (
        'libs.pipeline.sassc.SASSCCompiler',
    ),
    'SASS_ARGUMENTS': '-t compressed',
    'CSS_COMPRESSOR': 'libs.pipeline.cssmin.CSSCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.jsmin.JSMinCompressor',

    'STYLESHEETS': {
        'admin_customize': {
            'source_filenames': (
                'admin/css/jquery-ui/jquery-ui.min.css',
                'admin/scss/admin_fixes.scss',
                'admin/scss/admin_table.scss',
                'admin/scss/dl_core.scss',
                'admin/scss/dl_login.scss',
                'admin/scss/hierarchy_filter.scss',
            ),
            'output_filename': 'admin/css/customize.css',
        },
    },

    'JAVASCRIPT': {
        'admin_customize': {
            'source_filenames': (
                'admin/js/jquery-ui.min.js',
                'common/js/js.cookie.min.js',
                'common/js/jquery.ajax_csrf.js',
                'common/js/jquery.mousewheel.js',
                'common/js/jquery.utils.js',
                'common/js/file_dropper.js',
            ),
            'output_filename': 'admin/js/customize.js',
        },
    }
}
