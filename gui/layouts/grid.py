from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Screem(GridLayout):
    ...


class GridApp(App):
    def build(self):
        return Screem()
