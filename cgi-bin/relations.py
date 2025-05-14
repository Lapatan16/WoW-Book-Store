import cgi
import json
from db import DB

req = cgi.FieldStorage()
print("Content-type: application/json\n")

db = DB()

if("login" in req):
    user = db.getUser(req.getvalue("user"), req.getvalue("pass"))

    if(user == None):
        print("<p id='message'>Username or password are incorect!</p>")
    else:
        print("<div id='user'>")
        userData = {}
        userData['id'] = user[0]
        userData['username'] = user[1]
        userData["email"] = user[2]
        userData["phone"] = user[3]
        userData["money"] = user[4]
        userData["ses_id"] = user[5]
        userData["password"] = user[6]

        print(json.dumps(userData))
        print("</div>")

if("checkLogin" in req):
    result = db.checkLogin(req["ses_id"].value)
    if(result):
        print("<p id='login'>Jeste</p>")       

if("logout" in req):
    db.refreshSessionId(req["user"].value, None)

if("register" in req):
    user = db.findUser(req["user"].value)

    if(user != None):
        print(f"<p id='message'>User with username {req["user"].value} already exists!</p>")
    else:
        db.addUser(req["user"].value, req["pass"].value, req["email"].value, req["phone"].value)

if("book" in req):
    print("<p id='nema'>Jeste</p>")
    books = db.getBooks()

    if(books):
        print("<div id='allBooks'>")
        allBooks = []
        for book in books:
            oneBook = {}
            oneBook["id"] = book[0]
            oneBook["title"] = book[1]
            oneBook["price"] = book[2]
            oneBook["image"] = book[3]
            oneBook["author"] = book[4]
            oneBook["year"] = book[5]
            allBooks.append(oneBook)
        print(json.dumps(allBooks))
        print("</div>")

if("cart" in req):
    cart = db.getCart(req["user"].value)
    if(cart):
        print("<div id='fullCart'>")
        allBooks = []
        for book in cart:
            oneBook = {}
            oneBook["id"] = book[0]
            oneBook["title"] = book[1]
            oneBook["price"] = book[2]
            oneBook["image"] = book[3]
            oneBook["author"] = book[4]
            oneBook["year"] = book[5]
            oneBook["cart_id"] = book[6]
            allBooks.append(oneBook)
        print(json.dumps(allBooks))
        print("</div>")

if("addToCart" in req):
    db.addToCart(req["addToCart"].value, req["user"].value)
    print("<p>Done</p>")

if("removeFromCart" in req):
    db.removeFromCart(req["removeFromCart"].value)
    print("<p>Done</p>")

if("checkout" in req):
    db.checkout(req['checkout'].value)
    db.transaction(req['user'].value, req['money'].value)
    print("<p>done</p>")

if("addMoney" in req):
    db.transaction(req['user'].value, req['addMoney'].value)
    print("<p>done</p>")
    
    