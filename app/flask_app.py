from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from app import my_db
from app.forms import LoginForm
import os
from flask import Flask
from flask_mail import Mail, Message

SECRET_KEY = os.urandom(64)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.debug = True
PATH_TO_DB = "db/db_of_orders.sqlite"
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'danurabotai@gmail.com'
app.config['MAIL_PASSWORD'] = 'yegfxbve'

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    con = sqlite3.connect("bouquet.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM bouquets""").fetchall()
    count = len(result)
    result1 = cur.execute("""SELECT * FROM flowers""").fetchall()
    count1 = len(result1)
    result2 = cur.execute("""SELECT * FROM beauty""").fetchall()
    count2 = len(result2)


    return render_template('index.html', name=result, count=count, name1=result1, count1=count1, name2=result2,
                           count2=count2)


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

@app.route('/succcess', methods=['GET', 'POST'])
def succcess():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        address = form.address.data
        date = form.date.data
        return redirect(url_for('success', username=username, address=address, date=date))
    return render_template('succcess.html', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    username = request.args.get('username', None)
    address = request.args.get('address', None)
    date = request.args.get('date', None)
    send_email("уведомление о заказе", sender='danurabotai@gmail.com', recipients=[username],
               text_body=render_template("message.txt",
                                         address=address, date=date),
               html_body=render_template("message.txt",
                                         address=address, date=date))
    return 'Message Sent'


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


if __name__ == "__main__":
    app.run()
