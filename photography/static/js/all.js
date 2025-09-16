document.addEventListener('DOMContentLoaded', function () {
    // Get the start and end times from the HTML element data attributes
    var startTimeElement = document.getElementById("start_time");
    var endTimeElement = document.getElementById("end_time");

    if (startTimeElement && endTimeElement) {
        var startTime = new Date(startTimeElement.getAttribute("data-time")).getTime();
        var endTime = new Date(endTimeElement.getAttribute("data-time")).getTime();

        // Ensure the end time is correctly set to the next midnight (00:00:00)
        var currentDate = new Date();
        var nextMidnight = new Date(currentDate);
        nextMidnight.setHours(24, 0, 0, 0);  // Set it to the next midnight

        endTime = nextMidnight.getTime();

        console.log("Parsed Start Time: " + startTime);
        console.log("Parsed End Time: " + endTime);

        function updateCountdown() {
            var currentTime = new Date().getTime();
            var remainingTime = endTime - currentTime;  // Countdown to the endTime (next midnight)

            var hours = Math.floor((remainingTime / (1000 * 60 * 60)) % 24);
            var minutes = Math.floor((remainingTime / (1000 * 60)) % 60);
            var seconds = Math.floor((remainingTime / 1000) % 60);

            var formattedTime = (hours < 10 ? "0" : "") + hours + ":" +
                                (minutes < 10 ? "0" : "") + minutes + ":" +
                                (seconds < 10 ? "0" : "") + seconds;

            // Display the countdown on the page
            document.getElementById("countdown").innerHTML = formattedTime;

            // If the countdown reaches the end time (midnight), stop the countdown
            if (remainingTime <= 0) {
                clearInterval(interval);
                document.getElementById("countdown").innerHTML = "00:00:00";
            }
        }

        // Start the countdown immediately
        var interval = setInterval(updateCountdown, 1000);
    } else {
        console.error("Start time or end time element not found.");
    }
});

// Function to toggle the mobile menu
function toggleMenu() {
    const mobileMenu = document.getElementById("mobile-menu");
    const burgerMenu = document.getElementById("burger-menu");
    const closeMenu = document.getElementById("close-menu");

    mobileMenu.classList.toggle("hidden");

    // Toggle the burger and close menu visibility
    burgerMenu.style.display = mobileMenu.classList.contains("hidden") ? "block" : "none";
    closeMenu.style.display = mobileMenu.classList.contains("hidden") ? "none" : "block";
}

// Function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    const modeIcon = document.getElementById("mode-icon");

    // Toggle dark mode on the body element
    body.classList.toggle('dark');

    // Save the theme to localStorage
    const theme = body.classList.contains('dark') ? 'dark' : 'light';
    localStorage.setItem('theme', theme);

    // Update the icon based on the mode
    if (theme === 'dark') {
        modeIcon.classList.remove("fa-moon");
        modeIcon.classList.add("fa-sun");
    } else {
        modeIcon.classList.remove("fa-sun");
        modeIcon.classList.add("fa-moon");
    }
}

// On page load, check for stored theme and apply it
window.onload = () => {
    const storedTheme = localStorage.getItem('theme');
    const body = document.body;
    const modeIcon = document.getElementById("mode-icon");

    // Apply the stored theme if present
    if (storedTheme === 'dark') {
        body.classList.add('dark');
        modeIcon.classList.remove("fa-moon");
        modeIcon.classList.add("fa-sun");
    } else {
        body.classList.remove('dark');
        modeIcon.classList.remove("fa-sun");
        modeIcon.classList.add("fa-moon");
    }

    // Ensure the mobile menu is hidden initially
    const mobileMenu = document.getElementById("mobile-menu");
    const burgerMenu = document.getElementById("burger-menu");
    const closeMenu = document.getElementById("close-menu");

    mobileMenu.classList.add("hidden");
    burgerMenu.style.display = "block";
    closeMenu.style.display = "none";
};
