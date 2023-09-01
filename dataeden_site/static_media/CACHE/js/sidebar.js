let initialTop = 0;
let navbarHeight; // Declare navbarHeight using let
let isResizing = false; // Flag to indicate resizing

function updateSidebarClass(sidebar, initialTop) {
    const scrollPosition = window.scrollY;

    if (scrollPosition >= initialTop && (window.innerWidth > 320)) {
        sidebar.classList.toggle('not-fixed', false);
        sidebar.classList.toggle('fixed', true);
    } else {
        sidebar.classList.toggle('fixed', false);
        sidebar.classList.toggle('not-fixed', true);
    }
}

function calculateInitialTop() {
    navbarHeight = document.documentElement.clientHeight - window.innerHeight;
    initialTop = sidebar.getBoundingClientRect().top + window.scrollY - navbarHeight;
}

function handleScroll() {
    updateSidebarClass(sidebar, initialTop);
}

function handleLoadOrResize() {
    if (!sidebar.classList.contains('fixed')) {
        calculateInitialTop();
        handleScroll();
    }
    if (window.innerWidth > 320) {
        const fixedElement = document.querySelector('#sidebar');
        const parentWidth = document.querySelector('#sidebar-parent').offsetWidth;
    
        fixedElement.style.maxWidth = parentWidth + 'px';
    } else {
        sidebar.classList.toggle('fixed', false);
        sidebar.classList.toggle('not-fixed', true);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');

    window.addEventListener('load', handleLoadOrResize);
    window.addEventListener('scroll', handleScroll);

    // Calculate initialTop when the sidebar is loaded
    sidebar.addEventListener('load', calculateInitialTop);

    // Debounce the resize event
    let debounceTimeout;
    window.addEventListener('resize', () => {
        if (!isResizing) {
            isResizing = true;
            clearTimeout(debounceTimeout);
            debounceTimeout = setTimeout(() => {
                isResizing = false;
                handleLoadOrResize();
            }, 250); // Adjust the debounce delay as needed
        }
    });

    // Calculate initialTop when the script is first executed
    calculateInitialTop();
});
