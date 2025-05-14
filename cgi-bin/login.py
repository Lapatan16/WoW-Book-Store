print(
    '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <link rel="icon" href="../images/logo.jpg"></link>
        <link rel="stylesheet" href="../style/login.css">
        <script src="../script/script.js" defer></script>
    </head>
    <body onload="checkLogin()" style="height:100vh;">

        <video id="background-video" autoplay loop muted poster="../images/background.png">
            <source src="../images/wowVideo.mp4" type="video/mp4">
        </video>

        <div id="box">

            <label for="username">Username:</label>
            <br/>
            <input onkeyup="loginHandler(event)" type="text" id="username" name="username" required>
            <br/>
            <label class="passLabel" for="password">Password:</label>
            <br/>
            <input onkeyup="loginHandler(event)" type="password" id="password" name="password" required>

            <p style="color:red;" id="message"></p>

            <p>Don't have an account?</p>
            <a href="registration.py">Register here</a>
            <br/>
            
            <button onclick="login()">Log in</button>
            
        </div>

    </body>
    </html>
    '''
)