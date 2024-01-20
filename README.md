# WhatToEat
 
Setup Anleitung Backend

1. pip installieren
2. pipenv mit pip installieren (apt Version ist veraltet) 
3. Zu /WhatToEat/backend navigieren
4. pipenv shell ausführen
5. ./setup ausführen 
6. MONGODB Authentifizierungsdaten in WhatToEat/backend/api/main/config/config.cfg eintragen
    6.1 Falls es Probleme mit dem MONGODB connection string gibt, kann man MONGODB_URI in WhatToEat/backend/api/main/__init__.py direkt setzen
7. Falls man die Shell verlassen oder den Ordner gewechselt hat: Schritte 3 und 4 wiederholen
8. Das Backend mit ./run starten

Setup Anleitung Frontend

1. npm und nodejs installieren
2. Zu WhatToEat/frontend navigieren
3. npm install ausführen
4. npm run dev ausführen um das Frontend zu starten
