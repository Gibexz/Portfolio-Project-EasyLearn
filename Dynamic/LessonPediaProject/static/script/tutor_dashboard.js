$(document).ready(function() {

    // DashBoard Navigation Links 
    // start
    $('.nav_links').on("click", function(e) {
        e.preventDefault();

        $('.nav_links').removeClass('active');
        $(this).addClass('active');

        var targetDiv = $(this).attr('class').split(' ')[1];
        $('.content_divs').hide();
        $('.' + targetDiv + '_contents').show()
    });

    // set dashboard as active by default by triggering a click
    $('.dashboard').trigger('click');
    //stop


    // settings related jquery
    // start
    $(".test").click(function() {
        // Remove active class and reset styles for all td elements
        $(".test").css({
            "border": "none",
            "border-bottom": "1px solid black",
            "color": "black",
            "box-shadow": "none"
        });

        $("#deactivate_account").click(function(){
            $(this).css("color", "red")
        })
        $("#deactivate_account").css("color", "red")

        // Add active class and apply styles to the clicked td element
        $(this).css({
            "border": "1px solid black",
            "border-bottom": "1px solid transparent",
            "color": "rgb(3, 120, 3)",
            "box-shadow": "2px 2px 10px 2px rgb(201, 199, 199)"
        });
    });


    // toggling navigation for programs
    $("#your_subject").click(function(){
        $(".subject_view_display").css("display", "block")
        $(".subject_add_display").css("display", "none")
        $(".subject_update_display").css("display", "none")
        $(".subject_remove_display").css("display", "none")
    })
    $("#add_subject").click(function(){
        $(".subject_view_display").css("display", "none")
        $(".subject_add_display").css("display", "block")
        $(".subject_update_display").css("display", "none")
        $(".subject_remove_display").css("display", "none")
    })
    $("#update_subject").click(function(){
        $(".subject_view_display").css("display", "none")
        $(".subject_add_display").css("display", "none")
        $(".subject_update_display").css("display", "block")
        $(".subject_remove_display").css("display", "none")
    })
    $("#remove_subject").click(function(){
        $(".subject_view_display").css("display", "none")
        $(".subject_add_display").css("display", "none")
        $(".subject_update_display").css("display", "none")
        $(".subject_remove_display").css("display", "block")
    })



    // logic and alert for subject addtion to the database
    $('#subjectForm').submit(function(event) {
        event.preventDefault();
        const subjectName = $('#subjectName').val();
        const proficiency = $('#proficiency').val();
        const teachingExperience = $('#teachingExperience').val();
  
        // For demonstration purposes, alert the submitted values
        alert(`Subject Name: ${subjectName}\nProficiency: ${proficiency}\nTeaching Experience: ${teachingExperience}\n\n Successfully Added`);
  
        // You can replace the alert with code to save this information to a database or perform other operations
      });

    

    // toggling nav dialog display for settings
    $("#change_password").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".change_password_control_display").css("display", "block")
        $(".doc_uploads").css("display", "none")
    })

    $("#update_profile").click(function(){
        $(".profile_control_display").css("display", "block")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".doc_uploads").css("display", "none")
    })
    $("#update_schedule").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "block")
        $(".doc_uploads").css("display", "none")
    })

    $("#uploads").click(function(){
        $(".profile_control_display").css("display", "none")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".doc_uploads").css("display", "block")
    })

    $("#deactivate_account").click(function(){
        $(".deactivate_account_control_display").css("display", "block")
    })
    
    $(".mistake").click(function(){
        $(".deactivate_account_control_display").css("display", "none")
        $(".profile_control_display").css("display", "block")
        $(".change_password_control_display").css("display", "none")
        $(".working_schedule").css("display", "none")
        $(".doc_uploads").css("display", "none")
        $("#deactivate_account").css({
            "border": "none",
            "border-bottom": "1px solid black",
            "color": "red",
        });
        $("#update_profile").css({
            "border": "1px solid black",
            "border-bottom": "1px solid transparent",
            "color": "rgb(3, 120, 3)"
        });
    })
    // stop
    

    // update profile js
    $('#profile_update_save_btn').on('click', function(event) {
        event.preventDefault();
        alert("Password successfully changed");
        // implementation of database interaction codes
    });

    // update password js
    $('#password_update_save_btn').on('click', function(event) {
        event.preventDefault();
        alert("Password successfully changed");
        // implementation of database interaction codes
    });

   // update schedule js
    $('#day_save_btn').on('click', function(event) {
        event.preventDefault();
        
        const selectedDays = $('input[name="workingDay"]:checked').map(function() {
            return this.value;
        }).get();
        
        alert("Selected Working Days: " + selectedDays.join(", "));
        // Here you can perform further actions like sending the selected days to a server or saving them in a database
    });

    
    $('#hour_save_btn').on('click', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const selectedHours = $('input[name="workingHour"]:checked').map(function() {
            return this.value;
        }).get();

        alert("Selected Working Hours: " + selectedHours.join(", "));
        // Here you can perform further actions like sending the selected hours to a server or saving them in a database
    });


    // logout_activation
    // start
    $('.logout_activation').click(function(){
        $(".logout_btn").css("display", "block")
    })

    $(".cancel_logout").click(function() {
        $(".logout_btn").css("display", "none")
    })
    // stop

    // report button
    $('.report_btn').click(function(){
        $(".report_btn_activation").css("display", "block")
    })

    $(".cancel_report").click(function() {
        $(".report_btn_activation").css("display", "none")
    })
    // stop

    //  cancel contract button
    $('.cancel_contract_btn').click(function(){
        $(".cancel_contract_btn_activation").css("display", "block")
    })

    $(".cancel_report").click(function() {
        $(".cancel_contract_btn_activation").css("display", "none")
    })
    // stop

    //  review pop up link
    $('.review_link').click(function(){
        $(".review_link_popup_activation").css("display", "block")
    })

    $(".close_review").click(function() {
        $(".review_link_popup_activation").css("display", "none")
    })
    // stop

    //  review pop up link
    $('.view_reports').click(function(){
        $(".reports_view_popup_activation").css("display", "block")
    })

    $(".close_review").click(function() {
        $(".reports_view_popup_activation").css("display", "none")
    })
    // stop

});



// sort algorithm for tutors review pop up
$(document).ready(function() {
    $('.sortReview').on('click', function() {
      const column = $(this).data('column');
      const $tbody = $('#reviewTable tbody');
      const $header = $(this);
      const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

      // Remove arrow indicator from all headers
      $('.sortReview').data('direction', '');

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

  // sort algorithm for tutors report pop up
$(document).ready(function() {
    $('.sortReport').on('click', function() {
      const column = $(this).data('column');
      const $tbody = $('#reportTable tbody');
      const $header = $(this);
      const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

      // Remove arrow indicator from all headers
      $('.sortReport').data('direction', '');

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
//client_list_table_active

// sort js algorithm for Active Clients table
$(document).ready(function() {
    $('.client_list_table_active th').on('click', function() {
      const column = $(this).data('column');
      const $tbody = $('.client_list_table_active tbody');
      const $header = $(this);
      const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

      $('.client_list_table_active th').data('direction', '');

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



// sort js algorithm for client history table
$(document).ready(function() {
    $('.client_list_table_history th').on('click', function() {
      const column = $(this).data('column');
      const $tbody = $('.client_list_table_history tbody');
      const $header = $(this);
      const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

      $('.client_list_table_history th').data('direction', '');

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



// sort js algorithm for income table
$(document).ready(function() {
    $('.client_list_table_income th').on('click', function() {
      const column = $(this).data('column');
      const $tbody = $('.client_list_table_income tbody');
      const $header = $(this);
      const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

      $('.client_list_table_income th').data('direction', '');

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



// Dynamic saving of work days and hours selected to the html form. CHAT GPT I HAIL
// update schedule js
$(document).ready(function() {
    function populateSavedData() {
      const savedDays = localStorage.getItem('savedDays');
      const savedHours = localStorage.getItem('savedHours');

      if (savedDays) {
        $('#subjectDays tbody').html(savedDays);
      }

      if (savedHours) {
        $('#subjectHours tbody').html(savedHours);
      }
    }

    populateSavedData(); // Load saved data on page load

    $('#save_btn').on('click', function() {
      const daysChecked = $('#workDays input[type="checkbox"]:checked');
      const hoursChecked = $('#workHours input[type="checkbox"]:checked');

      $('#subjectDays tbody').empty();
      $('#subjectHours tbody').empty();

      daysChecked.each(function() {
        $('#subjectDays tbody').append('<tr><td>' + $(this).val() + '</td></tr>');
      });

      hoursChecked.each(function() {
        $('#subjectHours tbody').append('<tr><td>' + $(this).val() + '</td></tr>');
      });

      // Store data to Local Storage
      localStorage.setItem('savedDays', $('#subjectDays tbody').html());
      localStorage.setItem('savedHours', $('#subjectHours tbody').html());

      //ajax code implementation
              // Simulate sending data to the database
        // $.ajax({
        // type: 'POST',
        // url: '/your-backend-endpoint', // Replace with your backend API endpoint
        // data: {
        //     days: $('#subjectDays tbody').html(),
        //     hours: $('#subjectHours tbody').html()
        // },
        // success: function(response) {
        //     console.log('Data saved to database:', response);
        // },
        // error: function(error) {
        //     console.error('Error saving data:', error);
        // }
        // });

      $(this).addClass('inactive');
      $('#workDays')[0].reset();
      $('#workHours')[0].reset();
    });

    $('#reset_btn').on('click', function() {
      $('#workDays')[0].reset();
      $('#workHours')[0].reset();
      $('#subjectDays tbody').empty();
      $('#subjectHours tbody').empty();
      $('#save_btn').addClass('inactive');

      // Clear Local Storage data
      localStorage.removeItem('savedDays');
      localStorage.removeItem('savedHours');
    });

    $('.work_options input[type="checkbox"]').on('change', function() {
      const daysChecked = $('#workDays input[type="checkbox"]:checked');
      const hoursChecked = $('#workHours input[type="checkbox"]:checked');

      if (daysChecked.length > 0 && hoursChecked.length > 0) {
        $('#save_btn').removeClass('inactive');
      } else {
        $('#save_btn').addClass('inactive');
      }
    });


    // suspend tutor account
    $('.confirm_remove').on('click', function() {
      $(this).hide(); 
    $('#passwordInputContainer').toggle();
    $('.cancel_suspend').hide();
  });

});
