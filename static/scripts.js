$(document).ready(function() {
  $("#form").submit(function(e) {
    var formdata = $('#form').serialize();
    event.preventDefault()
    $.ajax({
      type: 'POST',
      url: '/go',
      data: formdata,
      dataType: "text",
      success: function (data) {
        var json = JSON.parse(data);
        console.log(json);
        $("img").css("display", "inline");
      }
    });
  });
});

$(document).ready(function() {
  $('#textarea').keyup(function() {
    var length = $("#textarea").val().length;
    if (length == 0) {
      $('#characters').text('');
    } else {
      $('#characters').text(length);
    }
  });
});
