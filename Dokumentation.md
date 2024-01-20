#Struktur

Das Projekt WhaToEat besteht aus einem Web Frontend, erstellt mit dem Javascript Framework Vue.js, und einem Python Backend welches Flask benutzt um eine REST API zur Kommunikation mit einer MongoDB Instanz zu erstellen.
Das Frontend ist hierbei der View und das Backend das Model, WhatToEat basiert also auf dem MVVM pattern. 

##Backend

Unter backend/api/main/{Klassenname} befinden sich jeweils zwei Dateien, einmal models.py und einmal routes.py. In models.py wird die Klasse definiert und alle nötigen Funktionen zur Verarbeitung der Anfragen des Frontends, sowie der Kommunikation mit der MongoDB Instanz angelegt. In der Routes.py werden die Routen des Endpunkts definiert und welche Funkion der Klasse aufgerufen wird. Die MongoDB_URI wird dynamisch aus den Angaben in der config.cfg erstellt.

##Frontend

In main.js werden die URL Pfade mit den dazugehörigen vue Dateien definiert. In WhatToEat.js wird die Klasse APIUtils definiert, sie definiert die get, post, put und delete Funktionen. Desweiteren werden Klassen zur Kommunikation mit den Endpunkten der Rest API definiert, diese werden alle von APIUtils abgeleitet um Zugriff auf die zuvor aufgelisteten Funktionen zu haben. Die vue Dateien enthalten sowohl den HTML als auch den Javascript Code und greift auf die in WhatToEat.js definierten Klassen zu um Daten mit dem Backend auszutauschen.

#Begründung
Wir haben uns dazu entschieden das Projekt in ein Web Frontend und Python Backend aufzuteilen, da sich Python zwar zur Datenverarbeitung und Kommunikation mit MongoDB sehr eignet, aber es schwieriger für uns ist eine ansprechende GUI in Python zu erstellen. Hierfür eignet sich eine Web GUI aber äußerst und da mit Flask die Mittel gegeben sind um diese beiden Teile zu Verknüpfen, haben wir uns für diesen Weg entschieden.