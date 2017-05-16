$(function() {
$('.persons').on('click', function() {
  var persons = this;
  var persons_id = $(this).attr('data-id');
  $.ajax({
    type:'DELETE',
    url: '/delete' + '/' + persons_id,
    context: persons,
    success:function(result) {
      if(result.status === 1) {
        $(this).remove();
        console.log(result);
      }
    }
  });
});

});
