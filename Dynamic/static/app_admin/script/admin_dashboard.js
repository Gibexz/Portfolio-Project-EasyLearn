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

    $('.action').click(function(){
        const userName = $(this).closest("tr").find(".user_name").text();
        const userEmail = $(this).closest("tr").find(".user_email").text();
        const userType = $(this).closest(".activate_tutors, .activate_learners").find(".inner_content .validate").text();
        $('.selected_user').text(userName)
        $('.selected_email').text(userEmail)
        $('.profile_userName').text(userName)

        const adminName = $(".admin_username").text()
        $('.active_admin').text(adminName)
        if (userType === "Total Tutors"){
            $(".set_tutors_details").show()
        } else {
            $(".set_tutors_details").hide()
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


$(document).ready(function() {
    let ascending = true;

    function sortTable(columnIndex) {
        const table = $('#data_table');
        const rows = table.find('tbody > tr').get();

        rows.sort(function(a, b) {
            const cellA = $(a).find(`td:eq(${columnIndex})`).text().toUpperCase();
            const cellB = $(b).find(`td:eq(${columnIndex})`).text().toUpperCase();

            if ($.isNumeric(cellA) && $.isNumeric(cellB)) {
                return ascending ? cellA - cellB : cellB - cellA;
            } else {
                return ascending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
            }
        });

        $.each(rows, function(index, row) {
            table.children('tbody').append(row);
        });
    }

    $('.table_header td').on('click', function() {
        const columnIndex = $(this).index();
        sortTable(columnIndex);
        ascending = !ascending;
    });
});

