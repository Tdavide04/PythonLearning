from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize

sAnagrafe = "./anagrafe.json"
api = Flask(__name__)

#mettere una lista di liste dove ogni lista è un cittadino

#la chiave è il codice fiscale
#add cittadino
#read cittadino
#update cittadino
#delete cittadino


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
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


api.run(host="127.0.0.1", port=8080)