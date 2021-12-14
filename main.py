# -*- coding: utf-8 -*-
import random
import time


reaktionsantworten = {"hallo": "Hallo. Wie kann ich Ihnen helfen?",
                        "mitarbeiter": "Ich suche für Sie einen freien Mitarbeiter",
                        "rechner": "Was genau ist Ihr Problem mit Ihrem Rechner?",
                        "problem": "Was genau ist ihr anliegen?"
					  }
                      
print("Willkommen bei der Solutions IT!\nIch bin Ada, ihr Support Bot")
# time.sleep(2)
print("Um Ihnen zu helfen, sagen Sie mir bitte worum es geht.")
# time.sleep(2)
print("Zum Beenden des Gespräches geben Sie bitte einfach 'bye' ein") 
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage: ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])

    if nutzereingabe == "rechner geht nicht an":
        nutzereingabe == ""
        print()
        print("Ich habe ein paar Tipps für Sie.")
        print("Ist das Stromkabel eingesteckt?")
        nutzereingabe = input()
        if nutzereingabe == "ja":
            print("Ist der Bildschirm an?")
            nutzereingabe == ""
            nutzereingabe = input()
            if nutzereingabe == "nein":
                print("Dann schalten Sie den Bildschrim bitte an.")
                print("Funktioniert es jetzt?")
                nutzereingabe = ""
                nutzereingabe = input()
                if nutzereingabe == "ja":
                    print("Das Problem ist behoben!")
                    break
                else:
                    print("Benutzen Sie eine Mehrfachsteckdose und ist diese Richtig angesteckt?")
                    nutzereingabe = ""
                    nutzereingabe = input()
                    if nutzereingabe == "ja":
                        print("Ich verbinde Sie mit einem Mitarbeiter.")
                        break
                    else:
                        print("Ich verbinde Sie mit einem Mitarbeiter.")
                        break
            else:
                print("Ich verbinde Sie mit einem Mitarbeiter.")
        else:
            print("Stecken Sie es rein.")
            print("Funktioniert es jetzt?")
            nutzereingabe == ""
            nutzereingabe = input()
            if nutzereingabe == "ja":
                print("Das Problem ist behoben!")
                break
            else:
                print("Ich verbinde Sie mit einem Mitarbeiter.")
                break

    if nutzereingabe == "maus geht nicht":
        nutzereingabe == ""
        print()
        print("Ich habe ein paar Tipps für Sie.")
        print("Ist die Maus angeschlossen?")
        nutzereingabe = input()
        if nutzereingabe == "ja":
            print("Ist die Maus am richtigen Pc angeschlossen?")
            nutzereingabe == ""
            nutzereingabe = input()
            if nutzereingabe == "nein":
                print("Dann schließen Sie bitte die Maus an den richtigen Rechner.")
                print("Funktioniert es jetzt?")
                nutzereingabe = ""
                nutzereingabe = input()
                if nutzereingabe == "ja":
                    print("Das Problem ist behoben!")
                    break
                else:
                    print("Haben Sie eine Kabellosemaus?")
                    nutzereingabe = ""
                    nutzereingabe = input()
                    if nutzereingabe == "ja":
                        print("Schauen Sie nach ob der Akku oder die Batterien voll sind.")
                        print("Sind diese voll?")
                        nutzereingabe = ""
                        nutzereingabe = input()
                        if nutzereingabe == "ja":
                            print("Ich verbinde Sie mir einem Mitarbeiter.")
                            break
                        else:
                            print("Bitte laden Sie den Akku oder die Batterien!")
                            break
                    else:
                        print("Ich verbinde Sie mit einem Mitarbeiter.")
                        break
            else:
                print("Ich verbinde Sie mit einem Mitarbeiter.")
        else:
            print("Schließen Sie die Maus rein.")
            print("Funktioniert es jetzt?")
            nutzereingabe == ""
            nutzereingabe = input()
            if nutzereingabe == "ja":
                print("Das Problem ist behoben!")
                break
            else:
                print("Ich verbinde Sie mit einem Mitarbeiter.")
                break

    if nutzereingabe == "rechner macht geräusche":
        nutzereingabe == ""
        print()
        print("Ich habe ein paar Tipps für Sie.")
        print("Ist der Rechner neu?")
        nutzereingabe = input()
        if nutzereingabe == "nein":
            print("Sind die Lüfter sauber oder verdreckt?")
            nutzereingabe == ""
            nutzereingabe = input()
            if nutzereingabe == "verdreckt":
                print("Machen Sie die Lüfter sauber.")
                print("Funktioniert es jetzt?")
                nutzereingabe = ""
                nutzereingabe = input()
                if nutzereingabe == "ja":
                    print("Das Problem ist behoben!")
                    break
                else:
                    print("Haben oder hatten Sie Haustiere die Sie zur Zeit vermissen?")
                    nutzereingabe = ""
                    nutzereingabe = input()
                    if nutzereingabe == "ja":
                        print("Schauen Sie in ihrem Rechner nach ihnen.")
                        break
                    else:
                        print("Ich verbinde Sie mit einem Mitarbeiter.")
                        break
            else:
                print("Ich verbinde Sie mit einem Mitarbeiter.")
        else:
            print("Haben Sie noch Garantie?")
            nutzereingabe == ""
            nutzereingabe = input()
            if nutzereingabe == "ja":
                print("Wenden Sie sich an den Verkäufer.")
                break
            else:
                print("Ich verbinde Sie mit einem Mitarbeiter.")
                break
        
        
    print("")

print("Einen schönen Tag wünsche ich Ihnen. Bis zum nächsten Mal")


# def main():
#     print("Hello World")

# if __name__ == "__main__":
#     main()