define([
    'jquery',
    'underscore',
    'backbone',
    'util',
    'pages/login/login.controller',
    'pages/home/home.controller',
], function ($, _, Backbone, U, page_login, page_home) {

    var AppRouter = Backbone.Router.extend({
        currentViews: {},
        previousViews: null,
        appRouter: null
    });

    var initialize = function() {
        this.appRouter = new AppRouter;

        this.appRouter.route(/(.*)/, 'home');
        this.appRouter.route(/^login\/?/, 'login');

        this.appRouter.on('route:home', function() {
            console.log('homepage route');
            page_home.initialize();
        })

        this.appRouter.on('route:login', function() {
            console.log('login route');
            page_login.initialize();
        });

        Backbone.history.start( {pushState: true} );
    }

    var go = function(page, trigger) {
        this.appRouter.navigate(page, {trigger: trigger});
    }

    return {
        initialize: initialize,
        go: go,
    }


});