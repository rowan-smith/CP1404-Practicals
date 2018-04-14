from kivy.app import App
from kivy.uix.button import Label


class LoopNamesApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["John", "Harry", "Alex", "Bob", "Bill"]

    def build(self):
        self.title = "Loop Names"
        self.create_widgets()

    def create_widgets(self):
        for name in self.names:
            label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(label)

LoopNamesApp().run()
