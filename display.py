import shutil
import os
import time

pfad_webserver="/mnt/testsvr/"
#pfad_webserver="/opt/display/test/"
pfad_display="/opt/display/anzeige/"
pfad_template="/opt/display/template/"
pfad_javascript="/opt/display/"

#Alle Dateien im temporaeren Verzeichnis loeschen(einmalig)
for datei in os.listdir(pfad_display):
    if "liste1.html" not in datei:
        os.remove (pfad_display+datei)

#Html Dateien staendig nachladen und anpassen
while 1:
    shutil.copy (pfad_template+"liste1.html",pfad_display+"liste1.html")
    listennummer=0
    for html_datei in os.listdir(pfad_webserver):
        #print("datei gefunden" + html_datei)
        if ".html" in html_datei:
            listennummer+=1
            shutil.copy (pfad_webserver+html_datei,pfad_display+"liste"+str(listennummer)+".html")

            file = open(pfad_display+"liste"+str(listennummer)+".html", "r", encoding = 'ISO-8859-1',errors = 'replace' )
            replacement = ""
            for line in file:
                line = line.strip()
                changes = line.replace("<body>", "<body onload='pageScroll()'><script src='javascript_liste"+str(listennummer)+".js'></script>")
                replacement = replacement + changes + "\n"
            file.close()

            file = open(pfad_display+"liste"+str(listennummer)+".html", "w", encoding = 'ISO-8859-1')
            file.write(replacement)
            file.close()
        #else:
            #print("keine datei")
    #Javascript Dateien für die einzelnen Html Dateien erstellen und anpassen
    anzahl_listen=listennummer
    listennummer=0
    neue_seitennummer=1
    while listennummer<anzahl_listen:
        listennummer+=1
        shutil.copy (pfad_javascript+"javascript_liste.js",pfad_display+"javascript_liste"+str(listennummer)+".js")
        if neue_seitennummer == anzahl_listen:
            neue_seitennummer=1
        else:
            neue_seitennummer+=1
        
        file = open(pfad_display+"javascript_liste"+str(listennummer)+".js", "r")
        replacement = ""
        for line in file:
            line = line.strip()
            changes = line.replace("xxx", "file:///"+pfad_display+"liste"+str(neue_seitennummer)+".html")
            replacement = replacement + changes + "\n"
        file.close()

        file = open(pfad_display+"javascript_liste"+str(listennummer)+".js", "w")
        file.write(replacement)
        file.close()
    time.sleep(10)
