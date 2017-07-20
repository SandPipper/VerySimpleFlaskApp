import 'bootstrap-loader';
import '../css/style.css';
import './delete';


$(document).ready(function() {
  $("#Add_personForm").bind('submit', function(e) {
    e.preventDefault();

    var ajax = $.ajax({
      type: "POST",
      data: $("#Add_personForm").serialize(),
      url: "/new_person/",
      error: function(error) {
        console.log(error);
      }

    }).done(function(data){
      if(data.status === 1) {
        $("#results").hide(100)
          .removeClass()
          .addClass("alert alert-success results")
          .text("Person is successfuly added!")
          .show(500)
          .slideUp(1250);

      } else if(data.status === 0) {
        $("#results").hide(100)
          .addClass("alert alert-danger results")
          .text("Must be from 2 to 20 characters in the fields!")
          .show(500)
          .slideUp(1250);
      };

      console.log(data)

    });
    ajax.fail(function(data){
      console.log('error!');
  });
  });
});
