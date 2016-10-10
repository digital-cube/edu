$(document).ready(function(){
    $('.responsive-nav-icon').click(function(){
        $(this).toggleClass('open');
    });
});


$(function() {
    // Insert Responsive Sidebar Icon
    $('<div  class="responsive-nav-icon" style="position:fixed;" />').appendTo('.zid.one');
    $('<div class="responsive-nav-close" />').appendTo('.nav-container');

    // Navigation Slide In
    $('.responsive-nav-icon').click(function() {
        $('#overlay').hide();
        $('.responsive-nav-icon').fadeOut();

        $('.nav-container').addClass('slide-in');
        $('html').css("overflow", "hidden");
        $('#overlay').show();
        return false;
    });

    // Navigation Slide Out
    $('#overlay, .responsive-nav-close').click(function() {
        $('.responsive-nav-icon').fadeIn();

        $('.nav-container').removeClass('slide-in');
        $('html').css("overflow", "auto");
        $('#overlay').hide();
        return false;
    });
});


$(function () {
    var count = $("#slider > .slides > li").length
    var slider = 1
    var speed=6000
    var fadeSpeed = 1000
    var loop

    var to=[null,null,null,null];

    start()
    $("#1").fadeIn(fadeSpeed);
    $('.right').click(right)
    $('.left').click(left)
    $('.dots > li').click(goToSlide)
    // $('#slider').mouseenter(stop)
    // $('#slider').mouseleave(start)

    function start(){
        loop = setInterval(next, speed)
    }
    function stop(){
        clearInterval(loop)
    }
    function goToSlide(){

        var slide = $(this).attr('data-id');
        if(slider != slide){
            slider = slide
            $("#slider .slides > li").hide()
            $("#" + slider).fadeIn()
            stop()

            start()
        }
    }
    function right() {
        stop()
        next()
        start()
        return false
    }

    function left() {
        stop()
        prev()
        start()
        return false
    }

    function prev() {
        slider--
        if (slider < 1) {
            slider = count
        }

        $("#slider > .slides > li").fadeOut(fadeSpeed)
        $("#" + slider).fadeIn(fadeSpeed)
    }

    function next() {

        slider++
        if (slider > count) {
            slider = 1
        }

        $("#slider > .slides > li").fadeOut(fadeSpeed)
        $("#" + slider).fadeIn(fadeSpeed)


        if(slider == 2){
            showUlContent()
        }

    }



    function killTimeouts() {
        for (var i=0;i<to.length;i++) {
            if (to[i]!==null) {
                clearTimeout(to[i]);
                to[i]=null;
            }
        }
    }
    function showUlContent(){
        $("#li0").fadeIn();
        to[0]=setTimeout( function() {
            $("#li1").fadeIn();
            to[1]=setTimeout( function() {
                $("#li2").fadeIn();
                to[2]=setTimeout( function() {
                    $("#li3").fadeIn();
                    to[3]=setTimeout( function() {
                        $("#li4").fadeIn();
                    }, 500);
                }, 500);
            }, 500);
        }, 500);

    }


});

