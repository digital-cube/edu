$(document).ready( function() {

    $(document).on( 'click', '.l2>li', function(e) {
        $('.l2>li').removeClass('selected');
        $(this).addClass('selected');

        e.stopPropagation();
        return false;
    } )

    $(document).on( 'click', '.l1>li', function(e) {
        $(".l1>li ul").hide();
        $(this).find('ul').show();
    } )



} );
