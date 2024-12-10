from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Screem(BoxLayout):
    ...


class CrudApp(App):
    def build(self):
        return Screem()