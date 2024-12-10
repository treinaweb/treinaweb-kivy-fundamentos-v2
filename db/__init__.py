from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql://root:root@127.0.0.1/curso_kivy")

Session = sessionmaker(bind=engine)