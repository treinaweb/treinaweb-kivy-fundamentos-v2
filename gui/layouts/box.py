from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Screem(BoxLayout):
    ...


class BoxApp(App):
    def build(self):
        return Screem()
