# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:36:56 2018

@author: umer
"""
from flask import Flask
import os
from urllib import parse
import psycopg2



app = Flask(__name__)


@app.route('/')
def use():
    try:
        parse.uses_netloc.append("postgres")
        url = parse.urlparse(os.environ["DATABASE_URL"])

        conn = psycopg2.connect( database=url.path[1:],    user=url.username,    password=url.password, host=url.hostname, port=url.port )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test1 (id serial PRIMARY KEY, qa text, ans text);") 
        print("sucessfull")
    except:
        print("failed")
    return 'Hello World!'


@app.route('/qa/<question>', methods=['GET', 'POST'])

def qa(question):
    #print('%s'%question)
    # show the user profile for that user
    
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect( database=url.path[1:],    user=url.username,    password=url.password, host=url.hostname, port=url.port )
    cur = conn.cursor()
        
    cur.execute("INSERT INTO test2 (qa) VALUES (%s)", (str(question)))
 #       print("sucessfull")
  
  
    return 'question is  %s' % question


@app.route('/ans/<answer>', methods=['GET', 'POST'])
def ans(answer):
    # show the user profile for that user
    return 'answer is  %s' % answer

if __name__ == '__main__':
    app.run()
