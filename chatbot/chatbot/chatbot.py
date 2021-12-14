
class Chatbot:
    reaktionsantworten = { "DEFAULT" : "Leider weiß ich nicht, wie ich Ihnen damit helfen soll.", 
    "hallo": "Hallo. Wie kann ich Ihnen helfen?", 
    "mitarbeiter": "Alles klar, der nächste Mitarbeiter ist für Sie erreichbar unter der Telefonnummer: +49 40 123456789", 
    "problem": "Was genau ist ihr anliegen?",
    "ja" : "Alles klar, der nächste Mitarbeiter ist für Sie erreichbar unter der Telefonnummer: +49 40 123456789",
    "nein" : "Dann hoffe ich, dass ich Ihnen helfen konnte, und wünsche Ihnen einen schönen tag.",
    "danke" : "Ich freue mich, dass ich Ihnen helfen konnte. Einen schönen Tag noch."
    }

    # Problemspezifische Antworten
    
    rechner_problem = {"DEFAULT": "Was haben Sie für ein Problem mit ihrem Computer?",
    "geht_nicht": "Bitte stellen Sie sicher, dass das Kabel eingesteckt ist. Sofern Sie einen Mehrfachstecker verwenden, überprüfen Sie diesen ebenfalls.\nMöchten Sie mit einem Techniker telefonieren?"
    }
    maus_problem = {"DEFAULT": "Was ist das Problem mit der Maus?",
    "geht_nicht": "Ist die Maus angeschlossen?"
    }
    screen_problem = {"DEFAULT": "Was ist das Problem mit dem Bildschirm?",
    "geht_nicht": "Bitte stellen Sie sicher, dass alle Kabel korrekt angeschlossen sind.\nMöchten Sie mit einem Techniker telefonieren?" }
    sound_problem = {"DEFAULT": "Was für Geräusche hören Sie?",
    "kratzen" : "Sofern es Ihnen möglich ist, reinigen Sie bitte die Lüfter ihres Computers.\nMöchten Sie mit einem Techniker telefonieren?",
    "piepen" : "Es könnte ein Hardwaredefekt vorliegen, möchten Sie mit einem Techniker telefonieren?",
    "knirschen" : "Die Festplatte ist defekt. Möchten Sie mit einem Techniker Telefonieren?"}
    
    
    def __init__(self):
        pass


    def auswerten(self, text):
        words = text.split()
        problem = self.reaktionsantworten
        for word in words:
            if word.lower() in ["rechner", "computer", "pc"]:
                print("Computer problem")
                problem = self.rechner_problem
            elif word.lower() in ["monitor", "bildschirm"]:
                print("Screen problem")
                problem = self.screen_problem
            elif word.lower() == "maus":
                print("Maus problem")
                problem = self.maus_problem
            elif word.lower() in ["geräusche", "geräusch"]:
                print("Sound problem")
                problem = self.sound_problem

        return problem


    def get_response(self, message_text):
        problem_eingegrenzt = self.auswerten(message_text)
        #print(message_text)
        response = ""
        for word in message_text.split():
            print(word)
            #if (word.lower() in self.reaktionsantworten):
            #    response += self.reaktionsantworten[word.lower()] + "\n"
            if(word.lower() == "geht" or word == "nicht" or word.lower() == "an"):
                word = "geht_nicht"
            print(problem_eingegrenzt)

            print(word)
            if word.lower() in problem_eingegrenzt:
                response = problem_eingegrenzt[word.lower()]
                print("response:" + response)

        if response == "":
            response = problem_eingegrenzt["DEFAULT"]
        return(response)

