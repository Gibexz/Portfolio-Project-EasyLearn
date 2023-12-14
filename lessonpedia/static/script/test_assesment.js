$(document).ready(function() {
    const quizForm = $('#quizForm');
    const finishBtn = $('#finishBtn');
    const quizDuration = 5 * 60; // 1 minute in seconds

    let score = 0;
    let timer;

    // Define answer keys for English and Abstract questions
    const englishAnswers = {
      englishQ1: 'Fearful',
      englishQ2: 'Children',
      englishQ3: 'Joyful',
      englishQ4: 'Ate',
      englishQ5: 'Mad'
    };

    const abstractAnswers = {
      abstractQ1: '10',
      abstractQ2: 'Hexagon',
      abstractQ3: '25',
      abstractQ4: '48',
      abstractQ5: '□'
    };

    // Function to calculate score
    function calculateScore() {
      score = 0;

      // Check English question answers
      $.each(englishAnswers, function(question, answer) {
        const selectedAnswer = $('input[name=' + question + ']:checked').val();
        if (selectedAnswer === answer) {
          score++;
        }
      });

      // Check Abstract question answers
      $.each(abstractAnswers, function(question, answer) {
        const selectedAnswer = $('input[name=' + question + ']:checked').val();
        if (selectedAnswer === answer) {
          score++;
        }
      });
    }

    // Function to display score in a popup and redirect to dashboard
    function displayScore() {
      calculateScore();
      const totalQuestions = Object.keys(englishAnswers).length + Object.keys(abstractAnswers).length;
      const percentageScore = ((score / totalQuestions) * 100).toFixed(2);
      alert(`Your score is: ${percentageScore}%`);
      redirectToDashboard();
    }

    // Redirect to dashboard.com
    function redirectToDashboard() {
      window.location.href = 'https://dashboard.com';
    }

    // Timer function
    function startTimer(duration, display) {
      let timer = duration;
      let interval = setInterval(function() {
        let minutes = parseInt(timer / 60, 10);
        let seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;

        display.textContent = minutes + ':' + seconds;

        if (--timer < 0) {
          clearInterval(interval);
          displayScore();
        }
      }, 1000);
    }

    // Finish button click event
    finishBtn.click(function() {
      clearInterval(timer);
      displayScore();
      localStorage.removeItem('testScore'); // Clear the score upon completion

      // Override the default 'leave site' confirmation dialog
    //   window.onbeforeunload = function() {
        // Empty function to prevent the dialog
    //   };
    });

    // On page load or back button click
    $(window).on('beforeunload', function() {
      // Store the score in local storage before leaving the page
      localStorage.setItem('testScore', score);
      return null;
    });

    // Retrieve stored score if available on user-initiated page load
    $(window).on('load', function() {
      const storedScore = localStorage.getItem('testScore');
      if (storedScore !== null && performance.navigation.type === 1) {
        alert(`Your previous score was: ${storedScore}%`);
        redirectToDashboard();
      }
    });

    // Start timer when the page loads for the first time
    if (localStorage.getItem('testScore') !== null && performance.navigation.type === 0) {
      const timerDisplay = document.createElement('span');
      $(timerDisplay).css({
        'position': 'fixed',
        'top': '10px',
        'right': '10px',
        'padding': '5px',
        'background': '#fff',
        'border': '1px solid #ccc',
        'border-radius': '5px',
        'font-size': '18px'
      });
      $('body').append(timerDisplay);
      startTimer(quizDuration, timerDisplay);
    }
  });

  // Modify the storeScoreToDatabase function
// function storeScoreToDatabase(score) {
//     $.ajax({
//         type: 'POST',
//         url: '/store_score/', // Replace with your actual URL
//         data: {
//             csrfmiddlewaretoken: '{{ csrf_token }}', // Add CSRF token for security (Django template syntax)
//             score: score
//         },
//         success: function (response) {
//             console.log('Score stored in the database');
//         },
//         error: function (error) {
//             console.error('Error storing score:', error);
//         }
//     });
// }