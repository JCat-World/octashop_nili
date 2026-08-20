function showModalSearch() {
  document.getElementById("showModalSearch").style.display = "block";
  document.getElementById("opacitiScreen").style.display = "block";
}
function closeScreen() {
  document.getElementById("showModalSearch").style.display = "none";
  document.getElementById("opacitiScreen").style.display = "none";
}

$(document).ready(function(){

  const srchbx = $("#srchbx")
  $("#default-search").on("keyup", function(){
    srchbx.html("")
    var searchValue = $(this).val();

    $.ajax({

      url : `/api/front/product/products/?q=${searchValue}`,
      type : 'GET',
      data : {},
      // dataType:'json',
      success : function(response) {      
          // <img
          //   src="{% static 'base/image/product/bag.png' %}"
          //   alt=""
          //   class="w-14 rounded-lg ml-2"
          // />
        for (key in response) {
          console.log(key)
          $("#srchbx").append(`
              <a href="/product/${response[key].id}" class="flex items-center bg-white p-2 rounded-xl">
          
          <div class="text-xs opacity-70">${response[key].product_name}</div>
        </a>
              `)
            ;
        }
          


          
      },
      error : function(request,error)
      {
          alert("Request: "+JSON.stringify(request));
      }
  });

  })
  
})
