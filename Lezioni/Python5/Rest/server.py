from flask import Flask, json, request

api = Flask(__name__)
file_path = "Lezioni/Python5/Rest/file.json"


@api.route("/cittadino", methods=["POST"])
def gestisciAddCittadino():
    content_type = request.headers.get("Content-Type")
    print("Ricevuta chimata" + content_type)
    if content_type == "application/json":
        jsonReq = request.json
        print(jsonReq)
        # cittadini.append(jsonReq)
        jsonResp = {"Esito":"200", "Msg":"ok"}
        return json.dumps(jsonResp)
    else:
        return "Content-Type not supported!"
    
@api.route("/add_cittadino", methods=["POST"])
def addDatiCittadino(nome, cognome, dataN, codF):
    new_cittadino = {codF:{
        "nome": nome,
        "cognome": cognome,
        "dataNascita": dataN,
        "codFiscale": codF,
    }}
    try: 
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Error, no data found"
    
    if codF not in data:
        data.update(new_cittadino)
        with open(file_path, "w") as file:
            json.dump(data, file)
    else:
        return "Error, cittadino already registered"

@api.route("/read_cittadino", methods=["POST"])
def readDatiCittadino(codF) -> dict:
    try: 
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Error, no data found"
    if codF in data:
        return data[codF]
    
def updateDatiCittadino(codF, oldValue, newValue):
    try: 
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Error, no data found"
    
    if codF in data:
        if oldValue in data:
            data[codF][oldValue] = newValue
            with open(file_path, "w") as file:
                json.dump(data, file)
            return "Data updated"
        else:
            return "Data not found"
    else:
        return "Error, cittadino is not registered"
    
def deleteDatiCittadino(codF):
    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Error, no data found"
    if codF in data:
        del data[codF]
        with open(file_path, "w") as file:
            json.dump(data)
    else:
        return "Error, cittadino is not registered"


if __name__ == "__main__":

    api.run(host="127.0.0.1", port=8080)