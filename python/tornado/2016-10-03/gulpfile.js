var gulp = require('gulp'),
    sass = require('gulp-sass');

gulp.task('sass', function() {
    return gulp.src(['css/*.scss', 'css/pages/*.scss', 'css/inc/*.scss'])
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('css'));
});

gulp.task('watch', function(){
    gulp.watch(['css/*.scss'], ['sass']);
    gulp.watch(['css/pages/*.scss'], ['sass']);
    gulp.watch(['css/inc/*.scss'], ['sass']);
});

gulp.task('default', ['sass', 'watch'], function() {});
