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

    def _do_release(self, *args):
        Screem().select_client(self.client_id)
        return super()._do_release(*args)


class Screem(BoxLayout):
    client_id = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_clients()

    def select_client(self, client_id):
        Screem.client_id = client_id

    def add_client(self):
        with Session() as session:
            session.add(Client(name=self.__get_name(), age=self.__get_age()))
            session.commit()

        self.__clean_fields()
        
        self.list_clients()

    def list_clients(self):
        self.ids.clients.clear_widgets()

        with Session() as session:
            clients = session.execute(select(Client)).scalars().all()

        for client in clients:
            self.ids.clients.add_widget(
                ClientButton(client.id, client.name, client.age)
            )

    def delete_client(self):
        with Session() as session:
            client = session.get(Client, Screem.client_id)
            session.delete(client)
            session.commit()

        self.list_clients()

    def update_client(self):
        with Session() as session:
            client = session.get(Client, Screem.client_id)
            client.name = self.__get_name()
            client.age = self.__get_age()
            session.commit()

        self.__clean_fields()

        self.list_clients()

    def __get_name(self):
        return self.ids.name.text
    
    def __get_age(self):
        return self.ids.age.text
    
    def __clean_fields(self):
        self.ids.name.text = ''
        self.ids.age.text = ''


class CrudApp(App):
    def build(self):
        return Screem()