
    $(document).ready(function () {
        // Initialize variables
        let notificationBox = $("#notification-box");
        let bellIcon = $(".fa-bell");

        // Hide the notification box initially

        // Function to show/hide the notification box
        function toggleNotificationBox() {
            notificationBox.slideToggle();
        }

        // Function to hide the notification box after a delay
        function hideNotificationBox() {
            setTimeout(function () {
                notificationBox.slideUp();
            }, 3000);
        }

        // Bell icon click event
        bellIcon.click(function (e) {
            e.stopPropagation();
            toggleNotificationBox();

            hideNotificationBox();
        });

        // Document click event to hide the notification box
        $(document).click(function () {
            notificationBox.slideUp();
        });

        $('.dashboardBtn').click(function (event) {
            event.stopPropagation();
            $('.dropdownContainerTop').toggle();
        });
        $(document).click(function () {
            $('.dropdownContainerTop').hide();
        });


        // Function to show/hide the open to work status
        $('.fa-circle').hover(
            function() {
                // Mouse enter
                let statusText = $(this).parent('.show_block').data('status-text');
                $(this).parent('.show_block').append('<div class="status-text">' + statusText + '</div>');
            },
            function() {
                // Mouse leave
                $(this).parent('.show_block').find('.status-text').remove();
            }
        );
    });
