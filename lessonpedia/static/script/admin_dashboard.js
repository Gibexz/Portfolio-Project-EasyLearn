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
});