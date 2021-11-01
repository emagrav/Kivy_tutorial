from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button



class MainWindow(BoxLayout):
    # qui specifico l'id dell'oggetto che si trova subito sotto la 
    # definizione di <MainWindow> nel file kv che voglio accedere
    submit_button: ObjectProperty(None)
    nome: ObjectProperty(None)
    cognome: ObjectProperty(None)
    data_di_nascita: ObjectProperty(None)
    luogo_di_nascita: ObjectProperty(None)

    def invia_form(self):
        # modifico la proprietà text del button
        self.submit_button.text = "Form inviato"
        riga = f"Sig./Sig.ra {self.nome.text} {self.cognome.text} nato/a il {self.data_di_nascita.text} a {self.luogo_di_nascita.text}"
        print("Riga:", riga)
        with open("form.txt",'w') as f:
            f.write(riga)


# il nome della classe deve iniziare con Main come il file .kv
# può anche chiamarsi, quindi, semplicemente Main
class MainApp(App):
    def build(self):
        return MainWindow()

sample_app = MainApp()
sample_app.run()