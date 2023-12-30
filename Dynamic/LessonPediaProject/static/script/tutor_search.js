$(document).ready(function () {
    // Show the search results modal
    $('#searchResultsModal').show();

    // Function to close the search results modal
    function closeSearchResultsModal() {
        $('#searchResultsModal').hide();
    }

    let subjectName = "";
let popoverTrigger = $(".popover-trigger");
let popoverContent = $("#popover-content");
let searchForm = $(".search_bar_form");

// Click handler for list items
$('.checkValue').click(function () {
    subjectName = $(this).text();
    $('.checkValue').removeClass('popover-trigger');
    $(this).addClass('popover-trigger');
    performAjaxQuery();
});

// Click handler for popover trigger
popoverTrigger.click(function (e) {
    e.preventDefault();
    performAjaxQuery();
});

function performAjaxQuery() {
    let searchQuery = searchForm.find("input[name='query']").val().trim();
    if (searchQuery === "") {
        searchQuery = subjectName;
    }
    subjectName = "";

    if (searchQuery !== "") {
        $.ajax({
            type: 'GET',
            url: '/tutor/searchTutors/',
            data: {query: searchQuery},
            success: function (data) {
                updatePopoverContent(data);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
}


    // Close popover when clicking outside the popover
    $(document).click(function (event) {
        if (!popoverTrigger.is(event.target) && !popoverContent.is(event.target) && popoverContent.has(event.target).length === 0) {
            popoverContent.slideUp();
        }
    });

    // Function to update the popover content
    function updatePopoverContent(data) {
        // Clear previous content
        popoverContent.empty();

        // Add new content based on the JSON data
        popoverContent.append('<h2>Search Results for "' + data.query + '"</h2>');
        
        
        if (data.tutors.length > 0) {
            let tutors_count = data.tutors.length;
            popoverContent.append('<h3>Tutors: ' + '<span style="color: blue; font-size: 24px">' + tutors_count + '</span>' + '</h3>');
            popoverContent.append('<div class="tutor_row" id="flex_tutor_row">');

            data.tutors.forEach(function(tutor) {
                // Create tutor_overview div for each tutor
                var tutorOverview = $('<div class="tutor_overview"></div>');

                // Append tutor image box
                tutorOverview.append('<section class="tutor_image_box">' +
                    '<img class="tutor_image" src="' + tutor.profile_picture + '" alt="' + tutor.first_name + '\'s photo">' +
                    '</section>');

                // Append other_info div
                // tutorOverview.append('<div class="other_info">' +
                // '<section class="tutor_name">');
                
            
            // Adjust the rank display based on the rank value
                if (tutor.rank) {
                    if (tutor.rank > 4) {
                        tutorOverview.append('<center>' + '<h5 class="name" style="display: inline-block; margin: 0px auto;">' + tutor.first_name + ' ' + tutor.last_name + ' &nbsp;</h5>' + '<span class="rank_5" id="my_rank">★★★★★</span>'+ '</center>');
                    } else if (tutor.rank > 3) {
                        tutorOverview.append('<center>' + '<h5 class="name" style="display: inline-block; margin: 0px auto;">' + tutor.first_name + ' ' + tutor.last_name + ' &nbsp;</h5>' + '<span class="rank_4" id="my_rank">★★★★</span><span class="empty_rank">★</span>'+ '</center>');
                    } else if (tutor.rank > 2) {
                         tutorOverview.append('<center>' + '<h5 class="name" style="display: inline-block; margin: 0px auto;">' + tutor.first_name + ' ' + tutor.last_name + ' &nbsp;</h5>' + '<span class="rank_3" id="my_rank">★★★</span><span class="empty_rank">★★</span>'+ '</center>');
                    } else if (tutor.rank > 1) {
                         tutorOverview.append('<center>' + '<h5 class="name" style="display: inline-block; margin: 0px auto;">' + tutor.first_name + ' ' + tutor.last_name + ' &nbsp;</h5>' + '<span class="rank_2" id="my_rank">★★</span><span class="empty_rank">★★★</span>'+ '</center>');
                    } else {
                         tutorOverview.append('<center>' + '<h5 class="name" style="display: inline-block; margin: 0px auto;">' + tutor.first_name + ' ' + tutor.last_name + ' &nbsp;</h5>' + '<span class="rank_1" id="my_rank">★</span><span class="empty_rank">★★★★</span>'+ '</center>');
                    }
                } else {
                     tutorOverview.append('<center>' + '<h5 class="name" style="display: inline-block; margin: 0px auto;">' + tutor.first_name + ' ' + tutor.last_name + ' &nbsp;</h5>' + '<span class="rank_1" id="my_rank">★</span><span class="empty_rank">★★★★</span>'+ '</center>');
                }

                tutorOverview.append('</section>' +
                    '<section class="tutor_subject">' +
                    '<h6 class="show_block">' + tutor.primary_subject + '<i class="fa fa-circle" aria-hidden="true"></i></h6>' +
                    '</section>' +
                    '<section>' + '<center>' +
                    '<button class="view_tutor_profile"><a href="/tutor/tutorDetail/' + tutor.id + '">View Profile</a></button>' + '</center>' +
                    '</section>' +
                    '</div>');

                // Append tutor_overview to tutor_row
                popoverContent.find('.tutor_row').append(tutorOverview);
            });

            popoverContent.append('</div>');
        } else {
            popoverContent.append('<p>No tutors found for "' + data.query + '"</p>');
        }

        if (data.subjects.length > 0) {
            let subjects_count = data.subjects.length;
            popoverContent.append('<div class="subject_row">');
            popoverContent.append('<h3>Subjects: ' + subjects_count+ '</h3>');
            data.subjects.forEach(function(subject) {
                tutors = data.tutors.slice()
                console.log(subject);
                popoverContent.append('<div class="subject_overview">');
                popoverContent.append('<section class="subject_name">');
                popoverContent.append('<h5>' + subject.subject_name + '</h5>');
                popoverContent.append('</section>');
                popoverContent.append('</div>');
            });
            popoverContent.append('</div>');
        } else {
            popoverContent.append('<p>No subjects found for "' + data.query + '"</p>');
        }

        // Toggle visibility of the popover content
        popoverContent.slideToggle();
    }
});
