from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize

sAnagrafe = "./file.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciCreateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale not in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok"}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401

@api.route('/read_cittadino', methods=['GET'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            dati = anagrafe[sCodiceFiscale]
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok", "dati": dati}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
        
@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok", "Cittadino": dNuovoCittadino}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401
    
@api.route("/delete_cittadino", methods = ["DELETE"])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            pass

@api.route("/login", methods = ["POST"])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        try:
            data = request.json
            id = data.get("id")
            password = data.get("password")
            path = JsonDeserialize("./utenti.json")
            if id in path:
                user = path[id]
                if password == user["password"]:
                    admin = user["admin"]
                    jsonResp = {"Esito":"000", "Msg":"Buon lavoro", "Admin": admin, "id" : id, "Password" : password }
                    return json.dumps(jsonResp), 200
                else:
                    jsonResp = {"Esito": "001", "Msg": "Dati non validi"}
                    return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "User non trovato"}
                return json.dumps(jsonResp), 200
        except:
            return


api.run(host="127.0.0.1", port=8080, debug=True, ssl_context = "adhoc")