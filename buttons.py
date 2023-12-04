from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ButtonClick(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Hello World !")

        def on_click(instance):
            label.text="Button Clicked !"

        button = Button(text="Click me !", size_hint=(1,0.2))
        button.bind(on_press=on_click)

        layout.add_widget(label)
        layout.add_widget(button)

        return layout
    
if __name__ == "__main__":
    ButtonClick().run()