$(document).ready(function(){
    var status = $("#validate").data('activate')
    
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

    $('#con_pass').on({
        input: function () {
          comparePasswords();
        },
        mouseleave: function () {
          comparePasswords();
        }
      });
    
      function comparePasswords () {
        const pass_val = $('#pass').val();
        const compare_pass = $('#con_pass').val();
    
        if (pass_val !== compare_pass) {
          $('#con_pass').css('border-color', 'red');
          $('#registerBtn').prop('disabled', true);
          $('#registerBtn').css('background-color', 'red').css('color', 'white');
          $('#registerBtn').val('Check password');
          $("#registerBtn").css('cursor', 'not-allowed')
        } else {
          $('#con_pass').css('border-color', '');
          $('#registerBtn').prop('disabled', false);
          $('#registerBtn').css('background-color', '').css('color', '');
          $('#registerBtn').css('background-color', '');
          $('#registerBtn').val('Submit');
          $("#registerBtn").css('cursor', 'pointer')
        }
      }
})
