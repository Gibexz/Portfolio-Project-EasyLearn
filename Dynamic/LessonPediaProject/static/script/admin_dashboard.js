$(document).ready(function(){
    // $(".check_status").each(function() {
    //     const value = $(this).text();
    //     if (value === "Active") {
    //         $(this).css({
    //             "border": "1px solid green",
    //             "background-color": "rgb(205, 243, 209)"
    //         })
    //     } else {
    //         $(this).css({
    //             "border": "1px solid red",
    //             "background-color": "rgb(252, 206, 206)"
    //         })
    //     }
    // });

    $("#set_tutor").click(function(){
        $(".activate_tutors").show()
        $(".activate_learners").hide()
        $(".tutor_report").hide()
        $(".client_report").hide()
    })
    $("#set_learner").click(function(){
        $(".activate_tutors").hide()
        $(".activate_learners").show()
        $(".tutor_report").hide()
        $(".client_report").hide()
    })
    $("#set_tutor_report").click(function(){
        $(".activate_tutors").hide()
        $(".activate_learners").hide()
        $(".tutor_report").show()
        $(".client_report").hide()
    })
    $("#set_client_report").click(function(){
        $(".activate_tutors").hide()
        $(".activate_learners").hide()
        $(".tutor_report").hide()
        $(".client_report").show()
    })
    

    // Take action dialogue for Tutor ==============================
    $('.action').click(function(){

        const adminName = $(".admin_username").text()
        var tutorData = $(this).data('tutor')

        let tutorId = tutorData.id
        // // Associate the tutor ID with the suspension dialogue
        $('.confirm_remove_tutor').attr('data-tutor-id', tutorId);
        $('.confirm_activate_tutor').attr('data-tutor-id_activate', tutorId);

        // console.log(tutorData); // Check the entire tutorData object
        
        let tutorProfileImage = tutorData.profile_picture

        $('#tutor_profile_image').attr('src', tutorProfileImage);
    
        $('.selected_user').text(tutorData.username);
        $('.profile_userName').text(tutorData.username);
        $('.full_name').text(tutorData.first_name +" "+ tutorData.last_name);
        $('.gender').text(tutorData.gender);
        $('.phone_number').text(tutorData.phone_number);
        $('.residential_address').text(tutorData.residential_address);
        $('.state_of_residence').text(tutorData.state_of_residence);
        $('.nationality').text(tutorData.nationality);
        $('.institution').text(tutorData.institution);
        $('.institution_type').text(tutorData.institution_type);
        $('.area_of_specialization').text(tutorData.area_of_specialization);
        $('.highest_qualification').text(tutorData.highest_qualification);
        $('.result').text(tutorData.result);
        $('.employment_status').text(tutorData.employment_status);
        $('.employment_type').text(tutorData.employment_type);
        $('.availability').text(tutorData.availability);
        $('.total_clients').text(tutorData.total_clients);
        $('.active_clients').text(tutorData.active_clients);
        $('.rejected_clients').text(tutorData.rejected_clients);
        $('.ranking').text(tutorData.ranking);
        $('.is_active').text(tutorData.is_active );
        $('.id_tutor').text(tutorData.id);
        $('.last_login_tutor').text(tutorData.last_login);
        $('.date_of_birth_tutor').text(tutorData.date_of_birth);
        $('.reviews_id_tutor').text(tutorData.reviews_id);
        $('.status_tutor').text(tutorData.status);
        $('.created_at_tutor').text(tutorData.created_at);
        $('.lga_resident_tutor').text(tutorData.lga_resident);
        $('.personal_statement_tutor').text(tutorData.personal_statement);
        $('.discipline_tutor').text(tutorData.discipline);
        $('.others_tutor').text(tutorData.others);
        $('.working_hours_tutor').text(tutorData.working_hours);
        $('.cv_id_tutor').text(tutorData.cv_id);
        $('.updated_at_tutor').text(tutorData.updated_at);
        $('.groups_tutor').text(tutorData.groups);

    
        $('.active_admin').text(adminName);
    
        if (tutorData.hasOwnProperty('email')) {
            // console.log(tutorData.email); // Check if tutorData.email is populated
            $('.selected_email').text(tutorData.email);
        } else {
            // console.log('n0t accsisble');
        }

        $('.set_action_tutor').show()
    })

    $('.close').click(function(){
        $('.set_action_tutor').hide()
    })



    // Take action dialogue for Client ==============================
    $('.action_client').click(function(){

        const adminName = $(".admin_username").text()
        var clientData = $(this).data('client')

        let clientId = clientData.id
        // // Associate the tutor ID with the suspension dialogue
        $('.confirm_remove_client').attr('data-client-id', clientId);
        $('.confirm_activate_client').attr('data-client-id_activate', clientId);
    
        // console.log(clientData); // Check the entire clientData object
        
        let clientProfileImage = clientData.profile_picture

        $('#client_profile_image').attr('src', clientProfileImage);
    
        $('.id_client').text(clientData.id); //not used
        $('.selected_user_client').text(clientData.username);
        $('.profile_userName_client').text(clientData.username);
        $('.full_name_client').text(clientData.first_name +" "+clientData.last_name);
        $('.gender_client').text(clientData.gender);
        $('.phone_number_client').text(clientData.phone_number);
        $('.residential_address_client').text(clientData.residential_address);
        $('.state_of_residence_client').text(clientData.state_of_residence);
        $('.nationality_client').text(clientData.nationality);
        $('.is_active_client').text(clientData.is_active);
        $('.last_login_client').text(clientData.last_login);
        $('.date_of_birth_client').text(clientData.date_of_birth);
        $('.created_at_client').text(clientData.created_at);
        $('.educational_level_client').text(clientData.educational_level);
        $('.updated_at_client').text(clientData.updated_at);
        $('.tutor_client').text(clientData.tutor);
        $('.groups_client').text(clientData.groups);
        

        $('.active_admin').text(adminName);
    
        if (clientData.hasOwnProperty('email')) {
            // console.log(clientData.email); // Check if clientData.email is populated
            $('.selected_email_client').text(clientData.email);
        } else {
            console.log('not accsisble');
        }

        $('.set_action_client').show()
    })

    $('.close_client').click(function(){
        $('.set_action_client').hide()
    })


    // profile, review and report activation logic for tutor ==============================
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
    
    
    // profile, review and report activation logic for client ==============================
    $('#activate_review_client').click(function(){
        $('.set_other_details_client').hide()
        $('.set_review_details_client').show()
        $('.set_report_details_client').hide()
    })
    $('#activate_profile_client').click(function(){
        $('.set_other_details_client').show()
        $('.set_review_details_client').hide()
        $('.set_report_details_client').hide()
    })
    $('#activate_report_client').click(function(){
        $('.set_other_details_client').hide()
        $('.set_review_details_client').hide()
        $('.set_report_details_client').show()
    })


    // account suspending dialogue display for tutor  ==============================
    $('#activate_suspend_tutor').click(function(){
        const tutor_id = $(this).data('tutor')

        $('.set_action_tutor').hide()
        $('.set_suspend_account_tutor').show()
    })

    $('.disable_close, .mistake').click(function(){
        $('.set_action_tutor').show()
        $('.set_suspend_account_tutor').hide()
    })
    

    // account suspending dialogue display for client  ==============================
    $('#activate_suspend_client').click(function(){
        const client_id = $(this).data('client')

        $('.set_action_client').hide()
        $('.set_suspend_account_client').show()
    })

    $('.disable_close, .mistake').click(function(){
        $('.set_action_client').show()
        $('.set_suspend_account_client').hide()
    })

    
    // account blocking dialogue display for tutor  ==============================
    $('#activate_block').click(function(){
        const tutor_id = $(this).data('tutor')

        $('.set_action_tutor').hide()
        $('.set_disable_account').show()
    })

    $('.disable_close, .mistake').click(function(){
        $('.set_action_tutor').show()
        $('.set_disable_account').hide()
    })


    // account suspending dialogue display for client  ==============================
    $('#activate_block_client').click(function(){
        $('.set_action_client').hide()
        $('.set_disable_account_client').show()
    })

    $('.disable_close_client, .mistake_client').click(function(){
        $('.set_action_client').show()
        $('.set_disable_account_client').hide()
    })


    // account reactivation dialogue display for tutor  ==============================
    $('#reactivate_account_tutor').click(function(){
        $('.set_action_tutor').hide()
        $('.set_reactivate_account_tutor').show()
    })

    $('.disable_close, .mistake').click(function(){
        $('.set_action_tutor').show()
        $('.set_reactivate_account_tutor').hide()
    })


    // account reactivation dialogue display for client  ==============================
    $('#reactivate_account_client').click(function(){
        $('.set_action_client').hide()
        $('.set_reactivate_account_client').show()
    })

    $('.disable_close_client, .mistake_client').click(function(){
        $('.set_action_client').show()
        $('.set_reactivate_account_client').hide()
    })


    // account deletion dialogue display for tutor  ==============================
    $('#delete_account_tutor').click(function(){
        $('.set_action_tutor').hide()
        $('.set_delete_account_tutor').show()
    })

    $('.disable_close, .mistake').click(function(){
        $('.set_action_tutor').show()
        $('.set_delete_account_tutor').hide()
    })


    // account deletion dialogue display for client  ==============================
    $('#delete_account_client').click(function(){
        $('.set_action_client').hide()
        $('.set_delete_account_client').show()
    })

    $('.disable_close_client, .mistake_client').click(function(){
        $('.set_action_client').show()
        $('.set_delete_account_client').hide()
    })

});


$(document).ready(function() {

    function displayMessageSuccess(message) {
        let messageDivSuccess = $('#messageDivSuccess');
        messageDivSuccess.text(message);
        messageDivSuccess.fadeIn().delay(5000).fadeOut();
    }
    function displayMessageError(message) {
        let messageDivError = $('#messageDivError');
        messageDivError.text(message);
        messageDivError.fadeIn().delay(5000).fadeOut();
    }



    // logic to disable a tutor's account  ==========================================
    $('.confirm_remove_tutor').click(function() {

        const api_url = 'http://127.0.0.1:8000/appAdmin'

        let tutor_id = $(this).data('tutor-id'); 
        console.log(tutor_id);
        
        // collect the csrf token and store it in a variable
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        $.ajax({
            method: 'POST',
            // url: `${api_url}/api/tutors_action_api/deactivate_tutor/${tutor_id}/`, // works too
            url: `${api_url}/api/tutors_action_api/${tutor_id}/deactivate_tutor/`,

            beforeSend: function(xhr) { 
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
                displayMessageSuccess('Tutor deactivated (blocked) successfully');
            },
            error: function(xhr, textStatus, errorThrown) {
                displayMessageError('Error suspending tutor: ' + errorThrown);
            }
        });
        $('.set_action_tutor').show()
        $('.set_disable_account').hide()
    });



    // logic to disable a client's account  =====================================
    $('.confirm_remove_client').click(function() {

        const api_url = 'http://127.0.0.1:8000/appAdmin'

        let client_id = $(this).data('client-id'); 
        // console.log(client_id);
        
        // collect the csrf token and store it in a variable
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        $.ajax({
            method: 'POST',
            // url: `${api_url}/api/clients_action_api/suspend_client/${client_id}/`, // works too
            url: `${api_url}/api/clients_action_api/${client_id}/suspend_client/`,

            beforeSend: function(xhr) { 
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
                displayMessageSuccess('Client suspended successfully');
            },
            error: function(xhr, textStatus, errorThrown) {
                displayMessageError('Error suspending client: ' + errorThrown);
            }
        });
        $('.set_action_client').show()
        $('.set_disable_account_client').hide()
    });



    // logic to reactivate a tutor's account  ==========================================
    $('.confirm_activate_tutor').click(function() {

        const api_url = 'http://127.0.0.1:8000/appAdmin'

        let tutor_id = $(this).data('tutor-id_activate'); 
        console.log(tutor_id);
        
        // collect the csrf token and store it in a variable
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        $.ajax({
            method: 'POST',
            // url: `${api_url}/api/tutors_action_api/activate_tutor/${tutor_id}/`, // works too
            url: `${api_url}/api/tutors_action_api/${tutor_id}/activate_tutor/`,

            beforeSend: function(xhr) { 
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
                displayMessageSuccess('Tutor profile reactivated successfully');
            },
            error: function(xhr, textStatus, errorThrown) {
                displayMessageError('Error reactivating tutor profile: ' + errorThrown);
            }
        });
        $('.set_action_tutor').show()
        $('.set_reactivate_account_tutor').hide()
    });



    // logic to reactivate a clients's account  ==========================================
    $('.confirm_activate_client').click(function() {

        const api_url = 'http://127.0.0.1:8000/appAdmin'

        let client_id = $(this).data('client-id_activate'); 
        console.log(client_id);
        
        // collect the csrf token and store it in a variable
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        $.ajax({
            method: 'POST',
            // url: `${api_url}/api/clients_action_api/activate_client/${client_id}/`, // works too
            url: `${api_url}/api/clients_action_api/${client_id}/activate_client/`,

            beforeSend: function(xhr) { 
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
                displayMessageSuccess('client profile reactivated successfully');
            },
            error: function(xhr, textStatus, errorThrown) {
                displayMessageError('Error reactivating client profile: ' + errorThrown);
            }
        });
        $('.set_action_client').show()
        $('.set_reactivate_account_client').hide()
    });





})







//  live table sort for tutor admin table list  ===================================
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


//  live table sort for client admin table list  ====================================
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

$(document).ready(function() {
    // status check for tutor  ==============================
    $('.check_status').each(function() {
        const isActive = $(this).data('active');
        
        if (isActive === true || isActive == 'True') {
            $(this).css({'background-color': 'lightgreen', 'border': '1px solid white'});
        } else {
            $(this).css({'background-color': ' rgb(235, 64, 64)', 'border': '1px solid white', 'color': 'white'});
        }
    });
    // status check for client ==============================
    $('.check_status_client').each(function() {
        const isActive = $(this).data('active_client');
        
        if (isActive === true || isActive == 'True') {
            $(this).css({'background-color': 'lightgreen', 'border': '1px solid white'});
        } else {
            $(this).css({'background-color': ' rgb(235, 64, 64)', 'border': '1px solid white', 'color': 'white'});
        }
    });
});


// Pagination for Tutors view  ===============================================
$(document).ready(function() {
    var tutorRows = $('.tutor_table_list tbody tr');
    var tutorRowsPerPage = 10;
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


// pagination for learners/clients view ========================================
$(document).ready(function() {
    var clientRows = $('.learner_table_list tbody tr');
    var clientRowsPerPage = 10;
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