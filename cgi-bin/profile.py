print(
    '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Profile</title>
        <script src="../script/script.js"></script>
        <link rel="icon" href="../images/logo.jpg"></link>
        <link rel="stylesheet" href="../style/home.css">
        <link rel="stylesheet" href="../style/profile.css">
    </head>
    <body onload="showProfile(), checkUser()">

        <video id="background-video" autoplay loop muted poster="../images/background.png">
            <source src="../images/wowVideo.mp4" type="video/mp4">
        </video>

        <header id="header">        
            <div id="logout">
                <p>User: <span id="user"></span></p>
            </div>
        </header>

        <nav>
            <div><a class="active" href="profile.py">My Profile</a></div>
            <div><a href="home.py">Shop</a></div>
            <div><a href="cart.py" id="a-cart">Cart</a></div>
            <div><button onclick="logout()">Log Out</button></div>
        </nav>
        
        <div id="profile">
            
        </div>
        
        <footer style="position: absolute; bottom: 0;">
        

        </footer>
        
    </body>
    </html>
    '''
)