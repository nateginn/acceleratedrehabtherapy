(function() {

    CKEDITOR.plugins.add("toc", {
        requires: 'widget',
        icons: 'toc',
        init: function(editor) {
            editor.addContentsCss(this.path + 'styles/toc.css');

            editor.widgets.add('toc', {
                button: 'Create a ToC',
                template:
                    '<div class="toc">' +
                        '<h3 class="name">Skip ahead</h3>' +
                        '<div class="list">' +
                            '<ol><li>Item</li></ol>' +
                        '</div>' +
                    '</div>',
                allowedContent: 'div(!toc); div(!list); h3 ol li',
                requiredContent: 'div(toc); div(list)',
                editables: {
                    title: {
                        selector: '.name',
                        allowedContent: ''
                    },
                    content: {
                        selector: '.list',
                        allowedContent: 'ol; li; a[!href]'
                    }
                },
                upcast: function(element) {
                    return element.name === 'div' && element.hasClass('toc');
                }
            });
        }
    })

})();