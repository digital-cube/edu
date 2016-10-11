define([
    'jquery',
    'underscore',
    'backbone',
    'router',
], function ($, _, Backbone, R) {
    'use strict';
    return {
        initialize: function () {
            console.log('app.initialize');

            this.handle_link_clicks();

            R.initialize();
        },

        handle_link_clicks: function () {
            $(document).on('click', 'a:not([data-bypass])', function (evt) {

                var href = $(this).attr('href');
                var protocol = this.protocol + '//';

                if ($(this).attr('data-type') === 'download') {
                    return true;

                } else if ($(this).attr('data-toggle') === 'lightbox') {
                    return false;

                } else if (href !== undefined && href.substr(0, 7) === 'mailto:') {
                    return true;

                } else if (href !== undefined && href.substr(0, 10) === 'javascript' || href === '#') {
                    return true;

                } else if (href !== undefined && href.length > 1 && href.substr(0, 7) === 'http://') {
                    if (href.substr(0, window.location.origin.length) !== window.location.origin) {
                        return true;
                    }

                } else if (href !== undefined && href.slice(protocol.length) !== protocol) {
                    evt.preventDefault();
                    R.go(href, true);
                }
            });
        },

    }
});