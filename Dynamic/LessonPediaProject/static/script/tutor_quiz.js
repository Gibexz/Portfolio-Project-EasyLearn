$(document).ready(function () {
    // Quiz finish button click event
    $("#finishBtn").on("click", function () {
        calculateScoreAndRedirect();
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
    var timeLeft = 20; // 1 minute in seconds
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
        $("#quiz_result").val(score)
        storeScoreToDatabase(score);
        displayScorePopup(score);
        setTimeout(function () {
            window.location.href = "/tutor/dashboard";
        }, 8000);
    }

    // Function to calculate the score based on selected answers
    function calculateScore() {
        var totalQuestions = 10; // Total number of questions
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
        return scorePercentage.toFixed(2); // Return the score percentage with two decimal places
    }
    // Function to display score in a popup
    function displayScorePopup(score) {
        // Show the popup
        $("#popup").fadeIn();
    
        // Display the score and redirect message
        $("#scoreDisplay").text(`Your score: ${score}%`);
    
        // Hide the popup after 5 seconds and redirect
        setTimeout(function () {
            $("#popup").fadeOut();
            window.location.href = "/tutor/dashboard/"; // Redirect to dashboard
        }, 5000);
    }

    // Function to store the score in the database (This should be handled server-side)
    // Modify the storeScoreToDatabase function
    function storeScoreToDatabase(score) {
        $.ajax({
            type: 'POST',
            url: '/tutor/tutorQuiz/', // Replace with your actual URL
            data: {
                quiz_result: score,
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (response) {
                alert('Score stored in the database');
            },
            error: function (error) {
                alert('Error storing score:', error);
            }
        });
    }

    // Check if the page is reloaded (not on the first access)
    if (performance.navigation.type === 1) {
        $("#finishBtn").trigger("click");
        setTimeout(function () {
            window.location.href = "/tutor/dashboard/"; 
        }, 10000);
    }
});
