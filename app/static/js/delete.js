$(function() {
$('.persons').on('click', function() {
  var person = this;
  var person_id = $(this).attr('data-id');
  $.ajax({
    type:'DELETE',
    url: '/delete' + '/' + person_id,
    context: person,
    success:function(result) {
      if(result.status === 1) {
        $(this).remove();
        console.log(result);
      }
    }
  });
});

});
