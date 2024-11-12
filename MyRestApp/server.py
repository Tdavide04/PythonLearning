from flask import Flask, jsonify, request
from configparser import ConfigParser
import dbclient as db
import psycopg2
import os, sys

api = Flask(__name__)

@api.route("/login", methods=["POST"])
def login():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
        
    try:
        jsonReq = request.json
        id = jsonReq.get("operator_id")
        password = jsonReq.get("operator_password")
        login_query = (f"select id,password from operator where id = '{id}' and password = '{password}'")
        if db.read_in_db(connection, login_query) != -1:
            admin = False
            login_query = (f"select id,password from operator where id = '{id}' and password = '{password}' and admin = 'true'")
            if db.read_in_db(connection, login_query) != -1:
                admin = True
            access = True
            operator = {"id" : id, "password" : password}
            print(f"Benvenuto operatore {id}")
            return jsonify({"Esito" : "200", "Msg" : "Dati corretti", "operator" : operator}), 200
        else:
            print("Accesso negato, operatore non trovato")
            return jsonify({"Esito" : "404", "Msg" : "Dati non corretti"}), 404

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

@api.route("/")
def AddCittadino():
    pass


api.run(host="127.0.0.1", port=8080, ssl_context="adhoc")