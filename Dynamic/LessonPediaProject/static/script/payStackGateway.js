$(document).ready(function(){

    function formatNumber(number) {
        return number.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    }

    var url = '/client/api/contractForm';
    var tutorId = $("#tutorId").text()
    var urltnx = `/client/transaction/details/${tutorId}`
    var paymentType = $("#paymentType")
    var email = $("#email").val()
    var csrfToken = $("#token").text()
    var contractID
    var payNowAmount
    var halfPayment
    var balance
    var amount
    var balanceAmount
   

    $.ajax({
        url: url,
        data: "data",
        dataType: "json",
        success: function (response) {
            console.log(response)
            amount = response[tutorId]["amount"]
            contractID = response[tutorId]['contractId']
            bal = response[tutorId]['amountRemaining']
            balance = formatNumber(parseFloat(bal))
            if (bal > 0){
                amount = bal
                $(".amount").text(`#${balance}`)
            }

            halfPayment = amount
            
            if (bal == response[tutorId]['amount']){
                paymentType.change(function(){
                    var selected = $(this).val()
                    if (selected === 'fullPayment'){
                        $("#amount").val("#" + amount)
                        $("#amount").prop("disabled", true)
                        $("#balance").val("NILL")
                        payNowAmount = amount
                    } else if (selected === 'partPayment'){
                        payNowAmount = amount
                        $("#balance").val("#" + 0)
                        $("#amount").prop("disabled", false).val(parseInt(amount))
                        $("#amount").on("input", function(){
                            var userAmount = $(this).val()
                            balanceAmount = amount - userAmount
                            $("#balance").val("#" + balanceAmount)
                            payNowAmount = userAmount
                            halfPayment = amount / 2
                        })
                    } else {
                        $("#amount").val("-- select paymentType --")
                        $("#amount").prop("disabled", true)
                        $("#balance").val("-- select paymentType --")
                    }
                })
            } else {
                paymentType.val("fullPayment")
                paymentType.prop("disabled", true)
                $("#amount").val("#" + amount)
                $("#amount").prop("disabled", true)
                $("#balance").val("NILL")
                payNowAmount = amount
            }
        }
    });
    

    var activeUser = $("#userName").text()
    $(".closeReview").click(function(){
        window.location.href = `/client/signIn/User_dashboard/${activeUser}`
    })


    function genran() {
        const min = 200000000000000; // Smallest 12-digit number
        const max = 299999999999999; // Largest 12-digit number
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    var referenceId = genran()
    $(".inlineP").text(referenceId)
    
    $('.pay_Now').click(function(){
        if ((paymentType.val() === "partPayment") || (paymentType.val() === 'fullPayment')){
            if (payNowAmount >= halfPayment){
                if ((balanceAmount >= 0) || (balanceAmount == undefined)){
                    amt = Math.round(payNowAmount * 100)
            
                    let refree = referenceId
                
                    let handler = PaystackPop.setup({
                        key: 'pk_test_18ed358a84c305a3340530bf43a9832fdef246f5',
                        email: email,
                        amount: amt,
                        currency: 'NGN',
                        ref: refree,
                        callback: function (response) {
                            var reference = response.reference;
                            dataDetails = {
                                "contractId": contractID,
                                "amount": payNowAmount,
                                "paymentType": paymentType.val(),
                                "referenceId": refree,
                                "transactionStatus": response.status,
                                "transactionMessage": response.message,
                                "transactionId": response.transaction,
                            }
                            
                            $.ajax({
                                method: "POST",
                                url: urltnx,
                                data: dataDetails,
                                dataType: "json",
                                headers: {
                                    'X-CSRFToken': csrfToken,
                                },
                                success: function (response) {
                                    console.log(response)
                                },
                                error: function (error) {
                                    console.log(error)
                                }
                            });
                            alert('Payment complete! Reference: ' + reference);
                            window.location.href = `/client/signIn/User_dashboard/${activeUser}`
                            // Make an AJAX call to your server with the reference to verify the transaction
                        },
                        onClose: function () {
                            alert('Transaction was not completed, window closed.');
                            
                        },
                    });
                    handler.openIframe(); 
                } else {
                    alert("Input amount must be less than or equal to total amount")
                }
            }else {
                alert("Input amount must be at least 50% of total amount")
            }
        } else {
            alert("Please select paymentType")
        }
    })


})
