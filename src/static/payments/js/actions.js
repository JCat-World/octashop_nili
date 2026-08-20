$(document).ready(function(){
    function getCSRFToken() {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, 10) == ('csrftoken' + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue;
    };
    var fd = new FormData();
    const dataForUpload = {};
    $("#payment-img-box").on("click",function(){
        var fileDialog = $("<input type='file' accept='image/*'/>");
        fileDialog.click();
        fileDialog.on("change",function(){
            const file = $(this)[0].files[0]
            fd.append("img",file )
            fd.append("action", "post")
            fd.append("order", $("#order_id").attr("value"))
            $("#payment-img-box").html(`<img class="img-uploaded" src='${URL.createObjectURL(file)}' alt='تصویر رسید واریز'>`)
            $("#text-receipt-upload").css("display","none")
            $("#bt-payment-done").css("display","block")
        });
        return false;
    });
    $("#bt-payment-done").on("click", function(){
        $.ajax({
            url: '../upload-receipt/',
            method :"POST",
            headers: {
                'X-CSRFToken': getCSRFToken(),
            },
            data: fd,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            caches: false,
            success: function(response){
                if (response.status == "success") {
                    alert("خرید شما با موفقیت تکمیل شد.لطفا منتظر تایید سفارش از سمت فارس ماسل بمانید.")
                    location.reload()
                } else {
                    alert("لطفا مجددا تلاش نمایید.")
                    location.reload()
                }
            },
            error: function(xhr, errmsg, err){
            }
        })
    })
})



// 