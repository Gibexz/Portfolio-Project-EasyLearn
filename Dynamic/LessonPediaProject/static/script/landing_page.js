$(document).ready(function(){
    $(".other_nav").hover(function(){
        $(this).css("color", "green")
        $("#default").css("color", "black")
    })

    $(".other_nav").mouseleave(function(){
        $(this).css("color", "black")
        $("#default").css("color", "green")
    })

    $(".rightArrow").click(function(){
        $(this).closest(".content").find("p").toggle();
    });
})

// dropdown menu tweak
$(document).ready(function(){
    $(".login_btn").click(function(){
        $(".dropdown-content").toggle();
    });

    // Close dropdown when clicking outside
    $(document).on("click", function(event){
        if(!$(event.target).closest(".dropdown").length){
            $(".dropdown-content").hide();
        }
    });

    $("#explore").click(function(){
        $(".validate_signin").show()
    })
    $("#explore").mouseleave(function(){
        $(".validate_signin").hide()
    })

});