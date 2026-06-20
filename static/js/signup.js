document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector(".signup-form");

    form.addEventListener("submit", (event) => {

        const username = document.getElementById("username").value.trim();
        const firstName = document.getElementById("first_name").value.trim();
        const lastName = document.getElementById("last_name").value.trim();
        const age = document.getElementById("age").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (
            username === "" ||
            firstName === "" ||
            lastName === "" ||
            age === "" ||
            email === "" ||
            password === ""
        ) {
            alert("Please fill all fields");
            event.preventDefault();
        }
    });

});