import mysql.connector
import json

class mysql_object():
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root', password='123456', host='mysql', database='Automate')
        self.cursor = self.conn.cursor()
    def check_register_record(self,user_info):
        self.cursor.execute(f"SELECT count(*) FROM User_info where name = '{user_info['name']}'" )
        result = self.cursor.fetchall()
        return result
    def register_user(self,user_info):
        sql = f"""INSERT INTO User_info(
           NAME, PASSWORD, PHONE_NUMBER)
           VALUES (%s, %s, %s)"""
        values = (user_info['name'], user_info['password'], user_info['phone_number'])
        self.cursor.execute(sql,values)
        self.conn.commit()
    def check_user(self,user_info):
        self.cursor.execute(f"SELECT * FROM User_info where name = '{user_info['name']}'" )
        result = self.cursor.fetchall()
        return result
    def book_list(self):
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute(f"SELECT * FROM Book_info" )
        result = self.cursor.fetchall()
        return json.dumps(result)
    def buy_new_book(self,purchase_info):
        sql = f"""INSERT INTO Booking_record(
            NAME, TITLE, PRICE)
            VALUES (%s, %s, %s)"""
        values = (purchase_info['name'],purchase_info['title'],purchase_info['price'])
        self.cursor.execute(sql, values)
        self.conn.commit()
    def show_user_purchase_record(self,show_info):
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute(f"SELECT * FROM Booking_record where name = '{show_info['name']}'" )
        result = self.cursor.fetchall()
        return json.dumps(result)
    def delete_purchase_record(self,delete_info):
        self.cursor.execute(f"DELETE FROM Booking_record where record_number = {delete_info['record_number']}" )
        self.conn.commit()
        return "delete_success"
