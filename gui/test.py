from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Primary(BoxLayout):
    ...


class TestApp(App):
    def build(self):
        return Primary()
