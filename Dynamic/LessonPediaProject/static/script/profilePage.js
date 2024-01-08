$(document).ready(function() {
    $('#dp').change(function() {
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

    var primarySelection = [
        "-- select one --",
        "Primary 1",
        "Primary 2",
        "Primary 3",
        "Primary 4",
        "Primary 5",
        "Primary 6",
    ]

    var secondarySelection = [
        "-- select one --",
        "JSS 1",
        "JSS 2",
        "JSS 3",
        "SSS 1",
        "SSS 2",
        "SSS 3",
    ]

    var tertiarySelection = [
        "-- select one --",
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
        "-- select one --",
        "PgD",
        "Masters",
        "PhD",
        "Others",
    ]


    // Overwrite the default select option
    $("#specifics").empty()
    $("#specifics").append('<option value="">Select Educational Level</option>')
    // Hangle dynamical dropdown
    $('#eduLevel').change(function() {
        var selected = $(this).val();
        var dropdwn = $('#specifics')
        dropdwn.empty()
        if (selected == "Primary"){
            primarySelection.forEach(element => {
                dropdwn.append('<option value="' + element + '">' + element + '</option>')
            });
        } else if (selected == "Secondary"){
            secondarySelection.forEach(element => {
                dropdwn.append('<option value="' + element + '">' + element + '</option>')
            });
        } else if (selected == "Tertiary"){
            tertiarySelection.forEach(element => {
                dropdwn.append('<option value="' + element + '">' + element + '</option>')
            });
        } else if (selected == "Others"){
            others.forEach(element => {
                dropdwn.append('<option value="' + element + '">' + element + '</option>')
            });
        } else {
            dropdwn.append('<option value="">Select Educational Level</option>')
        }
    });
});
