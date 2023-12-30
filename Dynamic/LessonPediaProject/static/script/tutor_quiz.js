$(document).ready(function () {
    // Quiz finish button click event
    $("#finishBtn").on("click", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Check if quiz count is less than 2
        var quizCount = parseInt($("#quiz_count").val());
        if (quizCount < 2) {
            calculateScoreAndRedirect();
        } else {
            alert("You have already taken the quiz twice.");
        }
    });

    const englishAnswers = {
        englishQ1: 'Cowardly',
        englishQ2: 'Children',
        englishQ3: 'Joyful',
        englishQ4: 'Ate',
        englishQ5: 'Mad'
    };

    const abstractAnswers = {
        abstractQ1: '8.5',
        abstractQ2: 'Pentagon',
        abstractQ3: '25',
        abstractQ4: '48',
        abstractQ5: '□'
    };

    // Countdown timer
    var timeLeft = 20;
    var timer = setInterval(function () {
        $("#timer").text(formatTime(timeLeft));
        timeLeft--;
        if (timeLeft < 0) {
            clearInterval(timer);
            calculateScoreAndRedirect();
        }
    }, 1000);

    // Function to format time as mm:ss
    function formatTime(seconds) {
        var minutes = Math.floor(seconds / 60);
        var remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds < 10 ? "0" : ""}${remainingSeconds}`;
    }

    // Function to calculate the score and redirect
    function calculateScoreAndRedirect() {
        clearInterval(timer);
        var score = calculateScore();
        $("#quiz_result").val(score);
        storeScoreToDatabase(score);
        displayScorePopup(score);
    }

    // Function to calculate the score based on selected answers
    function calculateScore() {
        var totalQuestions = 10;
        var correctAnswers = 0;

        // Function to compare user-selected answers with correct answers
        function checkAnswers(answers) {
            for (const question in answers) {
                const userAnswer = $(`input[name=${question}]:checked`).val();
                if (userAnswer === answers[question]) {
                    correctAnswers++;
                }
            }
        }

        // Check English section answers
        checkAnswers(englishAnswers);

        // Check Abstract section answers
        checkAnswers(abstractAnswers);
        var scorePercentage = (correctAnswers / totalQuestions) * 100;
        return scorePercentage.toFixed(2);
    }

    // Function to display score in a popup
    function displayScorePopup(score) {
        // Show the popup
        $("#popup").fadeIn();
        $("#scoreDisplay").text(`Your score: ${score}%`);
        setTimeout(function () {
            $("#popup").fadeOut();
            window.location.href = "/tutor/dashboard/"; 
        }, 5000);
    }

    // Modify the storeScoreToDatabase function
    function storeScoreToDatabase(score) {
        $.ajax({
          type: 'POST',
          url: '/tutor/quiz/',
          data: {
            quiz_result: score,
            csrfmiddlewaretoken: getCookie('csrftoken')
          },
          success: function (response) {
            // Reset the form after successful submission
            $('#quizForm')[0].reset();
            $("#quiz").hide();
            $("#timer").hide();
            $('.instruction').hide();
            $('#completionMessage').toggle();

      
            // Disable the finish button to prevent further submissions
            $("#finishBtn").prop('disabled', true);
            window.onbeforeunload = null;
          },

          error: function (error) {
            alert('Error storing score:', error);
          }
        });
      }
    // Function to get CSRF token from cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
