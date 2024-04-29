from flask import Flask
import warnings
import os
from flask import request
from flask import Response
from flask_cors import cross_origin
from flask import jsonify
from MySQL_job import *

warnings.simplefilter(action='ignore', category=FutureWarning)
app = Flask(__name__)

class FooException(Exception):
    """ Binds optional status code and encapsulates returing Response when error is caught """
    def __init__(self, *args, **kwargs):
        code = kwargs.pop('code', 400)
        Exception.__init__(self)
        self.code = code

    def as_http_error(self):
        return Response(str(self), self.code)

@app.route('/')
@cross_origin()
def index():
    return 'index_page'

@app.route('/register', methods=["POST"])
@cross_origin()
def register():
    try:
        mysql_job_object = mysql_object()
        data = request.get_json()
        print(data)
        registered = mysql_job_object.check_register_record(data)
        print(registered[0][0])
        if registered[0][0] == 0:
            mysql_job_object.register_user(data)
        register_response = {
            'name': data['name'],
            'password': data['password'],
            'phone_number': data['phone_number'],
            'register_success': registered[0]}
        return register_response
    except FooException as ex:
        return ex.as_http_error()

@app.route('/login', methods=["POST"])
@cross_origin()
def login():
    try:
        mysql_job_object = mysql_object()
        data = request.get_json()
        result = mysql_job_object.check_user(data)
        print(result)
        if len(result) == 0:
            login_response = {
                'name': '',
                'password': 'nouser'
            }
            return login_response
        login_response = {
            'name': data['name'],
            'password': result[0][1]
            }
        return login_response
    except FooException as ex:
        return ex.as_http_error()

@app.route('/book_list', methods=["GET"])
@cross_origin()
def book_list():
    try:
        mysql_job_object = mysql_object()
        result = mysql_job_object.book_list()
        print(result)
        return result
    except FooException as ex:
        return ex.as_http_error()

@app.route('/buy_new_book', methods=["POST"])
@cross_origin()
def buy_new_book():
    try:
        mysql_job_object = mysql_object()
        data = request.get_json()
        print(data)
        result = mysql_job_object.buy_new_book(data)
        return 'purchase_success'
    except FooException as ex:
        return ex.as_http_error()

@app.route('/show_user_purchase_record', methods=["POST"])
@cross_origin()
def show_user_purchase_record():
    try:
        mysql_job_object = mysql_object()
        data = request.get_json()
        result = mysql_job_object.show_user_purchase_record(data)
        print(result)
        return result
    except FooException as ex:
        return ex.as_http_error()

@app.route('/delete_purchase_record', methods=["POST"])
@cross_origin()
def delete_purchase_record():
    try:
        mysql_job_object = mysql_object()
        data = request.get_json()
        print(data)
        result = mysql_job_object.delete_purchase_record(data)
        return result
    except FooException as ex:
        return ex.as_http_error()