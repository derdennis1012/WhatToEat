#Struktur

Das Programm WhaToEat besteht aus einem Web Frontend, erstellt mit dem Javascript Framework Vue.js, und einem Python Backend welches Flask benutzt um eine REST API zur Kommunikation mit einer MongoDB Instaz zu erstellen.
Das Frontend ist hierbei der View und das Backend das Model, WhatToEat basiert also auf dem MVVM pattern. 

##Backend

Unter backend/api/main/{Klassenname} befinden sich jeweils zwei Dateien, einmal models.py und einmal routes.py. In models.py wird die Klasse definiert und alle nötigen Funktionen zur Verarbeitung der Anfragen des Frontends
