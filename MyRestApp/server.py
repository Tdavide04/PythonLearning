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
            operator = {"id" : id, "password" : password, "admin" : admin, "access" : access}
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

@api.route("/create_cittadino", methods = ["POST"])
def CreateCittadino():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        nome = dati.get("nome")
        cognome = dati.get("cognome")
        dataNascita = dati.get("data nascita")
        codiceFiscale = dati.get("codice fiscale")
        query = (f"INSERT INTO cittadini (nome, cognome, datanascita, codfiscale) VALUES ('{nome}', '{cognome}', '{dataNascita}', '{codiceFiscale}');")
        if db.write_in_db(connection, query) != -1:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : "Query eseguita"}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : "Dati incorretti"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

@api.route("/read_cittadino", methods = ["GET"])
def ReadCittadino():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json 
        codiceFiscale = dati.get("codice fiscale")
        query = (f"SELECT * FROM cittadini WHERE codfiscale = '{codiceFiscale}'")
        db_connection = db.read_next_row(connection, query)
        if db_connection[0] == 0 and db_connection[1] != None:
            print("Query eseguita con successo")
            dati_query = db_connection[1]
            return jsonify({"Esito" : "200", "Msg" : "Query eseguita", "Dati cittadino" : dati_query}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : "Dati incorretti"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

@api.route("/update_cittadino", methods = ["PUT"])
def UpdateCittadino():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
    sys.exit()
    try:
        dati = request.json
        nome = dati.get("nome")
        cognome = dati.get("cognome")
        dataNascita = dati.get("data nascita")
        codiceFiscale = dati.get("codice fiscale")
        query = (f"UPDATE cittadini SET nome = '{nome}', cognome = '{cognome}', datanascita = '{dataNascita}' WHERE codfiscale = '{codiceFiscale}'")
        if db.write_in_db(connection, query) == 0:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : "Query eseguita"}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : "Dati incorretti"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

@api.route("/delete_cittadino", methods = ["DELETE"])
def DeleteCittadino():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()

    try:
        dati = request.json

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

api.run(host="127.0.0.1", port=8080, ssl_context="adhoc", debug=True)