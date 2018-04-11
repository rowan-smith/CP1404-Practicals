from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConverterApp(App):
    def build(self):
        Window.size = (200, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_increment(self, value):
        mile_value = int(numerical_error_handle(self.root.ids.input_label.text))
        mile_value += int(value)
        self.root.ids.input_label.text = str(mile_value)

    def convert_miles_to_kilometres(self):
        try:
            mile_value = int(self.root.ids.input_label.text)
        except ValueError:
            mile_value = int(numerical_error_handle(self.root.ids.input_label.text))
        kilometres = mile_value * MILES_TO_KM
        self.root.ids.output_label.text = "{0:.3f}".format(kilometres)


def numerical_error_handle(number):
    try:
        if int(number):
            if int(number) < 1:
                return int(0)
            return int(number)
    except ValueError:
        return int(0)

ConverterApp().run()
