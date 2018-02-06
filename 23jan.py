# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:36:56 2018

@author: umer
"""
from flask import Flask
import os
from urllib import parse
import psycopg2
from psycopg2 import sql
import re, math
from textblob import TextBlob
from collections import Counter
import operator


app = Flask(__name__)


@app.route('/')
def use():
    try:
        parse.uses_netloc.append("postgres")
        url = parse.urlparse(os.environ["DATABASE_URL"])
        conn = psycopg2.connect( database=url.path[1:],    user=url.username,    password=url.password, host=url.hostname, port=url.port )
        print("sucessfull")
    except:
        print("failed")
    return 'Hello World!'


@app.route('/qa/<question>', methods=['GET', 'POST'])

def qa(question):
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect( database=url.path[1:],    user=url.username,    password=url.password, host=url.hostname, port=url.port )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS qa11 ( qa text);")
    cur.execute(sql.SQL("insert into {} values (%s)").format(sql.Identifier('qa11')),[question])
    return 'question is  %s' % question


@app.route('/ans/<answer>', methods=['GET', 'POST'])
def ans(answer):
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect( database=url.path[1:],    user=url.username,    password=url.password, host=url.hostname, port=url.port )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ans11 ( ans text);")
    cur.execute(sql.SQL("insert into {} values (%s)").format(sql.Identifier('ans11')),[answer])
    return 'answer is  %s' % answer

@app.route('/query/<query>', methods=['GET', 'POST'])
def query(query):
    #conn = psycopg2.connect("dbname='db1' user='postgres' password='umer'")
    #cur = conn.cursor()
    
    text1 = 'I like cat'
    text2 = 'I like dog'
    try:
        dis1=float(get_cosine(str(text1),str(text1)))
        print(dis1)
        #float first=get_cosine(text1,text2)
        #print(first)
        #float secnd=DistJaccard(text1, text2)
       # print(secnd)
    except:
        
        print("cosine failed")
        
    try:
        dis2=float(DistJaccard(str(text1),str(text1)))
        print(dis2)
        #float first=get_cosine(text1,text2)
        #print(first)
        #float secnd=DistJaccard(text1, text2)
       # print(secnd)
    except: 
        print("jack failed")  
        
    return 'query is  %s' % query



WORD = re.compile(r'\w+')
def get_cosine(vec1, vec2):
    vec1 = Counter(WORD.findall(vec1))
    vec2 = Counter(WORD.findall(vec2))

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def DistJaccard(str1, str2):
    str1 = set(str1.split())
    str2 = set(str2.split())
    return float(len(str1 & str2)) / len(str1 | str2)


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def remove_spell_errors(text):
    b = TextBlob(text)
    return b.correct()



if __name__ == '__main__':
    app.run()
