document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (e) {
            const username = form.querySelector('input[name="usr"]').value;
            const password = form.querySelector('input[name="pwd"]').value;

            if (!username || !password) {
                e.preventDefault();
                alert("Please enter both username and password.");
            }
        });
    }
    if (window.location.href.includes("account") && window.location.search.includes("redirect")) {
        window.location.href = "/app"; // Redirect to /app after successful login
      }
});
