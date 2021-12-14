class Chatbot:

    reaktionsantworten = {"hallo": "Hallo. Wie kann ich Ihnen helfen?",
                        "mitarbeiter": "Ich suche für Sie einen freien Mitarbeiter",
                        "rechner": "Haben Sie ein Problem mit Ihrem Computer",
                        "problem": "Was genau ist ihr anliegen?"
					  }


    def get_response(message_text):
        response = ""
        for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            response += reaktionsantworten[einzelwoerter] * "\n" 
    return(reaktionsantworten[einzelwoerter])

