define([
    'jquery',
    'text!/js/pages/login/login.template.html'
], function ($, tpl) {
    'use strict';
    return {
        initialize: function() {

            $(document).off('click','#login_button');
            $(document).on('click','#login_button', this.login);

            $('#content').html(_.template(tpl)({
                username: 'igor@digitalcube.rs',
                message: 'please login to our system',
            }));

        },

        login: function() {
            $("#dijalog").show();
        }
    }
});