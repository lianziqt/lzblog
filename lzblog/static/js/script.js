$(function () {
    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    );
});

$(document).ready(function(){
    $(".card").mouseover(function(){

        $(this).css({"box-shadow":'5px 5px 20px #cec8c8'});
      });
    $(".card").mouseout(function(){
        $(this).css({"box-shadow":''});
      });
    $("pre").addClass("p-3 mb-2");
    $(".flask-pagedown-preview").addClass("p-3 mb-2 bg-light text-dark");
      
})
