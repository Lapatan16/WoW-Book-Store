function login()
{
    let username = document.getElementById("username")
    let password = document.getElementById("password")

    if(username.value != "" && password.value != "")
    {
        let xhttp1 = new XMLHttpRequest()

        xhttp1.onreadystatechange = function()
        {
            if(this.readyState == 4 && this.status == 200)
            {
                let parser = new DOMParser();
                let doc = parser.parseFromString(this.responseText, "text/html");
                let message = doc.getElementById("message");

                if(message)
                    message = message.innerHTML;
                else
                    message = "";

                let user_data = doc.getElementById("user")

                if(user_data)
                {
                    user_data = JSON.parse(user_data.innerHTML);
                    
                    setCookie("ses_id",user_data.ses_id,1);
                    setCookie("id",user_data.id,1);
                    setCookie("username",user_data.username,1);
                    setCookie("email",user_data.email,1);
                    setCookie("phone",user_data.phone,1);
                    setCookie("money", (parseFloat(user_data.money)).toFixed(2),1);
                    window.location.href = "home.py";
                }

                document.getElementById("message").innerHTML = message
            }
        }

        xhttp1.open("GET", "relations.py?login=1&user=" + username.value + "&pass=" + password.value, true)
        xhttp1.send();
    }
    else
    {
        document.getElementById("message").innerHTML = "Please enter a username and password!";
    }
}

function logout()
{
    let xhttp = new XMLHttpRequest()

    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            setCookie("ses_id",1,-1);
            setCookie("id",1,-1);
            setCookie("username",1,-1);
            setCookie("email",1,-1);
            setCookie("phone",1,-1);
            setCookie("money",1,-1);
            window.location.href = "login.py";
        }
    }

    xhttp.open("GET", "relations.py?logout=1&user=" + getCookie("id"), true)
    xhttp.send()
}

function setCookie(cname, cvalue, exdays) 
{
    const date = new Date();
    date.setTime(date.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ date.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";";
}

function getCookie(name) 
{
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) 
    {
        const [cookieName, cookieValue] = cookie.trim().split('=');
        if (cookieName === name)
            return decodeURIComponent(cookieValue);
    }
    return null;
}

function checkLogin()
{
    let ses_id = getCookie("ses_id");
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {            
            let parser = new DOMParser();
            let doc = parser.parseFromString(this.responseText, "text/html");
            let login = doc.getElementById("login");
            
            if(login)
                window.location.href = "home.py";
        }
    }

    xhttp.open("GET", "relations.py?checkLogin=1&ses_id=" + ses_id, true);
    xhttp.send();
}

function checkRegex(username, pass1, pass2, email, phone)
{
    if(username == "" || pass1 == "" || pass2 == "" || email == "" || phone == "")
        return "All fields must be filled!";
    
    const userReg = /^[a-zA-Z][a-zA-Z0-9]{3,10}$/;
    const passReg = /^[a-zA-Z0-9]{6,20}$/;
    const emailReg = /^[a-zA-Z0-9][a-zA-Z0-9\_\-\.]{1,}\@[a-z]{3,7}\.com$/;
    const phoneReg = /^[0-9]{10}$/;
    
    if(!userReg.test(username))
        return "Username invalid!";
    if(!emailReg.test(email))
        return "Email invalid!";
    if(!phoneReg.test(phone))
        return "Phone number invalid!";
    if(!passReg.test(pass1))
        return "Password invalid!";
    if(pass1 != pass2)
        return "Passwords don't match!";
    return "1";
}

function register()
{
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const passwordConf = document.getElementById("password-conf").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;

    let regex = checkRegex(username, password, passwordConf, email, phone)
    if(regex !== "1")
    {
        document.getElementById("message").innerHTML = regex;
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            let parser = new DOMParser()
            let doc = parser.parseFromString(this.responseText, "text/html")
            let message = doc.getElementById("message")
            if(message)
                document.getElementById("message").innerHTML = message.innerHTML;
            else
                window.location.href = "login.py";
        }
    }
    xhttp.open("GET", "relations.py?register=1&user=" + username + "&pass=" + password + "&email=" + email + "&phone=" + phone, true);
    xhttp.send();
}

function loginHandler(event)
{
    console.log(event.key);
    
    if(event.key === "Enter")
        login()
}

let books;

function loadBooks()
{
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            let parser = new DOMParser()
            let doc = parser.parseFromString(this.responseText, "text/html")
            books = doc.getElementById("allBooks");

            if(books)
            {
                books = JSON.parse(books.innerHTML)
                let authors = [];
                for(let book of books)
                {
                    if(authors.indexOf(book.author) == -1)
                        authors.push(book.author)
                }
                addAuthors(authors);
                updateBooks();
            }
        }
    }

    xhttp.open("GET", "relations.py?book=1" , true);
    xhttp.send();
}

function updateBooks()
{
    let bookDiv = document.getElementById("books");
    bookDiv.innerHTML = "";
    for(const book of books)
    {
        if(!filters(book))  continue;
        let div = document.createElement("div");
        div.className = "book";
        div.innerHTML = 
        `
            <div class="bookTitle"><h2>${book.title}</h2></div>
            <img src="${book.image}">
            <p>${book.author}</p>
            <p>${book.year}</p>
            <p>${book.price}$</p>
            <button value="${book.id}" onclick="addToCart(this)">Add to cart</button>
        `
        bookDiv.appendChild(div);
    }
}

function filters(book)
{
    let search = document.getElementById("search");
    let aut = document.getElementById("autSelect");
    let reg = new RegExp(search.value, 'i');
    let boolSearch = search.value == '' || reg.test(book.title);
    let boolAuthor = aut.value == "all" || book.author == aut.value;

    return boolSearch && boolAuthor;
}

function addAuthors(aut)
{
    let selAut = document.getElementById("autSelect");
    for (const it of aut) 
    {
        selAut.innerHTML +=
        `
            <option value="${it}">${it}</option>
        `
    }
}

function checkUser()
{
    let user = getCookie("username");
    if(user)
        document.getElementById("user").innerHTML = user;
}

function showProfile()
{
    let profile = document.getElementById("profile");
    profile.innerHTML = 
    `
        <p>Username: ${getCookie("username")}</p>
        <p>Email address: ${getCookie("email")}</p>
        <p>Phone number: ${getCookie("phone")}</p>
        <p>Balance: ${getCookie("money")}$</p>
        <button id="addMoneyButton" onclick="addMoney()">Update balance</button>
    `;
}

let cart;

function loadCart()
{
    const user = getCookie("id");

    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            let parser = new DOMParser()
            let doc = parser.parseFromString(this.responseText, "text/html")
            cart = doc.getElementById("fullCart");

            if(cart)
            {
                cart = JSON.parse(cart.innerHTML)
            }
            updateCart();
        }
    }

    xhttp.open("GET", "relations.py?cart=1&user=" + user, true)
    xhttp.send()
}

function updateCart()
{
    let cartDiv = document.getElementById("cart");
    cartDiv.innerHTML = "";
    if(!cart)
    {
        cartDiv.innerHTML = 
        `
            <div class="total">
                <p>Cart is empty</p>
            </div>
        `;
        return;
    }

    let books = [];
    let bookIds = [];

    for(book of cart)
    {
        if(bookIds.indexOf(book.id) == -1)
        {
            bookIds.push(book.id);
            let obj = 
            {
                cartId: book.cart_id,
                quantity: 1,
                image: book.image,
                title: book.title,
                price: book.price,
            }
            books.push(obj);
        }
        else
            books[bookIds.indexOf(book.id)].quantity++;
        
    }
    let total = 0;
    for(book of books)
    {
        total += book.price * book.quantity;
        let wrapper = document.createElement("div");
        wrapper.className = "wrapper";
        wrapper.innerHTML += 
        `
            <div class="left">
                <p>${book.quantity}x </p>
                <img src="${book.image}">
                <p>${book.title}</p>
            </div>

            <div class="right">
                <p>${book.price}$</p>
                <button value="${book.cartId}" onclick="removeFromCart(this)">Remove</button>
            </div>
        `
        cartDiv.appendChild(wrapper);
    }

    cartDiv.innerHTML += 
    `
        <div class="total">
            <p>Total: ${total.toFixed(2)}$</p>
            <button value="${total}" onclick="checkout(this)">Checkout</button>
        </div>
    `
}

function addToCart(button)
{
    const user = getCookie("id");
    const book = button.value;

    let xhttp = new XMLHttpRequest()
    xhttp.open("GET", "relations.py?addToCart="+ book +"&user=" + user, true)
    xhttp.send()
}

function removeFromCart(button)
{
    const cart = button.value;

    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
            loadCart();
    }
    xhttp.open("GET", "relations.py?removeFromCart="+ cart +"&user=" + user, true)
    xhttp.send()
}

function checkout(button)
{
    const user = getCookie("id");
    let money = getCookie("money");
    const price = button.value;
    
    if(parseFloat(money) < price)
    {
        alert("You dont have enough money!");
        return;
    }
    money = money - price;
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            setCookie("money",1,-1);
            setCookie("money",money,1);
            loadCart();
        }
    }
    xhttp.open("GET", "relations.py?checkout="+ user + "&money=" + money + "&user=" + user, true)
    xhttp.send()
}

function addMoney()
{
    const user = getCookie('id');
    let money = prompt("Enter how much money you wish to upload");    
    if(!money || isNaN(money) || money < 0)
        return;
    
    let balance = getCookie("money");
    money = parseFloat(money);
    money += parseFloat(balance);

    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            setCookie("money",1,-1);
            setCookie("money",money,1);
            location.reload();
        }
    }
    xhttp.open("GET", "relations.py?addMoney="+ money + "&user=" + user, true)
    xhttp.send()
}