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
});
