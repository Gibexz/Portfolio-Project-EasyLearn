// function updateTutorCount() {
//     // $(document).ready(function() {
//         $.getJSON('http://127.0.0.1:8000/appAdmin/api/get_tutor_count/', function (data) {
//             $("#tutorCount").text(data.tutor_count)
//         });
//     // }) 
// }


function updateTutorCount() {
    $.ajax({
        url: 'http://127.0.0.1:8000/appAdmin/api/get_tutor_count/', // URL to fetch tutor count from the server
        type: 'GET',
        success: function(response) {
            $('#tutorCount').text(response.tutorCount); // Update the HTML with the fetched count
        },
        error: function(xhr, status, error) {
            console.error(error); // Handle errors if any
        }
    });
}

$('#registerBtn').on('submit', function() {
    updateTutorCount();
})

$('#registerBtn').on('click', function() {
    updateTutorCount();
})