$(document).ready(function(){

    $(".set_active").click(function(){
        $(".set").css("display", "block")
        $(".db").css("display", "none")
        $(".history_set").css("display", "none")
    })

    $(".db_active").click(function(){
        $(".set").css("display", "none")
        $(".db").css("display", "block")
        $(".history_set").css("display", "none")
    })

    $(".history_active").click(function(){
        $(".set").css("display", "none")
        $(".db").css("display", "none")
        $(".history_set").css("display", "block")
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
        $("body html").css("overflow", "hidden")
    })

    $(".mistake").click(function(){
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        })
        $("body html").css("overflow", "auto")
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
    
    // logout_activation

    $('.logout_activation').click(function(){
        $(".logout_btn").show()
        $("body, html").css("overflow", "hidden")
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        })
    })

    $(".cancel_logout").click(function() {
        $(".logout_btn").css("display", "none")
        $("body, html").css("overflow", "auto")
    })

    // Ajax load
//    function loadView(){
//     var url = $("#change_password").data("url");
//     $.ajax({
//         type: "GET",
//         url: url,
//         success: function(response) {
//             $("#change_password").html(response);
//         },
//         error: function(error) {
//             console.log('Error:', error);
//         }
//     });
//    }
   
//    $("#change_password").click(function(){
//     loadView()
//    })

// Profile picture preview
$("#UpdateDp").change(function(){
    var fileInput = this;
    var file = fileInput.files[0];
    if (file) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var previewImage = $('#previewDp');
            previewImage.attr('src', e.target.result);
            $("#change").css({color: 'blue', "pointer-events": 'auto', cursor: 'pointer'})
        };
        reader.readAsDataURL(file);
    }
})

// remove user
$(".remove_tutor").click(function(e){
    e.stopPropagation(); 
    var commonAncestor = $(this).closest('.tutor_toggles');
    var removeUser = commonAncestor.next(".removeUser");

    removeUser.show();
    $("body, html").css({"overflow": "hidden"});
});

$(".cancel_remove").click(function(event){
    $(".removeUser").hide();
    $("body, html").css({"overflow": "auto"});
});

$("body").on("click", function(e){
    if (!$(e.target).hasClass("remove_tutor") || !$(e.target).hasClass("rankStar")) {
        $(".removeUser").hide();
        $(".rankStar").hide();
        $("body, html").css({"overflow": "auto"});
    }
});


// Ranking implementation
var getID
$(".rank").on('click', function(e) {
    e.stopPropagation(); 
    var rankStar = $(this).find(".rankStar");
    rankStar.show();

    getID = $(this).find(".getID").text();
    client_username = $(this).find(".client_username").text();

    url = `/client/signIn/User_dashboard/${client_username}?tutorId=${getID}`
    $.ajax({
        url: url,
        method: "GET",
        dataType: "json",
        success: function (response) {
            var rankVal = response.rank;

            if (rankVal >= 0) {
                var viewColorStars = "";
                var defaultColorStars = "";

                for (var i = 0; i < rankVal; i++) {
                    viewColorStars += '<span class="viewColor">★</span>';
                }                

                for (var i = 0; i < (5 - rankVal); i++) {
                    defaultColorStars += '<span class="defaultColor">★</span>';
                }

                var allStars = viewColorStars + defaultColorStars;
                rankStar.find(".rankTutor").html(allStars);
            }
        },
        error: function (error) {
            // Handle errors if needed
        }
    });
});


// Handle the initial click event
$(".rank").on('click', function(e) {
    e.stopPropagation(); 
    var rankStar = $(this).find(".rankStar");
    rankStar.show();

    getID = $(this).find(".getID").text();
    client_username = $(this).find(".client_username").text();

    url = `/client/signIn/User_dashboard/${client_username}?tutorId=${getID}`
    $.ajax({
        url: url,
        method: "GET",
        dataType: "json",
        success: function (response) {
            var rankVal = response.rank;

            if (rankVal >= 0) {
                var viewColorStars = "";
                var defaultColorStars = "";

                for (var i = 0; i < rankVal; i++) {
                    viewColorStars += '<span class="viewColor">★</span>';
                }

                for (var i = rankVal; i < 5; i++) {
                    defaultColorStars += '<span class="defaultColor">★</span>';
                }

                rankStar.find(".rankTutor").html(viewColorStars + defaultColorStars);
            }
        },
        error: function (error) {
        }
    });
});

// Handle the click event for dynamically added elements
$(".rank").on('click', '.rankTutor span', function() {
    var clickedIndex = $(this).index() + 1;
    var tutorId = $(this).closest(".tutor_info").find(".hideRating .tutorId").text();

    $.ajax({
        url: `/client/tutor/ranking/${tutorId}/${clickedIndex}`,
        method: "GET",
        success: function (response) {
            console.log('Success');
        },
        error: function (error) {
            console.log('Error:', error.responseJSON.error);
        }
    });

    var rankTutorContainer = $(this).closest('.rankTutor');

    rankTutorContainer.find("span").each(function(i) {
        if (i < clickedIndex) {
            $(this).removeClass("defaultColor").addClass("rankColor");
        } else {
            $(this).removeClass("rankColor").addClass("defaultColor");
        }
    });
});


$(".db").on("click", ".searchClient_button", function (event) {
    event.preventDefault();

    var keyword = $('#keywordVal').val()
    url_keyword = `/client/filter/tutor/keyword=/${keyword}`
    
    if ((keyword === "all") || (keyword == '*')){
        location.reload()
    } else {
    $.ajax({
        url: url_keyword,
        success: function (response) {
            var dataFound = false;
            $(response).find(".tutor_name").each(function () {
                if ($(this).text().trim() !== "") {
                    dataFound = true;
                    return false; 
                }
            });

            if (dataFound) {
                $(".db").html($(response).find(".db").html());
            } else {
                $('.subjects').hide()
                $(".notFound").show()
                $(".notFound p").text(`No tutor with keyword "${keyword}"`);
                return false
            }
        },
        error: function (error) {
            alert("No item found")
        }
    })
    };
});

// Review ajax method
$(".db").on("click", ".review", function () {

    tutorID = $(this).closest(".tutor_info").find(".hideRating .tutorId").text();
    url = `/client/review/tutorid/${tutorID}`
    $.ajax({
        url: url,
        success: function (response) {
            var data = response.Rtutor
            $('.reviews').show()
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            })
            $('.review_tutor_details .name').text(`${data['TfirstName']} ${data['TlastName']} [${data['Tqualification']}]`)
            $('.profilePicture p').text(data['Temail']),
            $('.profilePicture img').attr('src', data['dp'])
            
            var rankValue = data['Trank']
            if (rankValue >= 1){
                var starsString = Array(rankValue + 1).join('★');
                var balance = 5 - rankValue;
                var defaultStars = Array(balance + 1).join('★');
                $(".Trank .rankGotten").text(starsString)
                $(".Trank .lostRank").text(defaultStars)
            }
            $('html, body').css("overflow", "hidden")

            var tutorId = data['id'];
            var formAction = $('#reviewForm').attr('action').replace(/0/, tutorId);
            $('#reviewForm').attr('action', formAction);

        }
    });
});

$(".closeReview").click(function(){
    $('.reviews').hide()
})

})