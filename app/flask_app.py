from flask import Flask, render_template, request, redirect
import sqlite3
from app.forms import LoginForm
import os

SECRET_KEY = os.urandom(64)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    con = sqlite3.connect("bouquet.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM bouquets""").fetchall()
    count = len(result)
    result1 = cur.execute("""SELECT * FROM flowers""").fetchall()
    count1 = len(result1)
    result2 = cur.execute("""SELECT * FROM beauty""").fetchall()
    count2 = len(result2)
    return render_template('index.html', name=result, count=count, name1=result1, count1=count1, name2=result2,
                           count2=count2, form=form)


if __name__ == "__main__":
    app.run()
