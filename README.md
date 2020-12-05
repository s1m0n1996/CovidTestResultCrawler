# Allgemein

Checke das Corona Testergebnis in den konfigurierten Abständen.

# Konfiguration
Alle Einstellungen wie z. B. der Abstand, in dem das Ergebnis überprüft wird, sind in der Datei 
```./src/config.ini``` zu ändern.

# Ausführung
es bietet sich sich due ausführung auf einem gerät an welches 24/7 Läuft (z.B. RaspberryPi).

Man kann die main.py manuell mit python ausführen, oder den systemd-service ausführen, welcher in crawler.service 
konfiguriert ist.

Die viel elegantere variante ist der service über systemd/systemctl.