$('body').on('click', '.apavolku-galocksed', function(){
    if ($(this).is(':checked')){
    $('#Password1').attr('type', 'text');
    $('#Password2').attr('type', 'text');
    } else {
    $('#Password1').attr('type', 'password');
    $('#Password2').attr('type', 'password');
    }
  });