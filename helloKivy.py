from kivy.app import App
from kivy.uix.label import Label

class HelloKivy(App):
    def build(self):
        return Label(text="Hello Kivy!!")

if __name__ == "__main__":
    HelloKivy().run()