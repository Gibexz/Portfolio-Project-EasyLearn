$(document).ready(function () {
    const tutorsContainer = $('#similarTutors .similarTutors_body');
    const tutorItems = $('.tutor_row');
    const numToShow = 4;
    let currentIndex = 0;

    tutorItems.hide();
    showTutors();

    function showTutors() {
        tutorItems.slice(currentIndex, currentIndex + numToShow).fadeIn(500);
    }

    $('#nextArrow').click(function () {
        currentIndex += numToShow;
        if (currentIndex >= tutorItems.length) {
            currentIndex = 0;
        }
        tutorItems.fadeOut(50);
        showTutors();
    });

    $('#prevArrow').click(function () {
        currentIndex -= numToShow;
        if (currentIndex < 0) {
            currentIndex = Math.floor(tutorItems.length / numToShow) * numToShow;
        }
        tutorItems.fadeOut(50);
        showTutors();
    });

    // active and review toggle
    $('.review_btn').click(function () {
        $('.overview_btn').removeClass('active');
        $('.overview_body').hide();
        $('.link2social').hide();
        $('.review_btn').addClass('active');
        $('.reviews').show();
    });

    $('.overview_btn').click(function () {
        $('.review_btn').removeClass('active');
        $('.reviews').hide();
        $('.link2social').show();
        $('.overview_btn').addClass('active');
        $('.overview_body').show();
    });


    // Rank tutor temporarily

    $('.rankTutorDisplay').click(function () {
        $('#rankForm').toggle();
    });

    $(".star").click(function() {
        var selectedValue = $(this).data('value');
        $(".star").removeClass("gold");
        $(".star").each(function() {
          if ($(this).data('value') <= selectedValue) {
            $(this).addClass("gold");
          }
        });
        $("#rank").val(selectedValue);
      });

    
});