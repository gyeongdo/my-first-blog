$(document).ready(function(){

    $('#next').on("click",function(){
        $.scrollify.enable();
    });

    $('#next1').on("click",function(){
        $.scrollify.disable();
    });

    $(window).scroll(function () {
        var height = $(document).scrollTop();
    });

    $(function() {
        $.scrollify({
          section : ".example-classname",
          interstitialSection : ".page-header"
        });
    });

    function log(str){
        $('#log').text(str);
    }

}); 