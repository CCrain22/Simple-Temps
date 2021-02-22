import kivy
import sys
from kivy.app import App
from kivy.uix.label import Label

text = ''
true_false = False
if true_false == True:
    text = 'variable is true :D'
else:
    text = 'variable is false D:'

class MyApp(App):
    def build(self):
        return Label(text=text, font_size=30)


if __name__ == '__main__':
    MyApp().run()