from kivy.app import App
from kivy.uix.stacklayout import StackLayout


class Screem(StackLayout):
    ...


class StackApp(App):
    def build(self):
        return Screem()
