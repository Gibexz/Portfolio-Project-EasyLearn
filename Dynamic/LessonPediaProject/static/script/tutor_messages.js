$(document).ready(function () {
    function closeFlash() {
        setTimeout(function() {
          $(".flash-container").fadeOut(500);
        }, 5000);
      };
      closeFlash();
});