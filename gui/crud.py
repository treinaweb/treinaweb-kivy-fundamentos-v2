from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from db import Session
from db.models import Client


class Screem(BoxLayout):
    def add_client(self):
        name = self.ids.name.text
        age = self.ids.age.text

        with Session() as session:
            session.add(Client(name=name, age=age))
            session.commit()

        self.ids.name.text = ''
        self.ids.age.text = ''


class CrudApp(App):
    def build(self):
        return Screem()