  // Function to get CSRF token from cookie
  
  $(document).ready(function() {
    
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          let cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    // DashBoard Navigation Links 
    // start
    $('.nav_links').on("click", function(e) {
        e.preventDefault();

        $('.nav_links').removeClass('active');
        $(this).addClass('active');

        let targetDiv = $(this).attr('class').split(' ')[1];
        $('.content_divs').hide();
        $('.' + targetDiv + '_contents').show()
        if (targetDiv !== 'dashboard') {
            $('.stats').css('cursor', 'not-allowed');
        }
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
            "font-weight": "normal",
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
            "font-weight": "bold",
            "box-shadow": "2px 2px 10px 2px rgb(201, 199, 199)"
        });
    });
    $(".test2").click(function() {
      $('.test2').css({
        color: 'black',
        fontWeight: 'normal',
        boxShadow: 'none',
      })
      // Add active class and apply styles to the clicked td element
      $(this).css({
          "color": "rgb(3, 120, 3)",
          "font-weight": "bold",
          "box-shadow": "2px 2px 10px 2px rgb(201, 199, 199)"
  
  });
    })


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
        $(".deactivate_account_blank").css("display", "block")
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

    //  cancel contract pop up link
    $('.cancel_contract_btn button').click(function(){
        $(".disengage").css("display", "block")
    })

    $(".closeModal").click(function() {
        $(".disengage").css("display", "none")
    })
    // stop
    $('.review_link').click(function(){
      $(".review_link_popup_activation").css("display", "block")
  })

  $(".close_review").click(function() {
      $(".review_link_popup_activation").css("display", "none")
  })

    // pending client pop up
    $('#pending_clients').click(function(){
      $(".pending_clients_activation").css("display", "block")
    })

    $(".close_pending_clients").click(function() {
      $(".pending_clients_activation").css("display", "none")
    })
    // stop

    // settled client pop up
        // pending client pop up
        $('#settled_clients').click(function(){
          $(".settled_clients_activation").css("display", "block")
        })
    
        $(".close_settled_clients").click(function() {
          $(".settled_clients_activation").css("display", "none")
        })
        // stop

    //  reports pop up link
    $('.view_reports').click(function(){
        $(".reports_view_popup_activation").css("display", "block")
    })

    $(".close_review").click(function() {
        $(".reports_view_popup_activation").css("display", "none")
    })
    // stop


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

//client_list_table_active

// sort js algorithm for Active Clients table

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


// sort js algorithm for client history table

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


// sort js algorithm for client pending table

$('.sortPendingClients').on('click', function() {
  const column = $(this).data('column');
  const $tbody = $('#pendingClientTable tbody');
  const $header = $(this);
  const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

  // Remove arrow indicator from all headers
  $('.sortPendingClients').data('direction', '');

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

// sort Settled
$('.sortSettledContracts').on('click', function() {
  const column = $(this).data('column');
  const $tbody = $('#settledClientTable tbody');
  const $header = $(this);
  const direction = $header.data('direction') === 'ascending' ? 'descending' : 'ascending';

  // Remove arrow indicator from all headers
  $('.sortPendingContracts').data('direction', '');

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

// sort js algorithm for income table

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

// js for tutor availability

  $('#reset_btn').click(function () {
    $('#updateScheduleForm').trigger('reset');
  });


function isOverlap(fromTime, toTime, storedFromTime, storedToTime) {
  if (fromTime === toTime || storedFromTime === storedToTime) {
 

    return true;
  }

  const [fromHour, fromMinute] = fromTime.split(':').map(Number);
  const [toHour, toMinute] = toTime.split(':').map(Number);
  const [storedFromHour, storedFromMinute] = storedFromTime.split(':').map(Number);
  const [storedToHour, storedToMinute] = storedToTime.split(':').map(Number);
  
  if ( storedFromTime.length < 1 || storedToTime.length < 1 || storedFromTime === undefined || storedToTime === undefined || storedFromTime === '' || storedToTime === '') {
    if (fromHour > toHour) {
      return true;
    }
  }
  // Check for empty ranges

  if ((fromHour === storedFromHour)) {
    return true;
  }
  if ((toHour === storedToHour)) {
    return true;
  }
  if (fromHour === storedFromHour || toHour === storedToHour) {
    return true;
  }
  if (fromHour > toHour) {
    return true;
  }
  if (fromHour < storedFromHour && toHour >= storedFromHour) {
    return true;
  }


  // No overlap found
  return false;
}

  const form = $('.updateEngagements');

  form.submit(function (e) {
    e.preventDefault();
    // Serialize the form data as an array
    let selectedDay = form.find('select[name="day"] option:selected').text();
    let newStartTime = form.find('select[name="from_hour"] option:selected').text();
    let newEndTime = form.find('select[name="to_hour"] option:selected').text();
    let existingTimeSlots = [];

    // Iterate over each row in the subjectDays table
    $('#subjectDays tbody tr').each(function (index) {
      let existingDay = $(this).find('td').text().trim();
      if (selectedDay === existingDay) {
        // If matched, find the corresponding time slot in subjectHours table
        let existingTimeRange = $('#subjectHours tbody tr:eq(' + index + ') td').text().split(' - ');
        let existingStartTime = existingTimeRange[0].trim();
        let existingEndTime = existingTimeRange[1].trim();
        existingTimeSlots.push({ startTime: existingStartTime, endTime: existingEndTime });
      }
    });
    let overlap = false;
    if (newStartTime ===  newEndTime){
      overlap = true;
    }
    const [toHour, toMinute] = newStartTime.split(':').map(Number);
    const [fromHour, fromMinute] = newEndTime.split(':').map(Number);
    if (toHour >= fromHour) {
      overlap = true;
    }

    // Check for overlap with existing time slots
    for (let i = 0; i < existingTimeSlots.length; i++) {
      if (isOverlap(newStartTime, newEndTime, existingTimeSlots[i].startTime, existingTimeSlots[i].endTime)) {
        overlap = true;
        break;
      }
    }

    if (overlap) {
      $('#overlap').show();
      $('#closeOverlapModal').click(function () {
        $('#overlap').hide();
      });
      return;
    }

    // No overlap, proceed with form submission
    let formDataArray = form.serializeArray();
    $.ajax({
      type: 'POST',
      url: '/tutor/dashboard/',
      data: formDataArray,
      success: function (data) {
        let token = $('[name="csrfmiddlewaretoken"]').val();

        form.trigger('reset');
        if (data && data.schedule_data) {
          updateScheduleTables(data.schedule_data, token);
        }
      },
      error: function (data) {
        console.error('Error:', data);
      },
    });
  });

// function updateScheduleTables(data, token) {
//   // Update the Days table
//   let daysTable = document.getElementById('subjectDays');
//   daysTable.innerHTML = '<thead><tr><th>Days</th></tr></thead><tbody>';
//   data.forEach(function (schedule) {
//     daysTable.innerHTML += `<tr><td class="flexRemove">${schedule.day} &nbsp<i class="fa-solid fa-circle-xmark" data-schedule-id="${schedule.id}"></i></td></tr>`;
//     daysTable.innerHTML += `<form method="post" action="{% url 'delete_schedule' schedule.id %}"> <input type="hidden" name="csrfmiddlewaretoken"  value="${token}"> <button hidden  type="submit"></button></form>`;
//   });
//   daysTable.innerHTML += '</tbody>';//<input type="hidden" name="csrfmiddlewaretoken" value="AV3C03Ch1ea1fHOZ6zJDnoRuIvmBAp6ZlLqrsl3zmmGzAJGlPfRZKeHbujZPM0tH">
  
//     // Update the Hours table
//     let hoursTable = document.getElementById('subjectHours');
//     hoursTable.innerHTML = '<thead><tr><th>Hours</th></tr></thead><tbody>';
//     data.forEach(function (schedule) {
//       hoursTable.innerHTML += '<tr><td>' + schedule.from_hour + ' - ' + schedule.to_hour + '</td></tr>';
//     });
//     hoursTable.innerHTML += '</tbody>';

// }
function updateScheduleTables(data, token) {
  // Update the Days table
  let daysTable = $('#subjectDays tbody');
  daysTable.empty(); // Clear the existing content

  data.forEach(function (schedule) {
    daysTable.append(`<tr><td class="flexRemove">${schedule.day} &nbsp<i class="fa-solid fa-circle-xmark" data-schedule-id="${schedule.id}"></i></td><form method="post" action="/tutor/deleteSchedule/${schedule.id}"> 
      </form>
      <input type="hidden" name="csrfmiddlewaretoken" value="${token}"></tr>`);
  });

  // Update the Hours table
  let hoursTable = $('#subjectHours tbody');
  hoursTable.empty(); // Clear the existing content

  data.forEach(function (schedule) {
    hoursTable.append(`<tr data-schedule-id="${schedule.id}"><td>${schedule.from_hour} - ${schedule.to_hour}</td></tr>`);
  });
}


  // Refresh the page
  $('.refreshPage, #refreshPage').click(function () {
    location.reload();
  });
  

// Event delegation for dynamically added elements
$(document).on('click', '.fa-circle-xmark', function (e) {
  e.preventDefault();

  let clickedElement = $(this);
  let scheduleId = clickedElement.data('schedule-id');

  let row = clickedElement.closest('tr');
  let hoursTable = $('#subjectHours');

  // Show the confirmation modal
  $('#confirmationModal').show();

  // Handle the confirm action
  $('#confirmAction').off().on('click', function () {
    $.ajax({
      url: '/tutor/deleteSchedule/' + scheduleId + '/',
      method: 'POST',
      data: {
        csrfmiddlewaretoken: getCookie('csrftoken')
      },
      success: function (data) {
        if (data.status === 'success') {
          // Find and remove the corresponding time row
          let timeRow = hoursTable.find('tr[data-schedule-id="' + scheduleId + '"]');
          timeRow.remove();

          // Remove the entire row (day and delete button) from the Days table
          row.remove();

          $('#successModal').show();
        }
      },
    });

    // Hide the confirmation modal
    $('#confirmationModal').hide();
  });

  // Handle the cancel action
  $('#closeConfirmationModal').off().on('click', function () {
    // Hide the confirmation modal
    $('#confirmationModal').hide();
  });

  // Prevent default form submission
  return false;
});


// Handle closing the success modal
$('#closeSuccessModal').click(function () {
  // Hide the success modal
  $('#successModal').hide();
});

// Handle closing the error modal
$('#refreshPage',).click(function () {
  // Refresh the page
  location.reload();
});



// Handle closing the success modal
$('#closeSuccessModal').click(function () {
  // Hide the success modal
  $('#successModal').hide();
});
  });

  // Tutor Profile and Settings
$(document).ready(function() {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      let cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        let cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
$('.upload-doc-form').submit(function (e) {
  e.preventDefault();

  // Check if any file inputs have files selected
  let hasFiles = false;
  $(this).find('input[type="file"]').each(function () {
      if ($(this)[0].files.length > 0) {
          hasFiles = true;
          return false;
      }
  });

  if (!hasFiles) {
      return;
  }

  let form = $(this);
  let formData = new FormData(form[0]);
  formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

  console.log('Form Data:', formData);

  $.ajax({
    type: 'POST',
    url: '/tutor/uploadDocs/',
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
        console.log('Success Response:', data);

        if (data.status === 'success') {
          $('#done').show();
          form.trigger('reset');
        } else {
          $('#errorModal').show();
            console.log('Inside error block');
        }
    },
    error: function (error) {
        console.log('Error Response:', error);
        console.log('Inside error block');
        $('#errorModal').show(); // Show the error modal
    },
});
$('#closeDone, #refreshPage').click(function () {
  $('.modal').hide();
});
});

// suspend tutor account
$('.confirm_remove').on('click', function() {
  $(this).hide(); 
$('#passwordInputContainer').toggle();
$('.cancel_suspend').hide();
});

// password match
    const newPasswordInput = $('#newPassword');
    const confirmPasswordInput = $('#confirmPassword');
    const submitButton = $('#password_update_save_btn');

    confirmPasswordInput.on('input', function () {
        const passwordsMatch = newPasswordInput.val() === confirmPasswordInput.val();
        if (passwordsMatch) {
            submitButton.removeClass('inactive')
            submitButton.addClass('active_pwd')
        }
        else{
            submitButton.removeClass('active_pwd')
            submitButton.addClass('inactive')
        }
    });
  })

  // Tutors Subjects AJAX
$(document).ready(function() {
  $('.refreshPage, #refreshPage').click(function () {
    location.reload();

  // Tutors Add Subject AJAX
  });

  // Add Subject
  $('#subjectForm').submit(function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    const csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    formData.append("csrfmiddlewaretoken", csrfToken);

    $.ajax({
      type: "POST",
      url: "/tutor/addSubject/",
      data: formData,
      processData: false,
      contentType: false,
      success: function (data) {
        if (data.status === "success") {
          $("#subjectForm").trigger("reset");
          $("#successModal4").show();
          $(".closeModal").click(function () {
            $(".modal2").hide();
          });
          updateSubjectTable(data, $("#subjectUpdateName"), $('#subjectDeleteName'));
        } else {
          $("#errorModal4").show();
          $(".closeModal").click(function () {
            $(".modal2").hide();
          });
        }
      },
      error: function (error) {
        $("#errorModal4").show();
        $(".closeModal").click(function () {
          $(".modal2").hide();
        });
        console.error("Error:", error);
      },
    });
  })


// Update Subject
  $('#subjectUpdateForm').submit(function (event) {
    event.preventDefault();

    const selectedSubjectId = $('#subjectUpdateName option:selected').data('subjectid');

    // Check if the selectedSubjectId is undefined or null
    if (!selectedSubjectId) {
        $('#errorModal2').show();
        return;
    }

    const formData = new FormData(this);
    formData.append('csrfmiddlewaretoken', $('[name="csrfmiddlewaretoken"]').val());

    $.ajax({
        type: 'POST',
        url: `/tutor/updateSubject/${selectedSubjectId}/`,
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
            if (data.status === 'success') {
                updateSubjectTable(data, $('#subjectUpdateName'), $('#subjectDeleteName'));
                $('#subjectUpdateForm').trigger('reset');
                $('#successModal3').show();
                $('.closeModal').click(function () {
                  $('.modal2').hide();                });

            } else {
                $('#errorModal3').show();
                $('.closeModal').click(function () {
                  $('.modal2').hide();                });
                console.error('Error Updating Subject: ' + data.message);
            }
        },
        error: function (error) {
          $('#errorModal3').show();
          $('.closeModal').click(function () {
            $('.modal2').hide();
            });

            console.error('Error Occurred: ' + error.statusText);
        }
    });
});


// populate subject update form 
  function updateSubjectTable(data, selectElement, updateDelete) {
    $('.subject_table tbody').empty();

    // Update the options in the select dropdown
    if (selectElement) {
        selectElement.empty();
        selectElement.append('<option value="" disabled selected>-- select one --</option>');

        if (data.tutor_subjects) {
            if (Array.isArray(data.tutor_subjects)) {
                data.tutor_subjects.forEach(function (subject) {
                    const option = `<option data-subjectId="${subject[0]}" value="${subject[1]}">${subject[1]}</option>`;
                    selectElement.append(option);
                });
            } else {
                const option = `<option data-subjectId="${data.tutor_subjects.id}" value="${data.tutor_subjects.subject_name}">${data.tutor_subjects.subject_name}</option>`;
                selectElement.append(option);
            }
        }
    }
    if (updateDelete) {
      updateDelete.empty();
      updateDelete.append('<option value="" disabled selected>-- select one --</option>');

      if (data.tutor_subjects) {
          if (Array.isArray(data.tutor_subjects)) {
              data.tutor_subjects.forEach(function (subject) {
                  const option = `<option data-subjectId="${subject[0]}" value="${subject[1]}">${subject[1]}</option>`;
                  updateDelete.append(option);
              });
          } else {
              const option = `<option data-subjectId="${data.tutor_subjects.id}" value="${data.tutor_subjects.subject_name}">${data.tutor_subjects.subject_name}</option>`;
              updateDelete.append(option);
          }
      }
  }

    // Add the other subjects to the table
    if (data.tutor_subjects) {
        if (Array.isArray(data.tutor_subjects)) {
            data.tutor_subjects.forEach(function (subject) {
                const subjectRow = `<tr><td>${subject[1]} - <span style="font-size: small;">${subject[2]}</span></td></tr>`;
                $('.subject_table tbody').append(subjectRow);
            });
        } else {
            const subjectRow = `<tr><td>${data.tutor_subjects.subject_name} - <span style="font-size: small;">${data.tutor_subjects.proficiency}</span></td></tr>`;
            $('.subject_table tbody').append(subjectRow);
        }
    }
}

// Delete Subject

  $('#subjectDeleteForm').submit(function (event) {
      event.preventDefault();
      const selectedSubjectId = $('#subjectDeleteName option:selected').data('subjectid');
      if (!selectedSubjectId) {
          alert('Please select a subject.');
          return;
      }
      const csrfToken = $('[name="csrfmiddlewaretoken"]').val();

      $.ajax({
          type: 'POST',
          url: `/tutor/deleteSubject/${selectedSubjectId}/`,
          data: {
              csrfmiddlewaretoken: csrfToken
          },
          success: function (data) {
              if (data.status === 'success') {
                  updateSubjectTable(data, $('#subjectUpdateName'), $('#subjectDeleteName'));
                  $('#subjectDeleteForm').trigger('reset');
                  $('#successModal2').show();
                  $('.closeModal').click(function () {
                    $('.modal2').hide();                  });
              } else {
                  $('#errorModal2').show();
                  $('.closeModal').click(function () {
                    $('.modal2').hide();
                    });
                  console.error('Error Removing Subject: ' + data.message);
              }
          },
          error: function (error) {
              console.error('Error Occurred: ', error);
              $('#errorModal2').show();
              $('.closeModal').click(function () {
                $('.modal2').hide();
                });

          }
      });
  });

// update contracts
  $(document).on("click", ".submitBtnPending", function (event) {
    event.preventDefault();
      let rowId = $(this).closest('tr').attr('id');
      let contractCode = $('#' + rowId + ' .contractCode').val();
      let status = $(this).data('action');
      const csrfToken = $('[name="csrfmiddlewaretoken"]').val();
      if (status !== 'undefined' && status !== null && status !== '') {
        $.ajax({
          url: `/tutor/updateContractStatus/${contractCode}/`,
          type: 'POST',
          data: {
            csrfmiddlewaretoken: csrfToken,
            status: status
          },
          success: function (response) {
                // Clear existing table rows
                if (response.status === 'success') {
                $('#pendingClientTable tbody').empty();
                $('#activeClientTable tbody').empty();
                $('#clientHistoryTable tbody').empty();
                // Iterate over each contract in the response and append to the table
                  for (let i = 0; i < response.pending_contracts.length; i++) {
                      let contract = response.pending_contracts[i];
  
                      // Construct HTML for the current contract
                      let contractHTML = `<tr id="contractRow${i+1}">`;
                      contractHTML += '<td>' + (i + 1) + '</td>'; // Assuming you want to display the index
                      contractHTML += '<td>' + contract.client_name + '</td>'; // Replace 'client_name' with the actual field name in your contract object
                      contractHTML += '<td>' + contract.subject_name + '</td>'; // Replace 'subject_name' with the actual field name in your contract object
                      contractHTML += '<td>' + contract.week_days + '</td>';
                      contractHTML += '<td>' + contract.contract_length + 'Days </td>';
                      contractHTML += '<td> ₦ ' + contract.pay_rate + '</td>';
                      contractHTML += '<td>' + contract.start_date + '</td>';
                      // Construct the accept button
                      contractHTML += `<td class="accept_contract_btn"><form class="contractForm" data-rowid="${i+1}" data-contractcode="${contract.contract_code}">`;
                      contractHTML += '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrfToken + '">';                      
                      contractHTML += `<input type="hidden" class="contractCode" value="${contract.contract_code}">`;
                      contractHTML += '<input type="hidden" name="status" value="Accept">';
                      contractHTML += '<button class="submitBtnPending" data-action="Accept" type="submit">Accept</button>';
                      contractHTML += '</form></td>';
  
                      // Construct the decline button
                      contractHTML += `<td class="decline_contract_btn"><form class="contractForm" data-rowid="${i+1}" data-contractcode="${contract.contract_code}">`;
                      contractHTML += '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrfToken + '">';                      
                      contractHTML += '<input type="hidden" class="contractCode"  value="' + contract.contract_code +'">';
                      contractHTML += '<input type="hidden" name="status" value="Decline">';
                      contractHTML += '<button class="submitBtnPending" data-action="Decline" type="submit">Decline</button>';
                      contractHTML += '</form></td>';
                      
                      contractHTML += '</tr>';
                      
                      // Append the HTML for the current contract to the tbody
                      $('#pendingClientTable tbody').append(contractHTML);
                      // }
                      
              }
              for (let i = 0; i < response.active_contracts.length; i++) {
                let contract = response.active_contracts[i];
                let contractHTML = '<tr>';
                contractHTML += '<td>' + (i + 1) + '</td>';
                contractHTML += '<td>' + contract.contract_code + '</td>';
                contractHTML += '<td>' + contract.client_name + '</td>';
                contractHTML += '<td>' + contract.subject_name + '</td>';
                contractHTML += '<td>' + contract.start_date + '</td>';
                contractHTML += '<td>' + contract.end_date + '</td>';
                contractHTML += '<td>' + contract.week_days + '</td>';
                contractHTML += '<td class="report_btn"> <button>report</button></td>';
                contractHTML += '<td class="cancel_contract_btn"><button>cancel</button></td>';
                contractHTML += '</tr>';
                $('#activeClientTable tbody').append(contractHTML);
              }


              for (let i = 0; i < response.contract_history.length; i++) {
                let contract = response.contract_history[i];
                let contractHTML = '<tr>';
                contractHTML += '<td>' + (i + 1) + '</td>';
                contractHTML += '<td>' + contract.contract_code + '</td>';
                contractHTML += '<td>' + contract.client_name + '</td>';
                contractHTML += '<td>' + contract.subject_name + '</td>';
                contractHTML += '<td>' + contract.start_date + '</td>';
                contractHTML += '<td>' + contract.end_date + '</td>';
                contractHTML += '<td>' + contract.week_days + '</td>';
                if (contract.contract_status === 'Terminated'){
                  contractHTML += `<td class="report_btn"><i class="fa fa-circle" style="color: red;" aria-hidden="true"></i>&nbsp;<button>report</button></td>`;
                }
                else if (contract.contract_status === 'Active'){
                  contractHTML += `<td class="report_btn"><i class="fa fa-circle" style="color: rgb(84, 215, 197);" aria-hidden="true"></i>&nbsp;<button>report</button></td>`;
                }
                else if (contract.contract_status === 'Settled'){
                  contractHTML += `<td class="report_btn"><i class="fa fa-circle" style="color: lime;" aria-hidden="true"></i>&nbsp;<button>report</button></td>`;
                }
                else {
                  contractHTML += `<td class="report_btn"><i class="fa fa-circle" style="color: gray;" aria-hidden="true"></i>&nbsp;<button>report</button></td>`;
                }
                contractHTML += '</tr>';
                $('#clientHistoryTable tbody').append(contractHTML);
              }
              $('#activeContractsH3').text(response.active_contracts_count);
              $('#pendingContractsH3').text(response.pending_contracts_count);
              $('#settledContractsH3').text(response.settled_contracts_count);
              $('#totalEarningsH3').text(response.received_payments);
              // clickedButton.closest('form')[0].reset(); 
            } else {
              console.log('Error:', response.message);
            }
          },
          error: function (jqXHR, textStatus, errorThrown) {
            console.error("AJAX Error:", textStatus, errorThrown);
            console.log("Response:", jqXHR.responseText);
          }
        });
    }
  });

});


// print user profile
$(document).ready(function () {
  $('#printProfileBtn').on('click', function () {
    alert('Work in progress')
      let profileContent = $('.profile_update');

      if (profileContent.length > 0) {
          let printWindow = window.open('', '_blank');
          printWindow.document.write('<html><head><title>Client Profile</title></head><body>');
          printWindow.document.write('<h1>Client Profile</h1>');
          printWindow.document.write(profileContent.html());
          printWindow.document.write('</body></html>');

          printWindow.document.close();
          printWindow.print();
      } else {
          console.error('Profile content not found');
      }
  });
});
