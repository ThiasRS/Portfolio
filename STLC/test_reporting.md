## Testdurchführungsdokumentation: Bewertungssystem

### Bewertung eines gekauften Produkts (Use Case Testing)
**Beschreibung:** Überprüfen, ob die Bewertungsfunktion für eingeloggte User bei bereits gekauften Produkten sichtbar und nutzbar ist.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Auf der Website einloggen | Login erfolgreich, Dashboard/Profil ist sichtbar | OK | https://grocerymate.masterschool.com/auth | |
| 2 | Zu "Shop" navigieren | Liste aller Produkte wird angezeigt | OK | https://grocerymate.masterschool.com/store | |
| 3 | Beliebiges Produkt in den Warenkorb legen |  | |  | |
| 4 | Zu "Warenkorb" navigieren | Liste der Produkte im Warenkorb wird angezeigt | OK | https://grocerymate.masterschool.com/checkout | |
| 5 | Adressdaten & Bezahldetails eingeben |  | |  | |
| 6 | Button "Pay Now" klicken | Bestellprozess abgeschlossen | NOK |  | |
| 7 | Zum bestellten Produkt navigieren | Produktseite wird angezeigt | OK |  | |
| 8 | Bewertungsbereich prüfen | Bewertungssystem (Sterne/Textfeld) ist sichtbar | OK |  | |
| 9 | Test-Bewertung schreiben und absenden | Erfolgsmeldung erscheint, Bewertung wird gespeichert | NOK | | |
