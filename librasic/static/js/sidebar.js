const sidebarToggle = document.getElementById('searchToggle');
const mainDivCol = document.getElementById('main-div-col');
const sidebar = document.getElementById('sidebar');

function manuallyToggleSidebarClasses() {
    sidebar.classList.toggle('search-sidebar-toggle');
    sidebar.classList.toggle('manually-toggled');
}
function adjustMainDivCol() {
    if (window.innerWidth > 768) {
        mainDivCol.classList.add('col-10');
        mainDivCol.classList.remove('col-12');
        sidebar.style.display = 'block';
    } else {
        mainDivCol.classList.add('col-12');
        mainDivCol.classList.remove('col-10');
        if (!sidebar.classList.contains('manually-toggled')) {
            sidebar.classList.add('search-sidebar-toggle');
            sidebar.style.display = 'none';
        }
    }
}

// Create a MutationObserver instance
const observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
        if (mutation.attributeName === "class") {
            if (window.innerWidth <= 768 && sidebar.classList.contains('search-sidebar-toggle') && !sidebar.classList.contains('manually-toggled')) {
                sidebar.style.display = 'none';
            } else {
                sidebar.style.display = 'block';
            }
        }
    });
});

// Call adjustMainDivCol on page load and window resize
window.addEventListener('resize', adjustMainDivCol);
window.addEventListener('load', adjustMainDivCol);
sidebarToggle.addEventListener('click', manuallyToggleSidebarClasses);
// Start observing the target node for configured mutations
observer.observe(sidebar, { attributes: true });