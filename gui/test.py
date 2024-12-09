from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")

        button = Button(text="Meu botão")
        label = Label(text="Minha label")

        layout.add_widget(label)
        layout.add_widget(button)

        return layout