from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Primary(BoxLayout):
    def test(self):
        print("O botão foi clicado")


class TestApp(App):
    def build(self):
        return Primary()
