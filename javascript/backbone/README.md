Backbone project from scratch
=============================

npm init - //entry point is gulpfile.js.
add "gulp":"gulp" in package.json // mind the coma

npm install gulp gulp-sass gulp-webserver --save
make gulpfile.js // from template
// .pipe(sass().on('error', sass.logError))
// delete from template if you dont want to import material bootstrap

npm install requirejs, underscore, jquery, backbone,
bootstrap@3,bootstrap-material-design --save 

make index.html

Entry point
```html
<html>
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="/css/styles.css">
    <script data-main="/js/main" src="/node_modules/requirejs/require.js"></script>

    <!-- Material Design fonts -->
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700">
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/icon?family=Material+Icons">
</head>

<body>

<div id="content">
</div>

</body>
</html>
```


mkdir scss/ _vars.scss, styles.scss, reset.scss, main.scss //from template
//comment out libs.scss and import line in styles.scss if 
mkdir css
mkdir js / copy from template main.js app.js router.js text.js

mkdir js/pages // layout.htm

in app.js -> $("#content").html(tplMainLayout); /// tplMainLayout ==
layout.html	
