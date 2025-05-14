print(
    '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration</title>
        <link rel="icon" href="../images/logo.jpg"></link>
        <link rel="stylesheet" href="../style/registration.css">
        <script src="../script/script.js" defer></script>
    </head>
    <body style="height:100vh;">

        <video id="background-video" autoplay loop muted poster="../images/background.png">
            <source src="../images/wowVideo.mp4" type="video/mp4">
        </video>

        <div id="box">
            <label for="username">Username:</label>
            <br/>
            <input type="text" id="username" name="username" required>
            <br/>
            <label for="email">Email:</label>
            <br/>
            <input type="email" id="email" name="email" required>
            <br/>
            <label for="phone">Phone number:</label>
            <br/>
            <input type="text" id="phone" name="phone-number">
            <br/>
            <label for="password">Password:</label>
            <br/>
            <input type="password" id="password" name="password" required>
            <br/>
            <label for="password-conf">Confirm password:</label>
            <br/>
            <input type="password" id="password-conf" name="confirm-password" required>

            <p style="color:red;" id="message"></p>

            <p>Already have an account? <a href="login.py">Login here</a></p>
            <button onclick="register()">Register</button>

        </div>
    </body>
    </html>
    '''
)