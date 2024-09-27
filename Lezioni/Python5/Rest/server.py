from flask import Flask, json, request

api = Flask(__name__)

@api.route("/add_cittadino", methods=["POST"])
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

if __name__ == "__main__":

    api.run(host="127.0.0.1", port=8080)