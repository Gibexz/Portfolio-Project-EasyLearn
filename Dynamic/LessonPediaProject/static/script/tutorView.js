$(document).ready(function () {
    const tutorsContainer = $('#similarTutors .similarTutors_body');
    const tutorItems = $('.similarTutors_body_div');
    const numToShow = 5;
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
        tutorItems.fadeOut(300);
        showTutors();
    });

    $('#prevArrow').click(function () {
        currentIndex -= numToShow;
        if (currentIndex < 0) {
            currentIndex = Math.floor(tutorItems.length / numToShow) * numToShow;
        }
        tutorItems.fadeOut(500);
        showTutors();
    });
});