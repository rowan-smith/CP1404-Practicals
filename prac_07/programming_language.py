class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        string = "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name,
                                                                             self.typing,
                                                                             self.reflection,
                                                                             self.year)
        return string

    def is_dynamic(self):
        return self.typing == "Dynamic"
