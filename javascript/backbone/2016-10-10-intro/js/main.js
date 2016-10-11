var lang='en';


require.config({
    // urlArgs: "bust=" + (new Date()).getTime(),
    paths: {
        jquery: '../node_modules/jquery/dist/jquery.min',
        underscore: '../node_modules/underscore/underscore-min',
        backbone: '../node_modules/backbone/backbone-min',
        i18n: '../node_modules/i18n/i18n',
        util: 'common/util'
    },
    config: {
        i18n: {
            locale: lang
        }
    },
    shim: {
        jquery: {
            deps: [],
            //exports: "$"
        },
        underscore: {
            deps: [],
            //exports: "_"
        },
        backbone: {
            deps: ["jquery", "underscore"],
            //exports: "Backbone"
        },
    }
});

require(['app'], function (App) {
    App.initialize();
});
