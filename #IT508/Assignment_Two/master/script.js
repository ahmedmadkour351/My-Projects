function checkPassword() {
    let pass = document.getElementById
        ("pass").value;
    let confpass = document.getElementById
        ("confpass").value;
    console.log(pass, confpass);
    let message = document.getAnimations.getElementById
        ("massage");
    if (pass.length != 0) {
        if (pass == confpass) {
            message.textContent = "Password match";
            message.style.backgroundcolor = "#3ae374";
        }
        else {
            message.textContent = "Password Don't match";
            message.style.backgroundcolor = "#ff4d4d";
        }
    }
    else {
        alert("password cant't be empty!");
        message.textContent = "";
    }
}