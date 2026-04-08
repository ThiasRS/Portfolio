# Testfallentwurf

**Entwirf deine Testfälle auf Grundlage der Funktionen, die für das nächste Release der sozialen Medienplattform entwickelt werden sollen!**

**Du musst sie nur *entwerfen* – die Testdurchführung erfolgt in einer späteren Phase.**

**Füge, falls zutreffend, das verwendete Testentwurfsverfahren hinzu.**

## 1. Bewertungssystem für Produkte
**Testentwurfsverfahren:** Anwendungsfalltest (Use Case Testing), Grenzwertanalyse (BVA), Fehlermessen (Error Guessing)

**Testfälle:**
1. **Anwendungsfalltest:**
  - **Testfall:** Überprüfen ob die Bewertungsfunktion sichtbar ist bei gekauften Produkten und eingeloggtem User.
    - **Eingabe:** Einloggen, Produkt kaufen, Navigation zum gekauftem Produkt.
    - **Erwartetes Ergebnis:** Bewertungssystem ist sichtbar.
2. **Grenzwertanalyse:**
  - **Testfall:** *Überprüfen ob die Bewertung mehr als 500 Zeichen zulässt.
    - **Eingabe:** Eine Bewertung mit 501 Zeichen schreiben.
    - **Erwartetes Ergebnis:** Bewertung nicht möglich.
3. **Fehlermessen:**
  - **Testfall:** *Überprüfen ob die Bewertung code zulässt (HTML oder Script).
    - **Eingabe:** Eine Bewertung mit code schreiben.
    - **Erwartetes Ergebnis:** Code wird als Text angezeigt.


## 2. Altersverifikation für alkoholische Produkte
**Testentwurfsverfahren:** Anwendungsfalltest (Use Case Testing), Grenzwertanalyse (BVA), Fehlermessen (Error Guessing)

**Testfälle:**
1. **Anwendungsfalltest:**
  - **Testfall:** Überprüfen ob die Altersverifikation nach Login unter der Kategorie "Alkoholische Produkte" auftaucht.
    - **Eingabe:** Einloggen, Navigation zur Produktkategorie "Alkoholische Produkte".
    - **Erwartetes Ergebnis:** Alterverifikation ist sichtbar.
2. **Grenzwertanalyse:**
  - **Testfall:** *Überprüfen ob die Produktkategorie auch sichtbar ist bei einem Alter von 17 Jahren.
    - **Eingabe:** Bei der Altersverifikation ein Datum angeben bei dem man 1 Tag davor entfernt ist 18 Jahre alt zu werden.
    - **Erwartetes Ergebnis:** Produktkategorie "Alkoholische Getränke" kein Zugriff.
3. **Fehlermessen:**
  - **Testfall:** *Das Datum bei der Alterverifikation im Format YYYY/MM/DD angeben.
    - **Eingabe:** Navigation zur Altersverifikation und 1993/08/24 eingeben.
    - **Erwartetes Ergebnis:** Datumsformat ungültig.


## 3. Änderung bei den Versandkosten
**Testentwurfsverfahren:** Anwendungsfalltest (Use Case Testing), Grenzwertanalyse (BVA), Fehlermessen (Error Guessing)

**Testfälle:**
1. **Anwendungsfalltest:**
  - **Testfall:** Prüfung der korrekten Anzeige des verbleibenden Differenzbetrags bis zum Gratis-Versand.
    - **Eingabe:** Ein Produkt im Wert von 12,00 € in den Warenkorb legen.
    - **Erwartetes Ergebnis:** Im Warenkorb erscheint ein Hinweis: „Noch 8,00 € bis zum kostenlosen Versand“, und die aktuellen Versandkosten werden voll berechnet.
2. **Grenzwertanalyse:**
  - **Testfall:** *Validierung der „Ab-20€-Regel“ durch zwei aufeinanderfolgende Grenzkontrollen.
    - **Eingabe:** Warenkorb auf genau 19,99 € füllen (Versandkosten prüfen), dann ein Produkt für 0,01 € hinzufügen (Gesamt 20,00 €).
    - **Erwartetes Ergebnis:** Bei 19,99 € werden Versandkosten addiert; bei exakt 20,00 € springt die Anzeige sofort auf 0,00 € (Gratis-Versand).
3. **Fehlermessen:**
  - **Testfall:** *Simulation eines Fehlers durch Entfernen von Artikeln nach Erreichen der Gratis-Schwelle.
    - **Eingabe:** Warenkorb auf 25,00 € füllen (Versand ist gratis), dann Artikel entfernen, bis der Wert auf 15,00 € sinkt.
    - **Erwartetes Ergebnis:** Die Versandkosten müssen automatisch wieder reaktiviert und auf den Gesamtpreis aufgeschlagen werden (kein „Einfrieren“ des Gratis-Status).
