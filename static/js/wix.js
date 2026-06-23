$('.sign').mouseover(function(){$(this).css('background-color','blue')})
.mouseout(function(){$(this).css('background-color','green')});
$('a').mouseover(function(){$(this).css('text-decoration', 'underline')})
.mouseout(function(){$(this).css('text-decoration', 'none')});
$('#about').css('display', 'none');
$('#menu').click(function(){$('#about').toggle()});
$('.content').not('#menu').click(function(){$('#about').hide()});
$('#opt_b').css('display','none');
$('#categories').mouseover(function(){$('#opt_b').toggle()})

$('body').not('#categories').mouseover(function(){$('#opt_b').hide()});



