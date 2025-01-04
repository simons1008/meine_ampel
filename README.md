# Meine Ampel

Die Programme my_sm7_rev0.py bis rev2.py zeigen die Ansteuerung einer Ampel mit einer Statemachine. Die Programme sind in Python geschrieben und laufen auf einem ESP32 DevKit mit MicroPython. 

## Externe Hardware
3 LEDs sind über Widerstände an digitale Ausgänge des ESP32 angeschlossen.  

2 Tasten sind direkt an digitale Eingänge des ESP32 angeschlossen. 

## Funktionen der Ampel
Die 3 LEDs simulieren die Ampel. 

Die Tasten steuern die Zustandsübergänge der Ampel. Taste1 schaltet durch die Zustände der Ampel. Taste2 schaltet in den Grundzustand. 

Wenn die Codezeilen mit den Timern aktiviert sind, werden die Zustandsübergänge der Ampel durch Timer gesteuert. 

## Quellen
Die Grundlage stammt von hier: https://github.com/hobbyelektroniker/StateMachine
In diesem Repository wird die Ansteuerung einer Ampel mit einer Statemachine gezeigt. Die Programme sind in C/C++ geschrieben und laufen auf dem Arduino. 

Die Programme my_sm7_rev0.py bis rev2.py sind Portierungen des ursprünglichen Programms sm7.ino von C/C++ nach Python.

Die letzte Version des Programms my_sm7_rev2.py realisiert die Statemachine mit Funktionen aus folgenden Bibliotheken: https://github.com/jrullan/micropython_statemachine und https://github.com/jrullan/micropython_neotimer

## Dank
Ich danke den Autoren "hobbyelektroniker" und "jrullan" für ihre hilfreichen Beiträge. 