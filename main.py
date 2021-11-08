from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition

# il popup non è un sotto oggetto di MainWindow ma un altro oggetto
# per questo definiamo una classe e, parallelamente, nel file kv
# creiamo il suo layout
class CustomPopup(Popup):
    accettato_invio_form = ObjectProperty(None)

    def dismiss_popup(self):
        self.dismiss()
# Ora per creare più schermate in un'applicazione, anziché ereditare
# da un layout (in questo caso BoxLayout), facciamo ereditare da Screen
# e per gestire le transizioni da uno screen all'altro dobbiamo definire
# una classe che eredita da ScreenManager
#class MainWindow(BoxLayout):
class MainWindow(Screen):
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
        
        #lanciamo la seconda schermata
        sm.switch_to(screens[1], direction="left")
        #sm.current = "secondwindow" 

class SecondWindow(Screen):
    lbl_benvenuto = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.lbl_benvenuto.text = "Guarda come cambio il testo di benvenuto"
    
    def go_back(self):
        #sm.current = "mainwindow"
        # funziona!!!
        print("screens[0].nome.text:", screens[0].nome.text)
        sm.switch_to(screens[0], direction="right")

class WindowManager(ScreenManager):
    pass

# qualora invece si volesse chiamare il file .kv ad es. "style.kv",
# va eseguita questa istruzione
# NOTA: anche se non ha molto senso, dal momento che si gestiscono più
# schermate, va necessariamente utilizzata questa istruzione. 
# L'importante è che il file kv non si chiami allo stesso modo di prima, main.kv.
# altrimenti funziona a metà e il popup non viene più visualizzato!
# Quindi chiamarlo style.kv
kv = Builder.load_file("style.kv")

# instanziamo il nostro ScreenManager
# se non ci piace la transizione di default possiamo utilizzarne altre
# come ad esempio la WipeTransition
sm = WindowManager()
#sm = WindowManager(transition=WipeTransition())

# definiamo una lista di screen con in ordine MainWindow a cui associamo il nome
# mainwindow e SecondWindow con nome secondwindow per consentire allo screen 
# manager per dentificare le schermate
screens = [MainWindow(name='mainwindow'), SecondWindow(name='secondwindow')]

# aggiungiamo le singole schermate allo screen manager
for screen in screens:
    sm.add_widget(screen)

# decidiamo quale schermata deve partire per prima
sm.current = 'mainwindow'

# definire una classe che eredita da App in cui il metodo build
# restituisca la prima o l'unica schermata dell'applicazione
# il nome della classe deve iniziare con Main come il file .kv
# può anche chiamarsi, quindi, semplicemente Main
class MainApp(App):
    def build(self):
        #return MainWindow()
        return sm

sample_app = MainApp()
sample_app.run()
