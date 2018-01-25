# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:36:56 2018

@author: umer
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def use():
    return 'Hello World!'


@app.route('/qa/<question>', methods=['GET', 'POST'])

def qa(question):
    #print('%s'%question)
    # show the user profile for that user
    return 'question is  %s' % question


@app.route('/ans/<answer>', methods=['GET', 'POST'])
def ans(answer):
    # show the user profile for that user
    return 'answer is  %s' % answer

if __name__ == '__main__':
    app.run()
