from kivy.app import App
from kivy.lang import Builder

NAMES = ["Bob", "Harry", "John", "Alex", "Mike"]

class LoopNames(App):
    def build(self):
        self.title = "Loop Names"
        self.root = Builder.load_file('loop_labels.kv')
        return self.root

    def create_label(self):
        pass

    def handle_names(self):
        for name in NAMES:
            button = Button(text=name, id=name)
            button.bind(on_release=self.press_entry)
        pass


LoopNames().run()
