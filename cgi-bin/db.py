import sqlite3
import hashlib
import random
import json

class DB():

    def __init__(self):
        self.connection = None

        try:
            self.connection = sqlite3.connect("projectDB.db")
        except sqlite3.Error as e:
            print(e)
        
    def refreshSessionId(self, userId, sesId):
        sql = "UPDATE user SET ses_id = ? WHERE id = ?;"
        query = self.connection.cursor()
        query.execute(sql, (sesId, userId))
        self.connection.commit()
        query.close()

    def getUser(self, username, password):
        sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest()
        random_number = random.randint(10**13, 10**14-1)

        sql = "SELECT * FROM user WHERE username = ? AND password = ?;"
        query = self.connection.cursor()
        query.execute(sql, (username, sha1))

        result = query.fetchone()
        query.close()

        if(result and result[5] == None):
            self.refreshSessionId(result[0], random_number)
            sql = "SELECT * FROM user WHERE username = ? AND password = ?;"
            query = self.connection.cursor()
            query.execute(sql, (username, sha1))
            result = query.fetchone()
            query.close()
        
        return result
    
    def findUser(self, username):
        sql = "SELECT * FROM user WHERE username=?;"
        query = self.connection.cursor()
        query.execute(sql, (username, ))
        result = query.fetchone()
        query.close()
        return result
    
    def addUser(self, user, password, email, phone):
        sql = "INSERT INTO user(username, password, email, phone, money) values(?, ?, ?, ?, 0);"
        query = self.connection.cursor()
        sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest()
        query.execute(sql, (user, sha1, email, phone))
        self.connection.commit()
        query.close()

    def checkLogin(self, ses_id):
        sql = "SELECT * FROM user WHERE ses_id = ?;"
        query = self.connection.cursor()
        query.execute(sql, (ses_id, ))
        result = query.fetchone()
        query.close()
        return result
    
    def getBooks(self):
        sql = "SELECT * FROM book;"
        query = self.connection.cursor()
        query.execute(sql)
        result = query.fetchall()
        query.close()
        return result
    
    def getCart(self, user):
        sql = "SELECT b.*, c.id as cart_id FROM cart c join book b on c.book_id = b.id WHERE c.user_id = ?;"
        query = self.connection.cursor()
        query.execute(sql, (user, ))
        result = query.fetchall()
        query.close()
        return result
    
    def addToCart(self, book, user):
        sql = "INSERT INTO cart(book_id, user_id) values(?, ?);"
        query = self.connection.cursor()
        query.execute(sql, (book, user))
        self.connection.commit()
        query.close()

    def removeFromCart(self, cart):
        sql = "DELETE FROM cart WHERE id = ?;"
        query = self.connection.cursor()
        query.execute(sql, (cart, ))
        self.connection.commit()
        query.close()

    def checkout(self, user):
        sql = "DELETE FROM cart WHERE user_id = ?;"
        query = self.connection.cursor()
        query.execute(sql, (user, ))
        self.connection.commit()
        query.close()

    def transaction(self, user, money):
        sql = "UPDATE user SET money = ? WHERE id = ?;"
        query = self.connection.cursor()
        query.execute(sql, (money, user))
        self.connection.commit()
        query.close()