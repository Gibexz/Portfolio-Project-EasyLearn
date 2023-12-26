$(document).ready(function() {
    $('#pic').change(function() {
        var valid_extensions = ['.jpg', '.jpeg', '.png'];

        const fileInput = this;
        const file_name = $(fileInput).val();

        var isValidExtension = false;

        $.each(valid_extensions, function (indexInArray, valueOfElement) {
            if (file_name.endsWith(valueOfElement)) {
                isValidExtension = true;
                return false;
            }
        });

        if (isValidExtension) {
            var file = fileInput.files[0];
            var previewImage = $('.image_preview');
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            })

            setTimeout(() => {
                window.scrollTo({
                    top: document.body.scrollHeight,
                    behavior: "smooth"
                })
            }, 3000);

            if (file) {
                var reader = new FileReader();

                reader.onload = function(e) {
                    previewImage.attr('src', e.target.result);
                };

                reader.readAsDataURL(file);
                previewImage.show();
            } else {
                previewImage.attr('src', '');
                previewImage.hide();
            }
        } else {
            alert('Invalid file extension. Please choose a valid image file.');
        }
    });


    // certificate validation
    $('#cert').change(function() {
        var valid_extensions = ['.jpg', '.jpeg', '.png'];
        
        const fileInput = this;
        const file_name = $(fileInput).val();

        var isValidExtension = false;

        $.each(valid_extensions, function (indexInArray, valueOfElement) {
            if (file_name.endsWith(valueOfElement)) {
                isValidExtension = true;
                return false;
            }
        });

        if (isValidExtension) {
            $('#view_cert').click(function(){
                var file = fileInput.files[0];
                var previewImage = $('#preview_cert');
                window.scrollTo({
                    top: 0,
                    behavior: "smooth"
                });
                $('.set_cert_display').show()
                $('body').css("overflow", "hidden")

                if (file) {
                    var reader = new FileReader();

                    reader.onload = function(e) {
                        previewImage.attr('src', e.target.result);
                    };

                    reader.readAsDataURL(file);
                    previewImage.show();
                } else {
                    previewImage.attr('src', '');
                    previewImage.hide();
                }
            })
            
        } else {
            alert('Invalid file extension. Please choose a valid image file.');
        }
    });

    // Resume or Cv validation
    $('#cv').change(function() {
        var valid_extensions = ['.pdf'];
        const fileInput = this;
        const file_name = $(fileInput).val();

        if (valid_extensions.some(ext => file_name.endsWith(ext))) {
            $('#view_cv').click(function(){
                var file = fileInput.files[0];

                var reader = new FileReader();
                reader.onload = function() {
                    var dataUri = this.result;

                    // Display the PDF using the data URI
                    $('#pdfViewer').attr('src', dataUri);
                    window.scrollTo({
                        top: 0,
                        behavior: "smooth"
                    });

                    $('body').css("overflow", "hidden")
                    $('.set_cv_display').show()
                };

                reader.readAsDataURL(file);
            })     
        } else {
            alert('Invalid file extension. Please choose a valid PDF file.');
        }
    });

    // close cert preview page
    $(".close_cert").click(function(){
        $('.set_cert_display').hide()
        $('body').css("overflow", "auto")
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: "smooth"
        });
    })

    // close cv preview page
    $(".close_cv").click(function(){
        $('.set_cv_display').hide()
        $('body').css("overflow", "auto")
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: "smooth"
        });
    })


    // nationality dropdown

    $("#nationality").on('change', function() {
        // Check if the selected nationality is not Nigerian
        if ($(this).val() !== 'NG') {
          $('#state').hide();
          $('div .lga').hide();
          $(".state input[type='text']").show();
          $('.lga_frn').show();
        } else {
            $('.location').css({
                'justify-content': 'flex-start',
            })
          $('#state').show(); // Show the state div
          $(".state input[type='text']").hide(); // Hide the text input
          $('div .lga').show();
            $('.lga_frn').hide();
        }
      });

         // Calculate the minimum date for someone who is 75 years old
    let maxDate = new Date();
    maxDate.setFullYear(maxDate.getFullYear() - 75);
    let formattedMaxDate = maxDate.toISOString().split('T')[0];

    // Calculate the maximum date for someone who is 15 years old
    let minDate = new Date();
    minDate.setFullYear(minDate.getFullYear() - 15);
    let formattedMinDate = minDate.toISOString().split('T')[0];

    // Set the min and max attributes of the input element
    $('#dob').attr('max', formattedMinDate);
    $('#dob').attr('min', formattedMaxDate);

    // cv_preview and certificate_preview
        // Initially hide the preview elements
    $('.cv_preview').hide();
    $('.cert_preview').hide();

    // Show CV preview when the "View CV" link is clicked
    $('#view_cv').click(function() {
        $('.cv_preview').toggle();
    });

    $('#view_cert').click(function() {
        $('.cert_preview').toggle();
    });
});
