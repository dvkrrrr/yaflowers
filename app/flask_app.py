from flask import Flask, render_template, request, redirect
import sqlite3
from app import my_db
from app.forms import LoginForm
import os

SECRET_KEY = os.urandom(64)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.debug = True
PATH_TO_DB = "db/db_of_orders.sqlite"


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
    count2 = len(result2)
    return render_template('index.html', name=result, count=count, name1=result1, count1=count1, name2=result2, count2=count2)


@app.route('/admins')
def admin():
    my_db.global_init(PATH_TO_DB)
    session = my_db.create_session()
    bouquet1 = session.query(my_db.Products).filter(my_db.Products.id == 1).first()
    bouquet2 = session.query(my_db.Products).filter(my_db.Products.id == 2).first()
    bouquet3 = session.query(my_db.Products).filter(my_db.Products.id == 3).first()
    bouquet4 = session.query(my_db.Products).filter(my_db.Products.id == 4).first()
    bouquet5 = session.query(my_db.Products).filter(my_db.Products.id == 5).first()
    bouquet6 = session.query(my_db.Products).filter(my_db.Products.id == 6).first()
    bouquet7 = session.query(my_db.Products).filter(my_db.Products.id == 7).first()
    bouquet8 = session.query(my_db.Products).filter(my_db.Products.id == 8).first()
    your_bouquet = session.query(my_db.Products).filter(my_db.Products.id == 9).first()

    return render_template('admin.html', bouquet1=bouquet1.orders, bouquet2=bouquet2.orders,
                           bouquet3=bouquet3.orders, bouquet4=bouquet4.orders,
                           bouquet5=bouquet5.orders, bouquet6=bouquet6.orders,
                           bouquet7=bouquet7.orders, bouquet8=bouquet8.orders,
                           your_bouquet=your_bouquet.orders)




if __name__ == "__main__":
    app.run()
