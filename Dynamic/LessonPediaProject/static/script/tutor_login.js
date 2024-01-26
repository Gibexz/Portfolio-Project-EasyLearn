$(document).ready(function () {
    $('.closeModal').click(function () {
        $('.modal').hide();
    });
    // Show forgot password form
    $('#forgotPasscode').click(function () {
        $('.forgot_password').show();
        $('.closeModal').click(function () {
            $('.forgot_password').hide();
        });
    });

    // Handle "Forgot Password" form submission
    $('#forgotPasswordForm').submit(function (e) {
        e.preventDefault();
        let form = $(this);
        $('#loadingMessage').show();
        let user_email = $('#forgotPasswordForm input[name="email"]').val();
        let formData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: '{% url "tutor_forgot_password" %}',
            data: formData,
            success: function (response) {
                    if (response.success) {
                        $('#loadingMessage').hide();
                        $('#emailSentModalForm input[name="tutor_email"]').val(user_email);
                        $('#resetPasswordForm input[name="tutor_email"]').val(user_email);
                        $('#emailSentModal').show();
                        $('.closeModal, .continue').click(function () {
                            $('#emailSentModal, #emailErrorModal').hide();
                        });
                        form.trigger('reset');
                    }
                    else {
                        $('#emailErrorModal').show();
                        // Close modal when elements are clicked
                        $('#loadingMessage').hide();
                        $('.closeModal').click(function () {
                            $('#emailSentModal, #emailErrorModal').hide();
                            form.prop('disabled', false);
                        });
                    }
                },
            error: function () {
                $('#loadingMessage').hide();
                form.prop('disabled', false);
            },
            complete: function () {
                // Re-enable the form after the request is complete
                form.prop('disabled', false);
            },
        });
    });

    // Handle "Continue" button in "Email Sent Modal"
    $('#emailSentModalForm').submit(function (e) {
        e.preventDefault();
        let form = $(this);
        let formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '{% url "tutor_reset_token" %}',
            data: formData,
            success: function (response) {
                if (response.success) {
                    // If token is confirmed, show the reset password form
                    form.trigger('reset');
                    $('.reset_password').show();
                } else {
                    // Handle error case (you can customize this part)
                    $('#emailErrorModal').show();
                    // Close modal when elements are clicked
                    $('#loadingMessage').hide();
                    $('.closeModal').click(function () {
                        $('#emailSentModal, #emailErrorModal').hide();
                    });
            }
            },
            error: function () {
                // Handle AJAX error (you can customize this part)
                $('#emailErrorModal').show();
                // Close modal when elements are clicked
                $('#loadingMessage').hide();
                $('.closeModal').click(function () {
                    $('#emailSentModal, #emailErrorModal').hide();
                });
            }
        });
    });

    // Handle "Reset Password" form submission
    $('#resetPasswordForm').submit(function (e) {
        e.preventDefault();
        let formData = $(this).serialize();
        let form = $(this);

        $.ajax({
            type: 'POST',
            url: '{% url "tutor_reset_password" %}',
            data: formData,
            success: function (response) {
                if (response.success) {
                    form.trigger('reset');
                    // If password is reset successfully, redirect to login
                    window.location.href = '{% url "tutor_login" %}';
                } else {
                    // Handle error case (you can customize this part)
                    $('#emailErrorModal').show();
                    // Close modal when elements are clicked
                    $('#loadingMessage').hide();
                    $('.closeModal').click(function () {
                        $('#emailSentModal, #emailErrorModal').hide();
                        form.prop('disabled', false);
                    });
            }
            },
            error: function () {
                // Handle AJAX error (you can customize this part)
                $('#emailErrorModal').show();
                // Close modal when elements are clicked
                $('#loadingMessage').hide();
                $('.closeModal').click(function () {
                    $('#emailSentModal, #emailErrorModal').hide();
                    form.prop('disabled', false);
                });
            }
        });
    });
});