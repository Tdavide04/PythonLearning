'''
Dato il file json quiz.json scrivere un programma che risponde alle seguenti domande:

    quante domande ci sono nel questionario?
    quante sono, in media, il numero di risposte possibili?
    quante domande ci sono di matematica?
'''

import json
def parser(file):
    with open("Lezioni/Python5/parser of a dictionary/file.json") as file:
        data = json.load(file)

    totalQuestion: int = 0
    totalMathQuestion: int = 0

    for key, values in data["quiz"].items():
        for _, _ in values.items():
            totalQuestion += 1
            if key == "maths":
                totalMathQuestion += 1
                
    answerMedia = totalQuestion / max(1, totalMathQuestion)


    return totalQuestion, totalMathQuestion, answerMedia

print(parser("Lezioni/Python5/parser of a dictionary/file.json"))