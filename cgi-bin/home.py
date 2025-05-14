print(
    '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
        <script src="../script/script.js" defer></script>
        <link rel="icon" href="../images/logo.jpg"></link>
        <link rel="stylesheet" href="../style/home.css">
        <link rel="stylesheet" href="../style/books.css">
    </head>
    <body onload="loadBooks(), checkUser()">

        <video id="background-video" autoplay loop muted poster="../images/background.png">
            <source src="../images/wowVideo.mp4" type="video/mp4">
        </video>
        
        <header>
            <div id="logout">
                <p>User: <span id="user"></span></p>
            </div>
        </header>
        
        <nav>
            <div><a href="profile.py">My Profile</a></div>
            <div><a class="active" href="home.py">Shop</a></div>
            <div><a href="cart.py" id="a-cart">Cart</a></div>
            <div><button onclick="logout()">Log Out</button></div>
        </nav>

        <div id="main">
            <div id="input-div">
                <div>
                        <label for="search">Search by name: </label> 
                    <input type="text" id="search" onkeyup="updateBooks()">
                </div>

                <div>
                    <p id="aut" style="display: inline-block;">Authors: </p>
                    <select id="autSelect" onchange="updateBooks()">
                        <option selected value='all'>All</option>
                    </select>
                </div>
            </div>

            <div id="books">

            </div>
        </div>

        <footer id="footer-home">
        
        </footer>

    </body>
    </html>
    '''
)