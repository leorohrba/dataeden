
// Prevent text from being dragged
document.addEventListener('dragstart', function(event) {
    event.preventDefault();
});

// Prevent text from being copied
document.addEventListener('copy', function(event) {
    event.preventDefault();
});

let mybutton = $("#scrollTop");
// window.onscroll = function() { scrollFunction() };
$(window).scroll(function() { scrollFunction() });

function scrollFunction() {
    // if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    // $( window ).on( "scroll", function() {
        if ($(window).scrollTop()) {
            // mybutton.show();
            mybutton.fadeIn();
            // mybutton.addClass('d-flex');
        } else {
            // mybutton.style.display = "none";
            // mybutton.removeClass('d-flex');
            mybutton.fadeOut();
            // mybutton.hide();
        }
    // } );
}
// $("body")

$(window).scroll(function() {
    if(window.scrollY==0){
        // mybutton.removeClass('d-flex');
        mybutton.fadeOut();
        //user scrolled to the top of the page
    }
    // if($(window).scrollTop() + $(window).height() == $(document).height()) {
    //     alert("bottom!");
    // }
});

function scrollToTop() {
    $(window).scrollTop(0);
    // mybutton.hide();
    // mybutton.fadeOut();
}