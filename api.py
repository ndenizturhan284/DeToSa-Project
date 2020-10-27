# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:42:33 2020

@author: Sami
"""

import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/createDress', methods=['POST'])
def create_dress():
    try:
        _json = request.json
        _dress_name = _json['dress_name']
        _dress_size = _json['dress_size']
        
        sqlQuery = "INSERT INTO dresses(dress_name, dress_size) VALUES(%s, %s)"
        sqlQuery2 = "select id from dresses where dress_name = %s"
        data = (_dress_name, _dress_size,)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)        
        cursor.execute(sqlQuery2, _dress_name)
        conn.commit()
        idd = cursor.fetchall()
        dress = {'id': idd,
        'dress_name': _dress_name,
        'dress_size': _dress_size,
        'available' : 1}
        res = jsonify({'dress':dress})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
@app.route('/createCustomer', methods=['POST'])
def create_customer():
    try:
        _json = request.json
        _first_name = _json['first_name']
        _last_name = _json['last_name']
        _phone_number = _json['phone_number']
        _size = _json['size']
        _wedding_date = _json['wedding_date']
        
        sqlQuery = "INSERT INTO customers(first_name, last_name, phone_number, size, wedding_date) VALUES(%s, %s, %s, %s, %s)"
        data = (_first_name, _last_name, _phone_number, _size, _wedding_date,)
        sqlQuery2 = "select max(id) from customers"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        cursor.execute(sqlQuery2)
        conn.commit()
        idd = cursor.fetchall()
        customer = {'id':idd,
        'first_name': _first_name,
        'last_name': _last_name}
        res = jsonify({'customer': customer})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/createReservation', methods=['POST'])
def create_reservation():
    try:
        _json = request.json
        _customer_id = _json['customer_id']
        _dress_id = _json['dress_id']
        _rent_date = _json['rent_date']
        
        sqlQuery = "INSERT INTO reservations(customer_id, dress_id, rent_date, return_on) VALUES(%s, %s, %s, %s)"
        sqlQuery2 = "select max(id) from reservations"
        data = (_customer_id, _dress_id, _rent_date, None,)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        cursor.execute(sqlQuery2)
        conn.commit()
        idd = cursor.fetchall()
        reservation = {
            'id': idd,
            'customer_id': _customer_id,
            'dress_id': _dress_id}
        res = jsonify({'reservation': reservation})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

			
@app.route('/dresses')
def dresses():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT sharks.id, sharks.dress_name, sharks.dress_size, COALESCE(sharks.available, 0 ) as available \
                        FROM ( \
	                        select dresses.id, dresses.dress_name, dresses.dress_size, \
	                        (max(reservations.return_on) > max(reservations.rent_date) or sum(reservations.id) is null) as available \
	                        from reservations \
	                        right join dresses \
	                        on reservations.dress_id = dresses.id \
	                        group by dresses.id) as sharks")
        rows = cursor.fetchall()
        res = jsonify({'dresses': rows})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
			
@app.route('/customers')
def customers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, first_name, last_name from customers")
        rows = cursor.fetchall()
        res = jsonify({'customers': rows})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/reservations')
def reservations():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, customer_id, dress_id from reservations")
        rows = cursor.fetchall()
        res = jsonify({'reservations': rows})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/return', methods=['POST'])
def update_status():
    try:
        _json = request.json
        _reservation_id = _json['reservation_id']
        _return_on = _json['return_on']
        
        sql = "update reservations set return_on = %s where id =%s"
        sql2 = "select dress_id from reservations where id = %s"
        data = (_return_on, _reservation_id,)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        cursor.execute(sql2, (_reservation_id,))
        idd = cursor.fetchall()
        conn.commit()
        res = jsonify({'dress_id': idd})
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
 

			
if __name__ == "__main__":
    app.run()