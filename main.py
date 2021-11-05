from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


# il popup non è un sotto oggetto di MainWindow ma un altro oggetto
# per questo definiamo una classe e, parallelamente, nel file kv
# creiamo il suo layout
class CustomPopup(Popup):
    accettato_invio_form = ObjectProperty(None)

    def dismiss_popup(self):
        self.dismiss()

class MainWindow(BoxLayout):
    # qui specifico l'id dell'oggetto che si trova subito sotto la 
    # definizione di <MainWindow> nel file kv che voglio accedere
    submit_button = ObjectProperty(None)
    nome = ObjectProperty(None)
    cognome = ObjectProperty(None)
    data_di_nascita = ObjectProperty(None)
    luogo_di_nascita = ObjectProperty(None)

    def conferma_invio_form(self):
        # creo il popup: size_hint come al solito vuole la larghezza (size_hint_x) e l'altezza 
        # (size_hint_y) in percentuale rispetto al genitore, in questo caso MainWindow
        # poi faccio l'associazione tra la variabile di classe "accettato_invio_form" del popup,
        # che corrisponde al pulsante "Invia", ed il metodo invia form di questa stessa classe 
        # così che nel layout di popup (file kv) possa richiamarla per il tramite proprio di 
        # accettato_invio_form che deve essere richiamato nel file kv come una funzione perché 
        # kivy dopo questa associazione crea un metodo corrispondente con lo stesso nome
        custom_popup = CustomPopup(title="Conferma invio form"
                                , size_hint=(.5, .4), accettato_invio_form=self.invia_form)
        # apro il popup
        custom_popup.open()

    def invia_form(self):
        # modifico la proprietà text del button
        #self.submit_button.text = "Form inviato"

        riga = f"Sig./Sig.ra {self.nome.text} {self.cognome.text} nato/a il {self.data_di_nascita.text} a {self.luogo_di_nascita.text}"
        print("Riga:", riga)
        with open("out/form.txt",'w') as f:
            f.write(riga)

# il nome della classe deve iniziare con Main come il file .kv
# può anche chiamarsi, quindi, semplicemente Main
class MainApp(App):
    def build(self):
        return MainWindow()

# qualora invece si volesse chiamare il file .kv ad es. "style.kv",
# va eseguita questa istruzione
#kv = Builder.load_file("style.kv")

sample_app = MainApp()
sample_app.run()
