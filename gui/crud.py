from sqlalchemy import select
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

from db import Session
from db.models import Client


class ClientButton(ToggleButton):
    def __init__(self, client_id, client_name, client_age, **kwargs):
        super().__init__(**kwargs)
        self.client_id = client_id
        self.text = f'{client_name} - {client_age}'
        self.group = 'clients'


class Screem(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_clients()

    def add_client(self):
        name = self.ids.name.text
        age = self.ids.age.text

        with Session() as session:
            session.add(Client(name=name, age=age))
            session.commit()

        self.ids.name.text = ''
        self.ids.age.text = ''
        self.list_clients()

    def list_clients(self):
        self.ids.clients.clear_widgets()

        with Session() as session:
            clients = session.execute(select(Client)).scalars().all()

        for client in clients:
            self.ids.clients.add_widget(
                ClientButton(client.id, client.name, client.age)
            )


class CrudApp(App):
    def build(self):
        return Screem()