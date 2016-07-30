$(document).ready(function(){

  $('div#z2').click(function(e){
    var myClass = this.className;
    var id = myClass.slice(-1);
    var target = 'div#z3.green'+id;
    $('div#z3').not($(target)).hide();
    $(target).show();
    document.getElementById('mod1').value = id
    document.getElementById('mod2').value = id
  });

  $('.green1').click(function(){
    $(this).hide();
    document.getElementById('mod').value = ""
  });
  $('.green2').click(function(){
    $(this).hide();
    document.getElementById('mod').value = ""
  });
  $('.green3').click(function(){
    $(this).hide();
    document.getElementById('mod').value = ""
  });

  if($('div#z4').is(":visible")){
    $('div#z5').show();
  }

  $('div#z5').click(function(e){
    var myClass = this.className;
    var id = myClass.slice(-1);
    var target = 'div#z3.green'+id;
    $('div#z3').not($(target)).hide();
    $(target).show();
    document.getElementById('mod1').value = id
    document.getElementById('mod2').value = id
  });



});
