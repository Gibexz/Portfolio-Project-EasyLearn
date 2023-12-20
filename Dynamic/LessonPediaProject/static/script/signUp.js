$(document).ready(function(){
    $(".learner").click(function(){
        $('.link_box_container').show()
        $('.hide_signup').show()
        $(".tutor_form").css("display", "none")
        $(".learner_form").css("display", "block")
        $(this).css({color: "#4BE5CA", "font-weight": "bold", "border-bottom": "2px solid #4BE5CA",});
        $(".tutor").css({color: "white", "font-weight": "normal", "border-bottom": "none"});
        var learnerUrl = $(this).data('url')
        window.location.href = learnerUrl
    })

    $(".tutor").click(function(){
        $('.link_box_container').hide()
        $('.hide_signup').hide()
        $(".learner_form").css("display", "none");
        $(".tutor_form").css("display", "block");
        $(this).css({color: "#4BE5CA", fontWeight: "bold", borderBottom: "2px solid #4BE5CA",});
        $(".learner").css({color: "white", fontWeight: "normal", borderBottom: "none",});
        var tutorUrl = $(this).data('url')
        window.location.href = tutorUrl;
    })

})