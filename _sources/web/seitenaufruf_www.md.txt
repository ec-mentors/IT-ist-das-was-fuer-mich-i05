# Was passiert bei einem Seitenaufruf?
1. Man gibt eine Internetadresse ein oder klickt auf einen Link
2. Der Webbrowser leitet die URL an den Router weiter
3. Der Router findet mit Hilfe eines DNS-Servers (DNS=Domain Name System) die IP-Adresse der Website heraus
4. Der Router fragt die benötigten Daten für den Seitenaufbau beim entsprechenden Webserver an. Diese Anfrage erfolgt via HTTP (HTTP=Hypertext Transfer Protocol)  in Form eines Datenpakets, das alle Informationen beinhaltet, die der Webserver benötigt, um die Webseitendaten auszuliefern. 
Das Datenpaket beeinhaltet:

   - die IP-Adresse der Website
   - die IP-Adresse des Routers
   - Auskunft über das Betriebssystem
   - Auskunft über den Browser 
   - Auskunft über die Art des Geräts, auf dem die Website angezeigt werden soll
7. Der Webserver wertet Informationen aus und übermittelt einen HTTP-Status-Code 
8. Ist die Anfrage erfolgreich versendet der Server ein Datenpaket mit allen für den Seitenaufbau notwendigen Informationen an den Webbrowser
9. Die eigehenden Datenpakete werden vom Router an den Rechner weitergeleitet
10. Der Webbrowser analysiert die Datenpakete und zeigt die Website an


