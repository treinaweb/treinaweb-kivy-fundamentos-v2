from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Screem(FloatLayout):
    ...


class FloatApp(App):
    def build(self):
        return Screem()
