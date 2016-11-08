var gulp = require('gulp'),
    gp_concat = require('gulp-concat'),
    gp_rename = require('gulp-rename'),
    gp_uglify = require('gulp-uglify'),
    gp_mincss = require('gulp-clean-css');

gulp.task('vendor-js', function(){
    return gulp.src(
            ['bower_components/jquery/dist/jquery.min.js',
            'bower_components/bootstrap/dist/js/bootstrap.min.js',
            'bower_components/jquery.maskedinput/dist/jquery.maskedinput.min.js',
            'bower_components/moment/min/moment-with-locales.min.js',
            'bower_components/eonasdan-bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js']
        )
        .pipe(gp_concat('vendor.min.js'))
        .pipe(gulp.dest('static/js'));
});

gulp.task('vendor-css', function(){
    return gulp.src(
            ['bower_components/bootstrap/dist/css/bootstrap.min.css',
            'bower_components/bootstrap/dist/css/bootstrap-theme.min.css',
            'bower_components/eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css']
        )
        .pipe(gp_concat('vendor.min.css'))
        .pipe(gulp.dest('static/css'));
});

gulp.task('contacts-js', function(){
    return gulp.src(['contacts/static/contacts.js'])
        .pipe(gp_uglify())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/js'));
});

gulp.task('contacts-css', function(){
    return gulp.src(['contacts/static/contacts.css'])
        .pipe(gp_mincss())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/css'));
});

gulp.task('currency-js', function(){
    return gulp.src(['currency/static/currency.js'])
        .pipe(gp_uglify())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/js'));
});

gulp.task('currency-css', function(){
    return gulp.src(['currency/static/currency.css'])
        .pipe(gp_mincss())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/css'));
});

gulp.task('lecture-js', function(){
    return gulp.src(
        ['lecture/static/js/jquery.dadata.suggestions.js',
        'lecture/static/js/kladr.js',
        'lecture/static/js/lecture.js']
        )
        .pipe(gp_concat('lecture.min.js'))
        .pipe(gp_uglify())
        .pipe(gulp.dest('static/js'));
});

gulp.task('lecture-css', function(){
    return gulp.src(
        ['lecture/static/kladr.css',
        'lecture/static/lecture.css']
        )
        .pipe(gp_concat('lecture.min.css'))
        .pipe(gp_mincss())
        .pipe(gulp.dest('static/css'));
});

gulp.task('passport-js', function(){
    return gulp.src(['passport/static/passport.js'])
        .pipe(gp_uglify())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/js'));
});

gulp.task('passport-css', function(){
    return gulp.src(['passport/static/passport.css'])
        .pipe(gp_mincss())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/css'));
});

gulp.task('template-css', function(){
    return gulp.src(['static_src/template.css'])
        .pipe(gp_mincss())
        .pipe(gp_rename({suffix: '.min'}))
        .pipe(gulp.dest('static/css'));
});

gulp.task('copy-fonts', function () {
    return gulp.src(['bower_components/bootstrap/dist/fonts/**/*']).pipe(gulp.dest('static/fonts'));
});

gulp.task('copy-highstock', function () {
    return gulp.src(['bower_components/highcharts/highstock.js'])
    .pipe(gp_rename({suffix: '.min'}))
    .pipe(gulp.dest('static/js'));
});

// run them like any other task
gulp.task('default', [
  'vendor-js',
  'vendor-css',
  'contacts-js',
  'contacts-css',
  'currency-js',
  'currency-css',
  'lecture-js',
  'lecture-css',
  'passport-js',
  'passport-css',
  'template-css',
  'copy-fonts',
  'copy-highstock'
]);