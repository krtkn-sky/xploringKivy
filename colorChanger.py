from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Red2Green(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        label = Label(text="Click rapidly to trigger !",
                      font_size=30)

        button = Button(text="Let's Go !",
                        background_color=(1, 0, 0, 1),
                        size_hint=(1,0.3))
        button.bind(on_press=self.induce_epilepsy)

        layout.add_widget(label)
        layout.add_widget(button)

        return layout
    
    def induce_epilepsy(self, instance):
        current_color = instance.background_color
        threshold = 0.001

        if all(abs(a - b) < threshold for a, b in zip(current_color, (1, 0, 0, 1))):
            instance.background_color = (0, 1, 0, 1)
        elif all(abs(a - b) < threshold for a, b in zip(current_color, (0, 1, 0, 1))):
            instance.background_color = (0, 0, 1, 1)
        elif all(abs(a - b) < threshold for a, b in zip(current_color, (0, 0, 1, 1))):
            instance.background_color = (1, 0, 0, 1)

if __name__ == "__main__":
    Red2Green().run()
