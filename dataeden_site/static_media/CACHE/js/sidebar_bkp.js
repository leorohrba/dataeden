let initialTop = 0;
let navbarHeight; // Declare navbarHeight using let
let isResizing = false; // Flag to indicate resizing

function updateSidebarClass(sidebar, initialTop) {
    const scrollPosition = window.scrollY;

    if (scrollPosition >= initialTop) {
        sidebar.classList.remove('not-fixed');
        sidebar.classList.add('fixed');
    } else {
        sidebar.classList.remove('fixed');
        sidebar.classList.add('not-fixed');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');

    function calculateInitialTop() {
        navbarHeight = document.documentElement.clientHeight - window.innerHeight;
        initialTop = sidebar.getBoundingClientRect().top + window.scrollY - navbarHeight;
    }

    function handleScroll() {
        updateSidebarClass(sidebar, initialTop);
    }

    function handleLoadOrResize() {
        calculateInitialTop();
        handleScroll();
    }

    window.addEventListener('load', handleLoadOrResize);
    window.addEventListener('scroll', handleScroll);

    // Calculate initialTop when the sidebar is loaded
    sidebar.addEventListener('load', calculateInitialTop);
    // Calculate initialTop when the window is resized
    window.addEventListener('resize', () => {
        if (!isResizing) {
            isResizing = true;
            requestAnimationFrame(() => {
                isResizing = false;
                handleLoadOrResize();
            });
        }
    });
    
    // Calculate initialTop when the script is first executed
    calculateInitialTop();
});