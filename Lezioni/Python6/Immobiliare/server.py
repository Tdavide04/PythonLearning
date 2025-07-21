from datetime import datetime
from flask import Flask, request, jsonify
import dbclient as db
import sys


api = Flask(__name__)

@api.route("/login", methods=["POST"])
def login():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    try:
        jsonReq = request.json
        id = jsonReq.get("operator_id")
        password = jsonReq.get("operator_password") 
        login_query = (f"SELECT id, password, admin, tipo FROM operatore WHERE id = '{id}' AND password = '{password}'")
        result = db.read_next_row(connection, login_query)
        if result[1]:
            admin = True
            access = True
            tipo = result[1][3]
            operator = {"id" : id, "password" : password, "admin" : admin, "access" : access, "tipo":tipo}
            print(f"Benvenuto operatore {id}")
            return jsonify({"Esito" : "200", "Msg" : "Dati corretti", "operator" : operator}), 200
        elif result == 0:
            print("Accesso negato, operatore non trovato")
            return jsonify({"Esito" : "404", "Msg" : "Dati non corretti"}), 404

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    
    finally:
        db.close(connection)

@api.route("/case_in_vendita", methods = ["GET"])
def CercaCasaVendita():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        catastale = dati.get("catastale")
        indirizzo = dati.get("indirizzo")
        piano = dati.get("piano")
        metri = dati.get("metri")
        vani = dati.get("vani")
        prezzo_min = dati.get("prezzo_min")
        prezzo_max = dati.get("prezzo_max")
        stato = dati.get("stato")

        conditions = []
        if catastale:
            conditions.append(f"catastale = '{catastale}'")
        if indirizzo:
            conditions.append(f"indirizzo = '{indirizzo}'")
        if piano:
            conditions.append(f"piano = {piano}")
        if metri:
            conditions.append(f"metri = {metri}")
        if vani:
            conditions.append(f"vani = {vani}")
        if prezzo_min is not None and prezzo_max is not None:
            conditions.append(f"prezzo BETWEEN {prezzo_min} AND {prezzo_max}")
        elif prezzo_min is not None:
            conditions.append(f"prezzo >= {prezzo_min}")
        elif prezzo_max is not None:
            conditions.append(f"prezzo <= {prezzo_max}")
        if stato:
            conditions.append(f"stato = '{stato}'")
        where_clause = " AND ".join(conditions)
        query = f"SELECT * FROM case_in_vendita"
        if where_clause: 
            query += f" WHERE {where_clause}"
        
        rows = db.read_all_row(connection, query)
        if rows and len(rows) > 0:
            print("Case trovate con successo!")
            return jsonify({"Esito":"ok","Msg":"Case trovate con successo!","case":rows}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : f"Query fallita"}), 404

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/case_in_affitto", methods = ["GET"])
def CercaCasaAffitto():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        catastale = dati.get("catastale")
        indirizzo = dati.get("indirizzo")
        tipo_affitto = dati.get("tipo_affitto")
        bagno_personale = dati.get("bagno_personale")
        prezzo_min = dati.get("prezzo_min")
        prezzo_max = dati.get("prezzo_max")

        conditions = []
        if catastale:
            conditions.append(f"catastale = '{catastale}'")
        if indirizzo:
            conditions.append(f"indirizzo = '{indirizzo}'")
        if tipo_affitto:
            conditions.append(f"piano = '{tipo_affitto}'")
        if bagno_personale:
            conditions.append(f"metri = '{bagno_personale}'")
        if prezzo_min is not None and prezzo_max is not None:
            conditions.append(f"prezzo BETWEEN {prezzo_min} AND {prezzo_max}")
        elif prezzo_min is not None:
            conditions.append(f"prezzo >= {prezzo_min}")
        elif prezzo_max is not None:
            conditions.append(f"prezzo <= {prezzo_max}")
        where_clause = " AND ".join(conditions)
        query = f"SELECT * FROM case_in_affitto"
        if where_clause: 
            query += f" WHERE {where_clause}"
        
        rows = db.read_all_row(connection, query)
        if rows and len(rows) > 0:
            print("Case trovate con successo!")
            return jsonify({"Esito":"ok","Msg":"Case trovate con successo!","case":rows}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : f"Query fallita"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/vendi_casa", methods = ["POST"])
def VendiCasa():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        catastale = dati.get("catastale")
        filiale = dati.get("filiale")
        query = f"SELECT * FROM case_in_vendita WHERE catastale = '{catastale}'"
        if db.read_in_db(connection, query) == 1:
            row = db.read_next_row(connection,query)[1]
        else:
            return jsonify({"Esito": "404", "Msg": "Qualcosa è andato storto"}), 404
        if row:
            query = f"INSERT INTO vendute_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita) VALUES ('{row[0]}', '{datetime.now()}', '{row[8]}', '{filiale}','{row[6]}')"
            if db.write_in_db(connection, query) == 0:
                query = f"DELETE FROM case_in_vendita WHERE catastale = '{catastale}'"
                db.write_in_db(connection, query)
                if db.read_in_db(connection, query) == 0:
                    print("Casa venduta con successo!")
                    return jsonify({"Esito":"200", "Msg":"Casa venduta con successo"}), 200
            else:
                return jsonify({"Esito": "404", "Msg": "Qualcosa è andato storto"}), 404
                
        else:
            return jsonify({"Esito": "404", "Msg": "Catastale non trovato"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/check_filiale", methods=["GET"])
def CheckFiliale():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        filiale = dati.get("filiale")
        query = f"SELECT * FROM filiali WHERE nome = '{filiale}'"
        if db.read_in_db(connection, query) == 1:
            return jsonify({"Esito":"200", "Msg":"Filiale trovata"}), 200
        
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/affitta_casa", methods = ["POST"])
def VendiCasa():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        catastale = dati.get("catastale")
        filiale = dati.get("filiale")
        durata = dati.get("durata")
        query = f"SELECT * FROM case_in_affitto WHERE catastale = '{catastale}'"
        if db.read_in_db(connection, query) == 1:
            row = db.read_next_row(connection,query)[1]
        else:
            return jsonify({"Esito": "404", "Msg": "Qualcosa è andato storto"}), 404
        if row:
            query = f"INSERT INTO vendute_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita) VALUES ('{row[0]}', '{datetime.now()}', '{row[8]}', '{filiale}','{row[6]}', '{durata}')"
            if db.write_in_db(connection, query) == 0:
                query = f"DELETE FROM case_in_vendita WHERE catastale = '{catastale}'"
                db.write_in_db(connection, query)
                if db.read_in_db(connection, query) == 0:
                    print("Casa venduta con successo!")
                    return jsonify({"Esito":"200", "Msg":"Casa venduta con successo"}), 200
            else:
                return jsonify({"Esito": "404", "Msg": "Qualcosa è andato storto"}), 404
                
        else:
            return jsonify({"Esito": "404", "Msg": "Catastale non trovato"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("vendi_casa", methods=["DELETE"])
def DeleteCasa():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        catastale = dati.get("catastale")
        query = f"DELETE FROM case_in_vendita WHERE catastale = '{catastale}'"
        if db.write_in_db(connection, query) == 0:
            return jsonify({"Esito":"200", "Msg":"Casa eliminata con successo"}), 200
                
        else:
            return jsonify({"Esito": "404", "Msg": "Catastale non trovato"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)


api.run(host="127.0.0.1", port=8080, ssl_context="adhoc", debug=True)