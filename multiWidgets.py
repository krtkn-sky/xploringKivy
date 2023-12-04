from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MultiWidgets(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=(10, 5, 10, 5))

        label = Label(text="Drop your username below")
        text_input = TextInput(text="Your username goes here")

        def on_click(instance):
            label.text = "Submission Successful !"

        button = Button(text="Submit!", size_hint=(None, None), width=200, height=50)
        button.bind(on_press=on_click)

        # Center the button horizontally and vertically
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(button)

        return layout

if __name__ == "__main__":
    MultiWidgets().run()
