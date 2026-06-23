$('#drop').css('display', 'none');
$('#cancel').css('display', 'none');
$('#menu').click(function(){$('#drop').show()})
            .click(function(){$('#cancel').show()});
$('#cancel').click(function(){$('#drop').hide()})
            .click(function(){$(this).hide()});
$('a').mouseover(function(){$(this).css('text-decoration','underline')})
     .mouseout(function(){$(this).css('text-decoration','none')});

