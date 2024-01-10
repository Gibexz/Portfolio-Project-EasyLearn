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
        $(".db").hide()
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        })
    })

    $(".cancel_logout").click(function() {
        $(".logout_btn").css("display", "none")
        $("body, html").css("overflow", "auto")
        $(".db").show()
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
            $(".db").hide()
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
    $(".allReviews").hide()
    $(".db").show()
})

// All_Review logic
$('.all_review').click(function(){
    $('.allReviews').show()
    $("body, html").css("overflow-y", "hidden !important")
    $(".db").hide()
})

// Dynamic Selection
var primarySelection = [
    "Primary 1",
    "Primary 2",
    "Primary 3",
    "Primary 4",
    "Primary 5",
    "Primary 6",
]

var secondarySelection = [
    "JSS 1",
    "JSS 2",
    "JSS 3",
    "SSS 1",
    "SSS 2",
    "SSS 3",
]

var tertiarySelection = [
    "University 100L",
    "University 200L",
    "University 300L",
    "University 400L",
    "University 500L",
    "ND 1",
    "ND 2",
    "HND 1",
    "HND 2",
]

var others = [
    "PgD",
    "Masters",
    "PhD",
    "Others",
]


// Hangle dynamical dropdown
$('#eduLevel').change(function() {
    var selected = $(this).val();
    var dropdwn = $('#specifics')
    dropdwn.empty()
    if (selected == "Primary"){
        dropdwn.append('<option value="-- select one --" disabled selected >-- select one --</option>');
        primarySelection.forEach(element => {
            dropdwn.append('<option value="' + element + '">' + element + '</option>')
        });
    } else if (selected == "Secondary"){
        dropdwn.append('<option value="-- select one --" disabled selected >-- select one --</option>');
        secondarySelection.forEach(element => {
            dropdwn.append('<option value="' + element + '">' + element + '</option>')
        });
    } else if (selected == "Tertiary"){
        dropdwn.append('<option value="-- select one --" disabled selected >-- select one --</option>');
        tertiarySelection.forEach(element => {
            dropdwn.append('<option value="' + element + '">' + element + '</option>')
        });
    } else if (selected == "Others"){
        dropdwn.append('<option value="-- select one --" disabled selected >-- select one --</option>');
        others.forEach(element => {
            dropdwn.append('<option value="' + element + '">' + element + '</option>')
        });
    } else {
        dropdwn.append('<option value="">Select Educational Level</option>')
    }
});

// edit review logics
$(".allReview_content").on("click", ".message .editReview", function(e){
    e.stopPropagation();
    var parentContainer = $(this).closest('.message');
    var transitSection = parentContainer.next(".transit");
    transitSection.show().css("opacity", "1");
});

$(".cancelEdit").click(function(){
    var parentContainer = $(this).closest('.transit');
    parentContainer.hide().css("opacity", "0");
});

var url = 'http://127.0.0.1:8000/client/api/contractForm';
var receivedContract = {};
$(".endDate").text("No engagement yet")

$.ajax({
    url: url,
    method: 'GET',
    dataType: 'json',
    success: function(response) {
        receivedContract = response;
        console.log(receivedContract);

        $(".tutor_info").each(function() {
            var ids = $(this).find(".tutorId").text().split(',');

            for (var id of ids) {
                var parsedId = parseInt(id.trim(), 10);

                if (!isNaN(parsedId) && parsedId in receivedContract) {
                    var obtained = receivedContract[parsedId]['status'];
                    var endDate = receivedContract[parsedId]['endDate']
                    var amountProposed = receivedContract[parsedId]['amount']
                    var amount_remaining = receivedContract[parsedId]['amountRemaining']
                    
                    // Select specific elements within the current .tutor_info container
                    var statusElement = $(this).find(".requestStatus .statusDefault");
                    var statuusElement = $(this).find(".requestStatus .statuus");
                    var engagement = $(this).find(".engagement")
                    var payment = $(this).find(".makePayment")
                    var completed = $(this).find(".congrats")
                    var balanceUp = $(this).find(".balanceUp")
                    var endDateElement = $(this).find(".endDate")

                    console.log("ID:", parsedId, "Status:", obtained);
                    
                    if (endDate){
                        endDateElement.text(endDate)
                    }

                    if (obtained === 'Pending') {
                        statusElement.removeClass("statusDefault").addClass("statusPending");
                        statuusElement.text("pending approval");
                        payment.hide()
                        engagement.hide()
                    } else if (obtained === "Active") {
                        statusElement.removeClass("statusDefault").addClass("statusActive");
                        statuusElement.text("Approved");
                        payment.show()
                        engagement.hide()
                    } else if (obtained === "Declined") {
                        statusElement.removeClass("statusDefault").addClass("statusDecline");
                        statuusElement.text("Declined");
                        payment.hide()
                        engagement.hide()
                    }

                    if ((amount_remaining > 0) && (amount_remaining != amountProposed)){
                        payment.hide()
                        balanceUp.show()
                       
                    } else if (amount_remaining == 0){
                        statusElement.removeClass("statusDefault").addClass("statusActive");
                        statuusElement.text("Approved");
                        engagement.hide()
                        payment.hide()
                        balanceUp.hide()
                        completed.show()
                    }

                }
            }
        });
    },
    error: function(error) {
        console.error('Error fetching API data:', error);
    }
});



})
