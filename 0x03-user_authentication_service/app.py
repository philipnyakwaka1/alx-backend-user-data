#!/usr/bin/env python3

from flask import Flask
from sqlalchemy import create_engine, Column, ForeignKey
import os

engine = create_engine(f'mysql+mysqldb://{DB_USER}:{PASSWORD}@{HOST}/{DB}')
app = Flask(__name__)

@app.route('/')
def home_page():
    return f'Hello World'

if __name__ == '__main__':
    app.run(debug=True)