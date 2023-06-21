# Zustandsautomat zur Steuerung einer Ampel
# Taster1 schaltet Zustände: rot - rot/gelb - grün - gelb - rot
# Nach: Der Hobbyelektroniker, 12.06.2018
# Von C/C++ nach Python portiert, 09.08.2022 (Si)
# Ohne die globalen Variablen e_taste1, e_taste2, takt_geben
# Für die Aktionen der Tasten: Zeile 83 durch return False ersetzen

# Import der Methode für die Ansteuerung der Pins
from machine import Pin

# Import der Methoden für den Taktgeber 
from time import ticks_ms
from time import sleep_ms

# Definition der Pins der Ampel LEDs
led_rot = Pin(2, Pin.OUT)
led_gelb = Pin(4, Pin.OUT)
led_gruen = Pin(15, Pin.OUT)

# Definition der Pins der Tasten
taste1 = Pin(18, Pin.IN, Pin.PULL_UP)
taste2 = Pin(19, Pin.IN, Pin.PULL_UP)

# Eine Ampel hat einen Zustand
# - keine LED leuchtet
# - rot
# - rot/gelb
# - grün
# - gelb
zustand = "keine"

# Startzeit für den Takt 
start = ticks_ms()

## Funktionen ##

# Keine Ampel LED leuchtet
def keine() -> None:
    led_rot.value(0)
    led_gelb.value(0)
    led_gruen.value(0)
    
# Die Ampel ist rot
def rot() -> None:
    led_rot.value(1)
    led_gelb.value(0)
    led_gruen.value(0)

# Die Ampel ist rot/gelb
def rot_gelb() -> None:
    led_rot.value(1)
    led_gelb.value(1)
    led_gruen.value(0)

# Die Ampel ist grün
def gruen() -> None:
    led_rot.value(0)
    led_gelb.value(0)
    led_gruen.value(1)

# Die Ampel ist gelb
def gelb() -> None:
    led_rot.value(0)
    led_gelb.value(1)
    led_gruen.value(0)
    
# Takt geben
def takt() -> bool:
    global zustand, start
    takt_geben = False
    
    if zustand == "rot":
        zeit = 5000
    elif zustand == "grün":
        zeit = 2000
    else:
        zeit = 1000
        
    if (start + zeit) < ticks_ms():
        takt_geben = True
        start = ticks_ms()
        
#    return takt_geben
    return False
        
# Taste1 gedrückt?
def taste1_gedrueckt() -> bool:
    if taste1.value() == 0:
        e_taste1 = True
        sleep_ms(300)
    else:
        e_taste1 = False
    return e_taste1

# Taste2 gedrückt?
def taste2_gedrueckt() -> bool:
    if taste2.value() == 0:
        e_taste2 = True
        sleep_ms(300)
    else:
        e_taste2 = False
    return e_taste2
    
# Ereignisse verarbeiten
def verarbeitung(zustand: str) -> str:
    if taste2_gedrueckt():
        keine()
        zustand = "keine"
    
    if taste1_gedrueckt() or takt():
        print(zustand)
        if zustand == "keine":
            rot()
            zustand = "rot"
        elif zustand == "rot":
            rot_gelb()
            zustand = "rot/gelb"
        elif zustand == "rot/gelb":
            gruen()
            zustand = "grün"
        elif zustand == "grün":
            gelb()
            zustand = "gelb"
        elif zustand == "gelb":
            rot()
            zustand = "rot"
        else:
            print("Fehler im Programm")
            
    return zustand

# Setup
keine()

# Loop
while True:
    zustand = verarbeitung(zustand)
    takt()