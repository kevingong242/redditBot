$(function(){
   //$('#display_threads').text('that new new');
    $.getJSON("/pythonBot/threads_found.json", function(data){
        $.each(data, function(key,value){
            $('.myList').append('<li>' + data[key].title + '<br><a href="' + data[key].url +'">' + data[key].url + '</a></li>');
        });
    });
});