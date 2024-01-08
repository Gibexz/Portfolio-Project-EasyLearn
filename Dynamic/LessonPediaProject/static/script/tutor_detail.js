$(document).ready(function () {

    // Show all subjects
    $('#allSubjectsBtn').click(function () {
    $('#allSubjectsView').show();
    $('.closeModal, .continue').click(function () {
        $('#allSubjectsView, #allScheduleView').hide();
    });
    });
    

    // Show all schedule
    $('.allScheduleBtn').click(function () {
        $('#allScheduleView').show();
        $('.closeModal, .continue').click(function () {
            $('#allSubjectsView, #allScheduleView').hide();
        });
        });

    // dashboard dropdown toggling
    $('.dashboardBtn').click(function (event) {
        event.stopPropagation(); // Prevent the click event from reaching document
        $('.dropdownContainerTop').toggle();
    });
    $(document).click(function () {
        $('.dropdownContainerTop').hide();
    });

    // Pagination
    const tutorItems = $('.tutor_row .tutor_overview');
    const numPerPage = 4;
    let currentPage = 1;

    function showTutors(startIndex) {
        const endIndex = startIndex + numPerPage;
        tutorItems.hide().slice(startIndex, endIndex).fadeIn(500);
        updatePaginationButtons();
    }

    function updatePaginationButtons() {
        const totalPages = Math.ceil(tutorItems.length / numPerPage);
        const pageButtons = $('#pageButtons');
        pageButtons.empty();

        for (let i = 1; i <= totalPages; i++) {
            const button = $(`<button>${i}</button>`);
            button.click(function () {
                currentPage = i;
                const startIndex = (currentPage - 1) * numPerPage;
                showTutors(startIndex);
                updateActiveButton();
            });
            pageButtons.append(button);
        }

        $('#currentPage').text(`Page ${currentPage}`);
        updateActiveButton();
    }

    function updateActiveButton() {
        $('#pageButtons button').removeClass('activeBtn');
        $(`#pageButtons button:nth-child(${currentPage})`).addClass('activeBtn');
    }

    // Initial display
    showTutors(0);

    $('#nextPage').click(function () {
        if (currentPage < Math.ceil(tutorItems.length / numPerPage)) {
            currentPage += 1;
            const startIndex = (currentPage - 1) * numPerPage;
            showTutors(startIndex);
            updateActiveButton();
        }
    });

    $('#prevPage').click(function () {
        if (currentPage > 1) {
            currentPage -= 1;
            const startIndex = (currentPage - 1) * numPerPage;
            showTutors(startIndex);
            updateActiveButton();
        }
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
        $(this).hide();
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
    
    $('#submitRankBtn').click(function () {
        $('#rankForm').hide();
        $('.rankTutorDisplay').show();
    })

    // goRight items, likes, email, more
    $(".fa-heart").click(function () {
        $(this).toggleClass("heart-red");
    });

    // Email icon click
    $(".fa-envelope").click(function (e) {
        e.stopPropagation(); // Prevent the click event from reaching the document click handler
        $(".email-form").toggle();
        $(".dropdownContainer").hide(); // Hide dropdownContainer if it's open
    });

    // Ellipsis icon click
    $(".fa-ellipsis-h").click(function (e) {
        e.stopPropagation(); // Prevent the click event from reaching the document click handler
        $(".dropdownContainer").toggle();
        $(".email-form").hide(); // Hide email form if it's open
    });

    // Document click to close email form and dropdownContainer
    $(document).click(function (event) {
        if (!$(event.target).closest(".email-form").length && !$(event.target).closest(".dropdownContainer").length) {
            // Close the email form and dropdown
            $(".email-form").hide();
            $(".dropdownContainer").hide();
        }
    });
    

    // dropdownContainer item click (example: Engage tutor)
    $(".dropdownContainer").on("click", ".", function () {
        // Add logic for the Engage Tutor action
        console.log("Engage Tutor clicked");
    });


    // Handle Ajax request for email
        $("#emailForm").submit(function (e) {
            e.preventDefault();
            const form = $(this);
            form.toggle();
    
            // Disable the form to prevent multiple submissions
            form.prop('disabled', true);
    
            $('#loadingMessage').show();
    
            const tutorId = $('#tutorId').val();
    
            $.ajax({
                type: "POST",
                url: `/tutor/emailTutor/${tutorId}/`,
                data: form.serialize(),
                success: function (data) {
                    if (data.success) {
                        $('#loadingMessage').hide();
                        $('#emailSentModal').show();
                        $('.closeModal, .continue').click(function () {
                            $('#emailSentModal, #emailErrorModal').hide();
                        });
                    } else {
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
    
        $(".cancelEmail").click(function () {
            $(".email-form").hide();
        });
    
});