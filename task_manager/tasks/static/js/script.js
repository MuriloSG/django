$(document).ready(function () {
  var baseUrl = "http://127.0.0.1:8000/";
  var deleteBtn = $(".delete-task");
  var searchForm = $(".search-form");
  var searchBtn = $(".search-btn");
  var filter = $("#taskFilter");

  $(deleteBtn).on("click", function (e) {
    e.preventDefault();

    var delLink = $(this).attr("href");
    var result = confirm("Quer deletar esta tarefa?");

    if (result) {
      window.location.href = delLink;
    }
  });

   $(searchBtn).on("click", function () {
     searchForm.submit();
   });
  
  $(filter).change(function () {
    var filterValue = $(this).val();
    window.location.href = baseUrl + "?filter=" + filterValue;
  });
});
