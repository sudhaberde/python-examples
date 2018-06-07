import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import  FloatLayout


class MyApp(App):

    def build(self):
        f =FloatLayout()
        s =Scatter()

        l = Label(text='Hello world')
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == '__main__':


    MyApp().run()