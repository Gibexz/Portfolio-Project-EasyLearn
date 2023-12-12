$(document).ready(function() {

    // DashBoard Navigation Links 
    // start
    $('.nav_links').on("click", function(e) {
        e.preventDefault();

        $('.nav_links').removeClass('active');
        $(this).addClass('active');

        var targetDiv = $(this).attr('class').split(' ')[1];
        $('.content_divs').hide();
        $('.' + targetDiv + '_contents').show()
    });

    // set dashboard as active by default by triggering a click
    $('.dashboard').trigger('click');
    //stop


    // settings related jquery
    // start
    $(".test").click(function() {
        // Remove active class and reset styles for all td elements
        $(".test").css({
            "border": "none",
            "border-bottom": "1px solid black",
            "color": "black"
        });

        $("#deactivate_account").click(function(){
            $(this).css("color", "red")
        })
        $("#deactivate_account").css("color", "red")

        // Add active class and apply styles to the clicked td element
        $(this).css({
            "border": "1px solid black",
            "border-bottom": "1px solid transparent",
            "color": "rgb(3, 120, 3)"
        });
    });

    // toggling settings nav dialog display
    $("#change_password").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".change_password_control_display").css("display", "block")
        $(".doc_uploads").css("display", "none")
    })

    $("#update_profile").click(function(){
        $(".profile_control_display").css("display", "block")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".doc_uploads").css("display", "none")
    })
    $("#update_schedule").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "block")
        $(".doc_uploads").css("display", "none")
    })

    $("#uploads").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".doc_uploads").css("display", "block")
    })

    $("#deactivate_account").click(function(){
        $(".deactivate_account_control_display").css("display", "block")
    })
    
    $(".mistake").click(function(){
        $(".deactivate_account_control_display").css("display", "none")
        $(".profile_control_display").css("display", "block")
        $(".change_password_control_display").css("display", "none")
        $("#deactivate_account").css({
            "border": "none",
            "border-bottom": "1px solid black",
            "color": "red",
        });
        $("#update_profile").css({
            "border": "1px solid black",
            "border-bottom": "1px solid transparent",
            "color": "rgb(3, 120, 3)"
        });
    })
    // stop
    

    // update profile js
    $('#profile_update_save_btn').on('click', function(event) {
        event.preventDefault();
        alert("Password successfully changed");
        // implementation of database interaction codes
    });

    // update password js
    $('#password_update_save_btn').on('click', function(event) {
        event.preventDefault();
        alert("Password successfully changed");
        // implementation of database interaction codes
    });

   // update schedule js
    $('#day_save_btn').on('click', function(event) {
        event.preventDefault();
        
        const selectedDays = $('input[name="workingDay"]:checked').map(function() {
            return this.value;
        }).get();
        
        alert("Selected Working Days: " + selectedDays.join(", "));
        // Here you can perform further actions like sending the selected days to a server or saving them in a database
    });

    
    $('#hour_save_btn').on('click', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const selectedHours = $('input[name="workingHour"]:checked').map(function() {
            return this.value;
        }).get();

        alert("Selected Working Hours: " + selectedHours.join(", "));
        // Here you can perform further actions like sending the selected hours to a server or saving them in a database
    });


    // logout_activation
    // start
    $('.logout_activation').click(function(){
        $(".logout_btn").css("display", "block")
    })

    $(".cancel_logout").click(function() {
        $(".logout_btn").css("display", "none")
    })
    // stop

});

$(document).ready(function() {
    
})