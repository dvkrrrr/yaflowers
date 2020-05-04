from flask import Flask, render_template, request
from flask_script import Manager, Command
import sqlite3
from app import my_db
app = Flask(__name__)
manager = Manager(app)
app.debug = True
PATH_TO_DB = "db/db_of_orders.sqlite"





@app.route('/')
def index():
    con = sqlite3.connect("bouquet.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM bouquets""").fetchall()
    count = len(result)
    result1 = cur.execute("""SELECT * FROM flowers""").fetchall()
    count1 = len(result1)
    result2 = cur.execute("""SELECT * FROM beauty""").fetchall()
    count2 = len(result2)
    return render_template('index.html', name=result, count=count, name1=result1, count1=count1, name2=result2, count2=count2)


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@app.route('/send.php', methods=['post', 'get'])
def books():
    if request.method == 'POST':
        s = request.form['a']
        if s != 0:
            my_db.global_init(PATH_TO_DB)
            session = my_db.create_session()
            f1 = session.query(my_db.Products).filter(my_db.Products.id == s).first()
            f1.orders += 1
            session.commit()
        return 'Заказ успешно оформлен'


@app.route('/login/', methods=['post', 'get'])
def login():
    con = sqlite3.connect("bouquet.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM bouquets""").fetchall()
    count = len(result)
    return render_template('login.html', name=result, count=count)


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
