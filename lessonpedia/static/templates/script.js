$(document).ready(function() {
    $('#sortForm').submit(function(event) {
      event.preventDefault(); // Prevents the default form submission
  
      const selectedOption = $('#sortOptions').val();
  
      switch (selectedOption) {
        case 'newest':
          sortTable(0, 'desc'); // Sort by Date column (assuming it's the second column) in descending order
          break;
        case 'oldest':
          sortTable(0, 'asc'); // Sort by Date column in ascending order
          break;
        case 'ascending':
          sortTable(2, 'asc'); // Sort by Amount Paid column (assuming it's the third column) in ascending order
          break;
        case 'descending':
          sortTable(2, 'desc'); // Sort by Amount Paid column in descending order
          break;
        default:
          break;
      }
    });
  
    function sortTable(column, order) {
      const table = $('#dataTable');
      const rows = table.find('tbody > tr').get();
  
      rows.sort(function(a, b) {
        const A = $(a).children('td').eq(column).text().toUpperCase();
        const B = $(b).children('td').eq(column).text().toUpperCase();
  
        if (order === 'asc') {
          return A.localeCompare(B);
        } else {
          return B.localeCompare(A);
        }
      });
  
      $.each(rows, function(index, row) {
        table.children('tbody').append(row);
      });
    }
  });
  