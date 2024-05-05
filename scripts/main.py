from scripts.gui import Windows


class Main:

    def __init__(self):
        self.open_main_window()

    def open_main_window(self):
        self.window = Windows()
        self.window.show()
