# Zustandsautomat zur Steuerung einer Ampel
# Taster1 schaltet Zustände: rot - rot/gelb - grün - gelb - rot
# Nach: Der Hobbyelektroniker, 12.06.2018
# Von C/C++ nach Python portiert, 09.08.2022 (Si)
# Für die Aktionen der Tasten: Zeile 121 auskommentieren

# Import der Methode für die Ansteuerung der Pins
from machine import Pin
# Import der Methoden zur Zeiterfassung 
from time import ticks_ms
from time import sleep_ms

## Globale Variable ##

# Definition der Pins der Ampel LEDs
led_rot = Pin(2, Pin.OUT)
led_gelb = Pin(4, Pin.OUT)
led_gruen = Pin(15, Pin.OUT)

# Grundzustand herstellen
led_rot.value(0)
led_gelb.value(0)
led_gruen.value(0)

# Definition der Pins der Tasten
taste1 = Pin(18, Pin.IN, Pin.PULL_UP)
taste2 = Pin(19, Pin.IN, Pin.PULL_UP)

# Eine Ampel wird durch Ereignisse gesteuert
taste1_gedrueckt = False
taste2_gedrueckt = False
takt_geben = False
start = ticks_ms()

# Eine Ampel hat einen Zustand:
zustand = "keine"

## Funktionen ##

# Keine Ampel LED leuchtet
def keine() -> None:
    global zustand,taste1_gedrueckt, taste2_gedrueckt
    
    led_rot.value(0)
    led_gelb.value(0)
    led_gruen.value(0)
    zustand = "keine"
    taste1_gedrueckt = False
    taste2_gedrueckt = False
    
# Die Ampel ist rot
def rot() -> None:
    global zustand, taste1_gedrueckt, takt_geben
    
    led_rot.value(1)
    led_gelb.value(0)
    led_gruen.value(0)
    zustand = "rot"
    taste1_gedrueckt = False
    takt_geben = False

# Die Ampel ist rot/gelb
def rot_gelb() -> None:
    global zustand, taste1_gedrueckt, takt_geben
    
    led_rot.value(1)
    led_gelb.value(1)
    led_gruen.value(0)
    zustand = "rot/gelb"
    taste1_gedrueckt = False
    takt_geben = False

# Die Ampel ist grün
def gruen() -> None:
    global zustand, taste1_gedrueckt, takt_geben
    
    led_rot.value(0)
    led_gelb.value(0)
    led_gruen.value(1)
    zustand = "grün"
    taste1_gedrueckt = False
    takt_geben = False

# Die Ampel ist gelb
def gelb() -> None:
    global zustand, taste1_gedrueckt, takt_geben
    
    led_rot.value(0)
    led_gelb.value(1)
    led_gruen.value(0)
    zustand = "gelb"
    taste1_gedrueckt = False
    takt_geben = False
    
# Takt geben
def takt() -> None:
    global zustand, start, takt_geben
    
    if zustand == "rot":
        zeit = 5000
    elif zustand == "grün":
        zeit = 2000
    else:
        zeit = 1000
        
    if (start + zeit) < ticks_ms():
        takt_geben = True
        start = ticks_ms()
        
# Ereignisse erfassen
def ereignisse() -> None:
    global taste1_gedrueckt, taste2_gedrueckt
    if taste1.value() == 0:
        taste1_gedrueckt = True
        sleep_ms(300)
        
    if taste2.value() == 0:
        taste2_gedrueckt = True
        sleep_ms(300)
        
#    takt()
    
# Ereignisse verarbeiten
def verarbeitung() -> None:
    global zustand, taste1_gedrueckt, taste2_gedrueckt
    
    if taste2_gedrueckt:
        keine()
        
    if taste1_gedrueckt or takt_geben:
        if zustand == "keine":
            rot()
        elif zustand == "rot":
            rot_gelb()
        elif zustand == "rot/gelb":
            gruen()
        elif zustand == "grün":
            gelb()
        elif zustand == "gelb":
            rot()
        else:
            print("Fehler im Programm")

# Loop
while True:
    ereignisse()
    verarbeitung()
    