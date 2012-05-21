$(document).ready(function(){
    $('.statistic section h2').toggle(
        function(){
            var dh = $(this).parent('section').find('.down').innerHeight();
            $(this).parent('section').find('.down-block').animate({'height':dh},500,function() {$(this).css('height','auto');});
            $(this).addClass('active');
        },
         function(){
            var h2 = $(this);
            $(this).parent('section').find('.down-block').animate({'height':0},500,function() {h2.removeClass('active');});
    });
});