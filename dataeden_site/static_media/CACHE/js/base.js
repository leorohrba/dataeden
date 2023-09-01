
// Prevent text from being dragged
document.addEventListener('dragstart', function(event) {
    event.preventDefault();
});

// Prevent text from being copied
document.addEventListener('copy', function(event) {
    event.preventDefault();
});

$(document).ready(function() {
    let mybutton = $("#scrollTop");

    // Function to check for overlap
    function checkOverlap(buttonRect, textRect) {
        return (
            buttonRect.left < textRect.right &&
            buttonRect.right > textRect.left &&
            buttonRect.top < textRect.bottom &&
            buttonRect.bottom > textRect.top
        );
    }

    $(window).scroll(function() {
        if ($(window).scrollTop()) {
            mybutton.fadeIn();
        } else {
            mybutton.fadeOut();
        }
    });

    $(window).scroll(function() {
        if (window.scrollY == 0) {
            mybutton.fadeOut();
        }
    });

    mybutton.click(function() {
        $(window).scrollTop(0);
    });

    let overlapped = false;

    $(window).scroll(function() {
        const buttonRect = mybutton[0].getBoundingClientRect();

        $("p").each(function(index) {
            const textRect = $(this)[0].getBoundingClientRect();
            const overlap = checkOverlap(buttonRect, textRect);

            if (overlap) {
                overlapped = true;
                mybutton.addClass("transparent");
                // console.log(`Button is overlapping text ${index + 1}.`);
            } else if (!overlapped){
                mybutton.removeClass("transparent");
                // console.log(`Button is not overlapping text ${index + 1}.`);
            }
        });
        overlapped = false;
    });
});  // end of document ready

// function checkButtonHoveringText() {
//     let buttonRect = mybutton[0].getBoundingClientRect();
//     let textElements = document.querySelectorAll('p');

//     let isHoveringText = Array.from(textElements).some(textElement => {
//         let textRect = textElement.getBoundingClientRect();
//         return (
//             buttonRect.top >= textRect.top &&
//             buttonRect.bottom <= textRect.bottom &&
//             buttonRect.left >= textRect.left &&
//             buttonRect.right <= textRect.right
//         );
//     });

//     if (isHoveringText) {
//         mybutton.addClass('transparent');
//     } else {
//         mybutton.removeClass('transparent');
//     }
// }

// function scrollToTop() {
//     $(window).scrollTop(0);
// }