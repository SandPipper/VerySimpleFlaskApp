/*$(document).ready(function() {
  $('#submit').click(function() {
    var first_name = $('#first_name').val();
    var surname = $('#surname').val();
    $.ajax({
      url: '/new_person',
      data: $('form').serialize(),
      type: 'POST',
      success: function(respose) {
        console.log(response);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });
});
$(document).ready(function() {
  $("#Add_personForm").bind('submit', function(e) {
    e.preventDefault();
    var ajax=$.ajax({
      type: "POST",
      data: $("#Add_personForm").serialize(),
      url: "/new_person"
    }).done(function(data){
      console.log('done!')
    });
    ajax.fail(function(data){
      console.log('error!')
    });
  });
});
*/
$(document).ready(function() {
  $("#Add_personForm").bind('submit', function(e) {
    e.preventDefault();
    var ajax=$.ajax({
      type: "POST",
      data: $("#Add_personForm").serialize(),
      url: "/new_person/"
    }).done(function(data){
      if(data.status === 1) {
        $("#results").removeClass()
          .addClass("alert alert-success")
          .text("Person is successfuly added!")
          .show();
        } else {
        $("#results").addClass("alert alert-danger")
          .text("Must be more characters in the fields!")
          .show();
      };
    });
    ajax.fail(function(data){
      console.log('error!');
  });
  });
});
