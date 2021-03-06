import sys
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from random import random

class PaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random())
            d = 50.
            Ellipse(pos=(touch.x -d /2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points =(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class Paint(App):
    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        Clearbtn = Button(text='Clear')
        Clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(Clearbtn)
        return parent
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    Paint().run()