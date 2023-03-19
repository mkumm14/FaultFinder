
document.addEventListener('click', function (event) {
    if (event.target.closest('#sidebarToggle')) {
        event.preventDefault();
        document.body.classList.toggle('sb-sidenav-toggled');
        localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
    }
});