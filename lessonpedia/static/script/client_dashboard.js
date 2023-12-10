$(document).ready(function(){
    $("#set_active").click(function(){
        $(".set").css("display", "block")
        $(".db").css("display", "none")
    })

    $("#db_active").click(function(){
        $(".set").css("display", "none")
        $(".db").css("display", "block")
    })

    // settings nav bar manipulation

    $(document).ready(function() {
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
    });

    // toggling navbar dialog display
    $("#change_password").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".change_password_control_display").css("display", "block")
    })

    $("#update_profile").click(function(){
        $(".profile_control_display").css("display", "block")
        $(".change_password_control_display").css("display", "none")
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
            "color": "black"
        });
        $("#update_profile").css({
            "border": "1px solid black",
            "border-bottom": "1px solid transparent",
            "color": "rgb(3, 120, 3)"
        });
    })
    
    

})
