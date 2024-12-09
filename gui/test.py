from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty


class Primary(BoxLayout):
    primary_label_text = StringProperty('Minha label')
    primary_label_font_size = NumericProperty(20)

    def test(self):
        print("O botão foi clicado")
        self.primary_label_text = 'O botão foi clicado'
        self.primary_label_font_size += 5


class TestApp(App):
    def build(self):
        return Primary()
