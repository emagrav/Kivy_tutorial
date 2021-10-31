from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App


class MainWindow(BoxLayout):
    pass

# il nome della classe deve iniziare con Main come il file .kv
# può anche chiamarsi, quindi, semplicemente Main
class MainApp(App):
    def build(self):
        return MainWindow()

sample_app = MainApp()
sample_app.run()