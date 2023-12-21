$(document).ready(function(){
    $('.app_admin_login').click(function() {
        $('.adminLogin').css('display', 'block');
        $('.adminSignUp').css('display', 'none');
        $('.app_admin_login').addClass('activeForm');
        $('.app_admin_signUp').removeClass('activeForm');
    });

    $('.app_admin_signUp').click(function() {
        $('.adminSignUp').css('display', 'block');
        $('.adminLogin').css('display', 'none');
        $('.app_admin_signUp').addClass('activeForm');
        $('.app_admin_login').removeClass('activeForm');
    });
});
