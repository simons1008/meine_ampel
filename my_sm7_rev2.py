# Zustandsautomat zur Steuerung einer Ampel
# Taster1 schaltet Zustände: GELB_BLINKEN - ROT - ROT/GELB - GRUEN - GELB - ROT
# Nach: Der Hobbyelektroniker, 12.06.2018
# Von C/C++ nach Python portiert, 11.08.2022 (Si)
# Zustand KEINE durch GELB_BLINKEN ersetzt, 04.12.2022 (Si)
# Einsatz der Bibliothek statemachine
# Für die Aktionen der Tasten: Zeilen 104 bis 108 auskommentieren

# Import der Methoden für den Zustandsautomaten
from neotimer import *
from statemachine import *

# Import der Methode für die Ansteuerung der Pins
from machine import Pin

# Definition der Pins der Ampel LEDs
led_rot = Pin(2, Pin.OUT)
led_gelb = Pin(4, Pin.OUT)
led_gruen = Pin(15, Pin.OUT)

# Gelbe LED initialisieren
led_gelb.value(0)

# Definition der Pins der Tasten
taste1 = Pin(18, Pin.IN, Pin.PULL_UP)
taste2 = Pin(19, Pin.IN, Pin.PULL_UP)

# Objekt state_machine erzeugen
state_machine = StateMachine()

# Timer 250 ms für Debouncing
myTimer_250 = Neotimer(250)

# Timer 500 ms, 1000 ms, 2000 ms, 5000 ms für periodische Ausführung
myTimer_500 = Neotimer(500)
myTimer_1000 = Neotimer(1000)
myTimer_2000 = Neotimer(2000)
myTimer_5000 = Neotimer(5000)

#### Funktionen in den Zuständen ####
# Bis zum Zustandswechsel wird die Funktion wiederholt aufgerufen
# Einmaliger Aufruf durch Abfrage von state_machine.execute_once
# Die Ampel blinkt gelb
def gelb_blinken():
    led_rot.value(0)
    led_gruen.value(0)
    if myTimer_500.repeat_execution():
        led_gelb.value(not led_gelb.value())
    
# Die Ampel ist rot
def rot():
    led_rot.value(1)
    led_gelb.value(0)
    led_gruen.value(0)

# Die Ampel ist rot/gelb
def rot_gelb():
    led_rot.value(1)
    led_gelb.value(1)
    led_gruen.value(0)

# Die Ampel ist grün
def gruen():
    led_rot.value(0)
    led_gelb.value(0)
    led_gruen.value(1)
    
# Die Ampel ist gelb
def gelb():
    led_rot.value(0)
    led_gelb.value(1)
    led_gruen.value(0)

# Taste1 gedrückt?
def taste1_gedrueckt():
    if myTimer_250.debounce_signal(taste1.value() == 0):
        return True
    else:
        return False

# Taste2 gedrückt?
def taste2_gedrueckt():
    if myTimer_250.debounce_signal(taste2.value() == 0):
        return True
    else:
        return False

# Definition der Zustände
GELB_BLINKEN    = state_machine.add_state(gelb_blinken)
ROT             = state_machine.add_state(rot)
ROT_GELB        = state_machine.add_state(rot_gelb)
GRUEN           = state_machine.add_state(gruen)
GELB            = state_machine.add_state(gelb)

# Zustandsübergänge hinzufügen
# Übergänge durch Tasten
GELB_BLINKEN.attach_transition(taste1_gedrueckt, ROT)
ROT.attach_transition(taste1_gedrueckt, ROT_GELB)
ROT_GELB.attach_transition(taste1_gedrueckt, GRUEN)
GRUEN.attach_transition(taste1_gedrueckt, GELB)
GELB.attach_transition(taste1_gedrueckt, ROT)

# # Übergänge durch Timer
# GELB_BLINKEN.attach_transition(myTimer_1000.repeat_execution, ROT)
# ROT.attach_transition(myTimer_5000.repeat_execution, ROT_GELB)
# ROT_GELB.attach_transition(myTimer_1000.repeat_execution, GRUEN)
# GRUEN.attach_transition(myTimer_2000.repeat_execution, GELB) 
# GELB.attach_transition(myTimer_1000.repeat_execution, ROT)

# Übergänge nach GELB_BLINKEN
ROT.attach_transition(taste2_gedrueckt, GELB_BLINKEN)
ROT_GELB.attach_transition(taste2_gedrueckt, GELB_BLINKEN)
GRUEN.attach_transition(taste2_gedrueckt, GELB_BLINKEN)
GELB.attach_transition(taste2_gedrueckt, GELB_BLINKEN)

# Loop
while True:
    state_machine.run()                        