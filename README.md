# Meine Ampel

Die Programme my_sm7_rev0.py bis rev2.py zeigen verschiedene Entwicklungsstufen bei der Ansteuerung einer Ampel. Die Programme sind in Python geschrieben und laufen auf einem ESP32 DevKit. 

## Externe Hardware
3 LEDs sind über Widerstände an digitale Ausgänge des ESP32 angeschlossen. Sie simulieren die Ampel. 

2 Tasten sind direkt an digitale Eingänge des ESP32 angeschlossen. 

## Funktionen der Ampel
Die 3 LEDs simulieren die Ampel. 

Timer steuern die Zustandsübergänge der Ampel. 
 
Wenn die Codezeilen mit den Timern auskommentiert sind, werden die Zustandsübergänge durch Tasten gesteuert. Taste1 schaltet durch die Zustände der Ampel. Taste2 schaltet in den Grundzustand. 

## Quellen
Die Idee stammt von hier: https://github.com/hobbyelektroniker/StateMachine
In diesem Repository wird eine Ampel mit dem Arduino programmiert. 

Die Programme my_sm7_rev0.py bis rev2.py sind Portierungen des ursprünglichen Programms sm7.ino von C/C++ nach Python.

Im finalen Program my_sm7_rev2.py werden folgende Bibliotheken eingesetzt: https://github.com/jrullan/micropython_statemachine und https://github.com/jrullan/micropython_neotimer

## Dank
Ich danke den Autoren "hobbyelektroniker" und "jrullan" für ihre hilfreichen Beiträge. 