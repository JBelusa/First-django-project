const loginPopup = document.getElementById("login-pop-up-form");
const loginAuthButton = document.getElementById("login-auth-button");
const loginForm = document.getElementById("login-form");

// Add an event listener to the button
loginAuthButton.addEventListener("click", function () {
  // Open the popup form
  loginPopup.style.display = "block";
});

// Add an event listener to the form submit event
document
  .getElementById("login-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch("/login", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          // Login successful, close the popup
          loginForm.style.display = "none";
          loginPopup.style.display = "none";
          window.location.reload();
        } else {
          // Login failed, show an error message in the popup
          var errorMessage = document.getElementById("error-message");
          errorMessage.textContent = data.message;
          errorMessage.style.display = "block";
        }
      })
      .catch((error) => {
        console.error(error);
        // Handle unsuccessful fetch requests here
      });
  });

// Add an event listener to the document (window) to close the popup when clicking outside of it
document.addEventListener("click", function (event) {
  if (
    !event.target.closest("#login-pop-up-form") &&
    !event.target.matches("#login-auth-button")
  ) {
    // Close the popup form
    loginPopup.style.display = "none";
  }
});
