
function check_if_user_is_logged_in(ulogovan, neulogovan) {

    var settings = {
          "async": true,
          "crossDomain": true,
          "url": "http://developer.digitalcube.rs:8999/user/check",
          "method": "POST",
          "headers": {
              "authorization": localStorage.token,
          }
    }

    $.ajax(settings).done(ulogovan).error(neulogovan);

}

function login() {
    var username=$("#username").val();
    var password=$("#password").val();

    if (username==='' || username===undefined) {
        alert('molimo vas unesite username');
        return;
    }
    if (password==='' || password===undefined) {
        alert('molimo vas unesite password');
        return;
    }


    var settings = {
          "async": true,
          "crossDomain": true,
          "url": "http://developer.digitalcube.rs:8999/user/login?username="+username+"&password="+password,
          "method": "POST",
          "headers": {
          }
    }

    $.ajax(settings).done(
        function(response) {
            response = $.parseJSON( response );
            localStorage.token = response.token;
            f_ulogovan();
        }
    ).error(
        function(){
            alert('greska u logovanju korisnika');
        }
    );

    console.log(2);



}

function prikazi_sve_kontakte() {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "http://developer.digitalcube.rs:8999/api/contacts",
      "method": "GET",
      "headers": {
          "authorization": localStorage.token,
      }
    }

    console.log(1);
    $.ajax(settings).done(
        function(response) {
            response = $.parseJSON( response );

            var tbl='<table>';

            for (var c=0;c<response.contacts.length;c++) {
                console.log('c',c,response.contacts[c]);
                tbl+='<tr data-contact-id="'+response.contacts[c].id+'"><td>'+response.contacts[c].first_name+'</td>'
            }
            tbl+="</table>"

            console.log('svi kontakti',response);

            $("#placeholder_contacts").html(tbl);

        }
    ).error( function(){alert('err');});

}

function f_ulogovan() {
    $("#template_loginform").hide();
    $("#logged_user_screen").show();

    $(document).off('click', '#add');
    $(document).on('click', '#add', function () {
        alert('dodajem kontakt...');
    });

    $(document).off('click', '#logout');
    $(document).on('click', '#logout', function () {
        delete localStorage.token;
        f_neulogovan();
    });
    prikazi_sve_kontakte();

}
function f_neulogovan() {
    $("#logged_user_screen").hide();
    $("#template_loginform").show();


    $(document).off('click', '#login' );
    $(document).on('click', '#login', login );


}





$( document ).ready(function() {
    check_if_user_is_logged_in(f_ulogovan, f_neulogovan);
});
