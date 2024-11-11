from flask import Flask, jsonify, request
from configparser import ConfigParser
from dbclient import db
import psycopg2
import os, sys

api = Flask(__name__)

@api.route("/login", method = ["POST"])
def login():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        content_type = request.headers.get("Content-Type")
        jsonReq = request.json
        id = jsonReq.get("operator_id")
        password = jsonReq.get("operator_password")
        login_query = (f"selcet id.password from operator where id = {id} and password = {password}")
        if db.read_next_row(connection)[1]:
            access = True
            operator = {"id" : id, "password" : password}
            print(f"Benvenuto operatore {id}")
            return jsonify({"Esito" : "200", "Msg" : "Dati corretti", "operator" : operator}), 200
        else:
            print("Accesso negato, operatore non trovato")
            return jsonify({"Esito" : "404", "Msg" : "Dati non corretti"}), 404

    except Exception as e:
        print(f"Rorre dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

api.run(host="127.0.0.1", port=8080, ssl_context="adhoc")