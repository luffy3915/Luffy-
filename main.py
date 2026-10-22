from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='مرحباً بك في Kivy!')

if __name__ == '__main__':
    MyApp().run()
