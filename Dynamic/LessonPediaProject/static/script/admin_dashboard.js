$(document).ready(function(){
    $(".check_status").each(function() {
        const value = $(this).text();
        if (value === "Active") {
            $(this).css({
                "border": "1px solid green",
                "background-color": "rgb(205, 243, 209)"
            })
        } else {
            $(this).css({
                "border": "1px solid red",
                "background-color": "rgb(252, 206, 206)"
            })
        }
    });

    $("#set_tutor").click(function(){
        $(".activate_tutors").show()
        $(".activate_learners").hide()
    })
    $("#set_learner").click(function(){
        $(".activate_tutors").hide()
        $(".activate_learners").show()
    })
    

    // Take action dialogue for Tutor
    $('.action').click(function(){
        // const userType = $(this).closest(".activate_tutors, .activate_learners").find(".inner_content .validate").text();

        // $('.selected_user').text(tutorData.username);
        // $('.selected_email').text(tutorData.email)

        const adminName = $(".admin_username").text()
        var tutorData = $(this).data('tutor')

    
        console.log(tutorData); // Check the entire tutorData object
        
        let tutorProfileImage = tutorData.profile_picture

        $('#tutor_profile_image').attr('src', tutorProfileImage);
    
        $('.selected_user').text(tutorData.username);
        $('.profile_userName').text(tutorData.username);
        $('.full_name').text(tutorData.first_name +" "+tutorData.last_name);
        $('.gender').text(tutorData.gender);
        $('.phone_number').text(tutorData.phone_number);
        $('.residential_address').text(tutorData.residential_address);
        $('.state_of_residence').text(tutorData.state_of_residence);
        $('.nationality').text(tutorData.nationality);
        $('.institution_attended').text(tutorData.institution_attended);  // not in the database yet
        $('.area_of_specialization').text(tutorData.area_of_specialization);
        $('.highest_qualification').text(tutorData.highest_qualification);
        $('.gpa').text(tutorData.gpa);
        $('.employment_status').text(tutorData.employment_status);
        $('.employment_type').text(tutorData.employment_type);
        $('.availability').text(tutorData.availability);
        $('.total_clients').text(tutorData.total_clients);
        $('.active_clients').text(tutorData.active_clients);
        $('.rejected_clients').text(tutorData.rejected_clients);
        $('.ranking').text(tutorData.ranking);

    
    
        $('.active_admin').text(adminName);
    
        if (tutorData.hasOwnProperty('email')) {
            // console.log(tutorData.email); // Check if tutorData.email is populated
            $('.selected_email').text(tutorData.email);
        } else {
            console.log('nit accsisble');
        }

        $('.set_action').show()
    })

    $('.close').click(function(){
        $('.set_action').hide()
    })

    // profile, review and report activation logic
    $('#activate_review').click(function(){
        $('.set_other_details').hide()
        $('.set_review_details').show()
        $('.set_report_details').hide()
    })
    $('#activate_profile').click(function(){
        $('.set_other_details').show()
        $('.set_review_details').hide()
        $('.set_report_details').hide()
    })
    $('#activate_report').click(function(){
        $('.set_other_details').hide()
        $('.set_review_details').hide()
        $('.set_report_details').show()
    })

    // account disabling logics
    $('#activate_suspend').click(function(){
        $('.set_action').hide()
        $('.set_disable_account').show()
    })

    $('.disable_close, .mistake').click(function(){
        $('.set_action').show()
        $('.set_disable_account').hide()
    })
});
//  live table sort for tutor admin table list
$(document).ready(function() {
    $('.table_header th').on('click', function() {
        const column = $(this).data('column');
        const $tbody = $('.tutor_table_list tbody');
        const $header = $(this);
        const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

        $('.table_header th').data('direction', '');
        $header.data('direction', direction);

        const rows = $tbody.find('tr').get();
        rows.sort(function(rowA, rowB) {
            const cellA = $(rowA).children('td').eq(column).text().trim().toLowerCase();
            const cellB = $(rowB).children('td').eq(column).text().trim().toLowerCase();

            if (direction === 'ascending') {
                return cellA.localeCompare(cellB);
            } else {
                return cellB.localeCompare(cellA);
            }
        });

        $.each(rows, function(index, row) {
            $tbody.append(row);
        });
    });
});


//  live table sort for client admin table list
$(document).ready(function() {
    $('.table_header_learner th').on('click', function() {
        const column = $(this).data('column');
        const $tbody = $('.learner_table_list tbody');
        const $header = $(this);
        const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

        $('.table_header_learner th').data('direction', '');
        $header.data('direction', direction);

        const rows = $tbody.find('tr').get();
        rows.sort(function(rowA, rowB) {
            const cellA = $(rowA).children('td').eq(column).text().trim().toLowerCase();
            const cellB = $(rowB).children('td').eq(column).text().trim().toLowerCase();

            if (direction === 'ascending') {
                return cellA.localeCompare(cellB);
            } else {
                return cellB.localeCompare(cellA);
            }
        });

        $.each(rows, function(index, row) {
            $tbody.append(row);
        });
    });

});

$(document).ready(function() {

    const api_url = 'http://127.0.0.1:8000/appAdmin'

    // Username api
    $.getJSON(`${api_url}/api/get_admin_username/`, function(data) {
        $('#admin_username').text(data.username);
    });

    // TUTORS ==========================================================
    // Total tutor count api
    function updateTutorCount() {
        $.getJSON(`${api_url}/api/get_tutor_count/`, function(data) {
            $("#tutorCount").text(data.tutor_count);
        });
    }

    updateTutorCount();

    setInterval(updateTutorCount, 100000);
    
    // Active tutor count api
    function activeTutorNos() {
        $.getJSON(`${api_url}/api/get_nos_active_tutors/`, function(data) {
            $('#activeTutors').text(data.active_tutor_count);
        }); 
    }
    activeTutorNos();

    setInterval(activeTutorNos, 1080000);


    // Iacctive tutor count api
    function inactiveTutorNos() {
        $.getJSON(`${api_url}/api/get_nos_inactive_tutors/`, function(data) {
            $('#inactiveTutors').text(data.inactive_tutor_count);
        }); 
    }
    inactiveTutorNos();

    setInterval(inactiveTutorNos, 1080000);


    // CLIENTS =============================================================
    // Total client count api
    function updateClientCount() {
        $.getJSON(`${api_url}/api/get_client_count/`, function(data) {
            $('#clientCount').text(data.client_count);
        });
    }
    updateClientCount();

    setInterval(updateClientCount, 100000);
    
    // Total active client count api
    function activeClientCount() {
        $.getJSON(`${api_url}/api/get_nos_active_clients/`, function(data) {
            $('#activeClient').text(data.active_client_count);
        });
    }
    activeClientCount();

    setInterval(activeClientCount, 1080000);
    

    // Iacctive client count api
    function inactiveClientNos() {
        $.getJSON(`${api_url}/api/get_nos_inactive_clients/`, function(data) {
            $('#inactiveClients').text(data.inactive_client_count);
        }); 
    }
    inactiveClientNos();

    setInterval(inactiveClientNos, 1080000);

}) 

//     var tutorRows = $('.tutor_table_list tbody tr');
//     var tutorRowsPerPage = 1;
//     var tutorTotalPages = Math.ceil(tutorRows.length / tutorRowsPerPage);
//     var tutorCurrentPage = 1;
//     var tutorPaginatedView = true;
//     var tutorStoredPage = 1; // Store the current page before showing all rows

//     function showTutorPage(page) {
//         tutorRows.hide();
//         tutorRows.slice((page - 1) * tutorRowsPerPage, page * tutorRowsPerPage).show();
//     }

//     function setupTutorPagination() {
//         var tutorPageNumbers = '';
//         var maxVisiblePages = 5; // Maximum visible page numbers
//         var totalPages = tutorTotalPages;
//         var startPage = 1;
//         var endPage = totalPages;

//         if (totalPages > maxVisiblePages) {
//             if (tutorCurrentPage > Math.floor(maxVisiblePages / 2)) {
//                 startPage = tutorCurrentPage - Math.floor(maxVisiblePages / 2);
//                 endPage = startPage + maxVisiblePages - 1;
//                 if (endPage > totalPages) {
//                     endPage = totalPages;
//                     startPage = endPage - maxVisiblePages + 1;
//                 }
//             } else {
//                 endPage = maxVisiblePages;
//             }
//         }

//         if (startPage > 1) {
//             tutorPageNumbers += `<button class="tutor-page-number" data-page="1">1</button>`;
//             if (startPage > 2) {
//                 tutorPageNumbers += `<span>...</span>`;
//             }
//         }

//         for (var i = startPage; i <= endPage; i++) {
//             tutorPageNumbers += `<button class="tutor-page-number" data-page="${i}">${i}</button>`;
//         }

//         if (endPage < totalPages) {
//             if (endPage < totalPages - 1) {
//                 tutorPageNumbers += `<span>...</span>`;
//             }
//             tutorPageNumbers += `<button class="tutor-page-number" data-page="${totalPages}">${totalPages}</button>`;
//         }

//         $('#tutorPageNumbers').html(tutorPageNumbers);
//     }

//     function updateTutorPaginationButtons() {
//         if (tutorCurrentPage === 1) {
//             $('#tutorPrevPage, #tutorFirstPage').prop('disabled', true);
//         } else {
//             $('#tutorPrevPage, #tutorFirstPage').prop('disabled', false);
//         }
//         if (tutorCurrentPage === tutorTotalPages) {
//             $('#tutorNextPage, #tutorLastPage').prop('disabled', true);
//         } else {
//             $('#tutorNextPage, #tutorLastPage').prop('disabled', false);
//         }
//     }

//     showTutorPage(tutorCurrentPage);
//     setupTutorPagination();
//     updateTutorPaginationButtons();

//     // Click handlers...
//     // Click handler for specific page number
//     $('#tutorPageNumbers').on('click', '.tutor-page-number', function() {
//         tutorCurrentPage = parseInt($(this).data('page'));
//         showTutorPage(tutorCurrentPage);
//         updateTutorPaginationButtons();
//     });

//     // Click handler for first page
//     $('#tutorFirstPage').on('click', function() {
//         tutorCurrentPage = 1;
//         showTutorPage(tutorCurrentPage);
//         updateTutorPaginationButtons();
//     });

//     // Click handler for last page
//     $('#tutorLastPage').on('click', function() {
//         tutorCurrentPage = tutorTotalPages;
//         showTutorPage(tutorCurrentPage);
//         updateTutorPaginationButtons();
//     });

//     // Click handler for previous page
//     $('#tutorPrevPage').on('click', function() {
//         if (tutorCurrentPage > 1) {
//             tutorCurrentPage--;
//             showTutorPage(tutorCurrentPage);
//             updateTutorPaginationButtons();
//         }
//     });

//     // Click handler for next page
//     $('#tutorNextPage').on('click', function() {
//         if (tutorCurrentPage < tutorTotalPages) {
//             tutorCurrentPage++;
//             showTutorPage(tutorCurrentPage);
//             updateTutorPaginationButtons();
//         }
//     });

//     // Click handler for 'All' / 'Back to Pagination' button
//     $('#tutorShowAll').on('click', function() {
//         if (tutorPaginatedView) {
//             tutorStoredPage = tutorCurrentPage;
//             tutorRows.show();
//             $('#tutorShowAll').text('Back to Pagination');
//             $('#tutorPageNumbers').empty();
//             $('#tutorPrevPage, #tutorNextPage, #tutorFirstPage, #tutorLastPage').prop('disabled', true);
//             tutorPaginatedView = false;
//         } else {
//             tutorRows.hide();
//             showTutorPage(tutorStoredPage);
//             setupTutorPagination();
//             updateTutorPaginationButtons();
//             $('#tutorShowAll').text('All');
//             tutorPaginatedView = true;
//         }
//     });

// });

$(document).ready(function() {
    var tutorRows = $('.tutor_table_list tbody tr');
    var tutorRowsPerPage = 1;
    var tutorTotalPages = Math.ceil(tutorRows.length / tutorRowsPerPage);
    var tutorCurrentPage = 1;
    var tutorPaginatedView = true;
    var tutorStoredPage = 1; // Store the current page before showing all rows

    function showTutorPage(page) {
        tutorRows.hide();
        tutorRows.slice((page - 1) * tutorRowsPerPage, page * tutorRowsPerPage).show();
    }

    function updateTutorPagination() {
        var maxPagesToShow = 5; // Number of page numbers to display
        var tutorPageNumbers = '';
        var startPage = 1;
        var endPage = Math.min(tutorTotalPages, maxPagesToShow);

        if (tutorTotalPages > maxPagesToShow) {
            if (tutorCurrentPage > Math.floor(maxPagesToShow / 2)) {
                startPage = tutorCurrentPage - Math.floor(maxPagesToShow / 2);
                endPage = tutorCurrentPage + Math.floor(maxPagesToShow / 2);
                if (endPage > tutorTotalPages) {
                    endPage = tutorTotalPages;
                    startPage = endPage - maxPagesToShow + 1;
                }
            }
        }

        for (var i = startPage; i <= endPage; i++) {
            tutorPageNumbers += `<button class="tutor-page-number" data-page="${i}">${i}</button>`;
        }
        $('#tutorPageNumbers').html(tutorPageNumbers);
    }

    function updateTutorPaginationButtons() {
        $('#tutorPrevPage, #tutorFirstPage').prop('disabled', tutorCurrentPage === 1);
        $('#tutorNextPage, #tutorLastPage').prop('disabled', tutorCurrentPage === tutorTotalPages);
    }

    showTutorPage(tutorCurrentPage);
    updateTutorPagination();
    updateTutorPaginationButtons();

    // Click handler for specific page number
    $('#tutorPageNumbers').on('click', '.tutor-page-number', function() {
        tutorCurrentPage = parseInt($(this).data('page'));
        showTutorPage(tutorCurrentPage);
        updateTutorPagination();
        updateTutorPaginationButtons();
    });

    // Click handler for first page
    $('#tutorFirstPage').on('click', function() {
        tutorCurrentPage = 1;
        showTutorPage(tutorCurrentPage);
        updateTutorPagination();
        updateTutorPaginationButtons();
    });

    // Click handler for last page
    $('#tutorLastPage').on('click', function() {
        tutorCurrentPage = tutorTotalPages;
        showTutorPage(tutorCurrentPage);
        updateTutorPagination();
        updateTutorPaginationButtons();
    });

    // Click handler for previous page
    $('#tutorPrevPage').on('click', function() {
        if (tutorCurrentPage > 1) {
            tutorCurrentPage--;
            showTutorPage(tutorCurrentPage);
            updateTutorPagination();
            updateTutorPaginationButtons();
        }
    });

    // Click handler for next page
    $('#tutorNextPage').on('click', function() {
        if (tutorCurrentPage < tutorTotalPages) {
            tutorCurrentPage++;
            showTutorPage(tutorCurrentPage);
            updateTutorPagination();
            updateTutorPaginationButtons();
        }
    });

    // Click handler for 'All' / 'Back to Pagination' button
    $('#tutorShowAll').on('click', function() {
        if (tutorPaginatedView) {
            tutorStoredPage = tutorCurrentPage;
            tutorRows.show();
            $('#tutorShowAll').text('Back to Pagination');
            $('#tutorPageNumbers').empty();
            $('#tutorPrevPage, #tutorNextPage, #tutorFirstPage, #tutorLastPage').prop('disabled', true);
            tutorPaginatedView = false;
        } else {
            tutorRows.hide();
            showTutorPage(tutorStoredPage);
            updateTutorPagination();
            updateTutorPaginationButtons();
            $('#tutorShowAll').text('All');
            tutorPaginatedView = true;
        }
    });
});


$(document).ready(function() {
    var clientRows = $('.learner_table_list tbody tr');
    var clientRowsPerPage = 3;
    var clientTotalPages = Math.ceil(clientRows.length / clientRowsPerPage);
    var clientCurrentPage = 1;
    var clientPaginatedView = true;
    var clientStoredPage = 1; // Store the current page before showing all rows

    function showClientPage(page) {
        clientRows.hide();
        clientRows.slice((page - 1) * clientRowsPerPage, page * clientRowsPerPage).show();
    }

    function updateClientPagination() {
        var maxPagesToShow = 5; // Number of page numbers to display
        var clientPageNumbers = '';
        var startPage = 1;
        var endPage = Math.min(clientTotalPages, maxPagesToShow);

        if (clientTotalPages > maxPagesToShow) {
            if (clientCurrentPage > Math.floor(maxPagesToShow / 2)) {
                startPage = clientCurrentPage - Math.floor(maxPagesToShow / 2);
                endPage = clientCurrentPage + Math.floor(maxPagesToShow / 2);
                if (endPage > clientTotalPages) {
                    endPage = clientTotalPages;
                    startPage = endPage - maxPagesToShow + 1;
                }
            }
        }

        for (var i = startPage; i <= endPage; i++) {
            clientPageNumbers += `<button class="client-page-number" data-page="${i}">${i}</button>`;
        }
        $('#clientPageNumbers').html(clientPageNumbers);
    }

    function updateClientPaginationButtons() {
        $('#clientPrevPage, #clientFirstPage').prop('disabled', clientCurrentPage === 1);
        $('#clientNextPage, #clientLastPage').prop('disabled', clientCurrentPage === clientTotalPages);
    }

    function resetPagination() {
        clientRows.show();
        clientCurrentPage = 1;
        showClientPage(clientCurrentPage);
        updateClientPagination();
        updateClientPaginationButtons();
    }

    showClientPage(clientCurrentPage);
    updateClientPagination();
    updateClientPaginationButtons();

    // Pagination button click handlers
    $('#clientFirstPage').on('click', function() {
        clientCurrentPage = 1;
        showClientPage(clientCurrentPage);
        updateClientPagination();
        updateClientPaginationButtons();
    });

    $('#clientPrevPage').on('click', function() {
        if (clientCurrentPage > 1) {
            clientCurrentPage--;
            showClientPage(clientCurrentPage);
            updateClientPagination();
            updateClientPaginationButtons();
        }
    });

    $('#clientNextPage').on('click', function() {
        if (clientCurrentPage < clientTotalPages) {
            clientCurrentPage++;
            showClientPage(clientCurrentPage);
            updateClientPagination();
            updateClientPaginationButtons();
        }
    });

    $('#clientLastPage').on('click', function() {
        clientCurrentPage = clientTotalPages;
        showClientPage(clientCurrentPage);
        updateClientPagination();
        updateClientPaginationButtons();
    });

    $(document).on('click', '.client-page-number', function() {
        clientCurrentPage = parseInt($(this).attr('data-page'));
        showClientPage(clientCurrentPage);
        updateClientPagination();
        updateClientPaginationButtons();
    });

    $('#clientShowAll').on('click', function() {
        if (clientPaginatedView) {
            clientStoredPage = clientCurrentPage;
            clientRows.show();
            $('#clientShowAll').text('Back');
            clientPaginatedView = false;
        } else {
            clientCurrentPage = clientStoredPage;
            showClientPage(clientCurrentPage);
            updateClientPagination();
            updateClientPaginationButtons();
            $('#clientShowAll').text('All');
            clientPaginatedView = true;
        }
    });
});