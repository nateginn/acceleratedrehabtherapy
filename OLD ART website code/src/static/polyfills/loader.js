(function() {

    var loadJS = function(src, async) {
        var script = document.createElement('script');
        script.src = src;
        script.async = async || false;
        document.body.appendChild(script);
    };

    if (!Modernizr.objectfit) {
        loadJS("/static/polyfills/ofi.js", '', true, function() {
            document.addEventListener('DOMContentLoaded', function() {
                objectFitImages();
            }, false);
        });
    }

    if (!Modernizr.sizes || !Modernizr.srcset || !Modernizr.picture) {
        document.createElement("picture");
        loadJS("/static/polyfills/picturefill.min.js");
    }
})();