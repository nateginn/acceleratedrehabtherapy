from django.conf import settings

CKEDITOR_DEFAULT_CSS = (
    'https://fonts.googleapis.com/css?family=Roboto:400,400italic,700,700italic',
    settings.STATIC_URL + 'ckeditor/admin/css/ckeditor.css',
)

# Конфигурация CKEditorField по умолчанию
CKEDITOR_CONFIG_DEFAULT = {
    'extraPlugins': 'blockquote,textlen,enterfix,image_attrs,table,tabletools,columns,div,',
    'toolbar': [
        {
            'name': 'basicstyles',
            'items': ['Bold', 'Italic', 'Blockquote', '-', 'RemoveFormat']
        },
        {
            'name': 'links',
            'items': ['Link', 'Unlink']
        },
        {
            'name': 'paragraph',
            'items': ['BulletedList', 'NumberedList', '-', 'Table', 'Columns', 'Div']
        },
        {
            'name': 'document',
            'items': ['Styles', 'Format', 'Source']
        },
    ]
}

CKEDITOR_UPLOAD_CONFIG_DEFAULT = {
    'extraPlugins': 'blockquote,textlen,enterfix,image_attrs,table,tabletools,columns,div,pagephotos,'
                    'pagevideos,pagefiles,simplephotos,toc',
    'toolbar': [
        {
            'name': 'basicstyles',
            'items': ['Bold', 'Italic', 'Blockquote', '-', 'RemoveFormat']
        },
        {
            'name': 'links',
            'items': ['Link', 'Unlink', 'Anchor']
        },
        {
            'name': 'paragraph',
            'items': ['BulletedList', 'NumberedList', '-', 'Table', 'Columns', 'Div']
        },
        {
            'name': 'insert',
            'items': ['PagePhotos', 'PageVideos', 'PageFiles', 'Toc']
        },
        '/',
        {
            'name': 'document',
            'items': ['Styles', 'Format', 'Source']
        },
    ]
}
