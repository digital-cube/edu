define([
    'jquery',
    'text!/js/pages/home/home.template.html'
], function ($, tpl) {
    'use strict';
    return {
        initialize: function() {

            $('#content').html(tpl);

        },
    }
});