import os
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
from flask import Flask, render_template, request
import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
PATH_TO_DB = "db/db_of_orders.sqlite"



SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)



    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


class Products(SqlAlchemyBase):
    __tablename__ = 'db_of_orders'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    orders = sqlalchemy.Column(sqlalchemy.Integer)



def add_user(session):
    user = Products()
    user.name = "bouquet1"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet2"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet3"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet4"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet5"
    user.price = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet6"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet7"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "bouquet8"
    user.orders = 0
    session.add(user)
    session.commit()

    user = Products()
    user.name = "your_bouquet"
    user.orders = 0
    session.add(user)
    session.commit()


def main():
    # проверим существует ли файл с базой
    new_base = not os.path.exists(PATH_TO_DB)
    global_init(PATH_TO_DB)
    session = create_session()
    # если файла не было, то необходимо добавить пользователя
    if new_base:
        add_user(session)


if __name__ == '__main__':
    main()
    app.run()
