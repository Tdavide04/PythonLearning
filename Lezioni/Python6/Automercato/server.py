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
        login_query = (f"SELECT id, password, admin FROM operator WHERE id = '{id}' AND password = '{password}'")
        result = db.read_in_db(connection, login_query)
        if result == 1:
            admin = True
            access = True
            operator = {"id" : id, "password" : password, "admin" : admin, "access" : access}
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

@api.route("/create_product", methods = ["POST"])
def CreateProduct():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        tipo = dati.get("tipo")
        marca = dati.get("marca")
        modello = dati.get("modello")
        prezzo = dati.get("prezzo")
        disponibilita = dati.get("disponibilita")
        filiale_id = dati.get("filiale_id") 
        if tipo == "automobile":
            query = (f"INSERT INTO automobili (marca, modello, prezzo, disponibilita, filiale_id) VALUES ('{marca}', '{modello}', '{prezzo}', '{disponibilita}', '{filiale_id}')")
        else:
            query = (f"INSERT INTO motociclette (marca, modello, prezzo, disponibilita, filiale_id) VALUES ('{marca}', '{modello}', '{prezzo}', '{disponibilita}', '{filiale_id}')")

        if db.write_in_db(connection, query) != -1:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : "Query eseguita"}), 200
        else:
            print("Query non eseguita")
            return jsonify({"Esito" : "404", "Msg" : "Dati incorretti"}), 404
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/read_product", methods = ["GET"])
def ReadProduct():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        marca = dati.get("marca")
        if "id" in dati:
            if dati.get("admin") == True:
                if "modello" in dati:
                    modello = dati.get("modello")
                    query = (f"""SELECT m.id, m.marca, m.modello, m.prezzo, fi.nome, fi.indirizzo
                            FROM motociclette m
                            JOIN filiali fi ON m.filiale_id = fi.id
                            WHERE m.marca = '{marca}' and m.modello = '{modello}'
                            UNION
                            SELECT a.id, a.marca, a.modello, a.prezzo, fi.nome, fi.indirizzo
                            FROM automobili a
                            JOIN filiali fi ON a.filiale_id = fi.id
                            WHERE a.marca = '{marca}' and a.modello = '{modello}';""")
                else:
                    query = (f"""SELECT m.id, m.marca, m.modello, m.prezzo, fi.nome, fi.indirizzo
                            FROM motociclette m
                            JOIN filiali fi ON m.filiale_id = fi.id
                            WHERE m.marca = '{marca}'
                            UNION
                            SELECT a.id, a.marca, a.modello, a.prezzo, fi.nome, fi.indirizzo
                            FROM automobili a
                            JOIN filiali fi ON a.filiale_id = fi.id
                            WHERE a.marca = '{marca}';""")
        else:
            if "modello" in dati:
                modello = dati.get("modello")
                query = (f"""SELECT m.marca, m.modello, m.prezzo, fi.nome, fi.indirizzo
                        FROM motociclette m
                        JOIN filiali fi ON m.filiale_id = fi.id
                        WHERE m.marca = '{marca} and m.modello = '{modello}''
                        UNION
                        SELECT a.marca, a.modello, a.prezzo, fi.nome, fi.indirizzo
                        FROM automobili a
                        JOIN filiali fi ON a.filiale_id = fi.id
                        WHERE a.marca = '{marca}' and a.modello = '{modello}';""")
            else:
                query = (f"""SELECT m.marca, m.modello, m.prezzo, fi.nome, fi.indirizzo
                        FROM motociclette m
                        JOIN filiali fi ON m.filiale_id = fi.id
                        WHERE m.marca = '{marca}'
                        UNION
                        SELECT a.marca, a.modello, a.prezzo, fi.nome, fi.indirizzo
                        FROM automobili a
                        JOIN filiali fi ON a.filiale_id = fi.id
                        WHERE a.marca = '{marca}';""")
        
        rows = db.read_all_row(connection, query)
        if rows and len(rows) > 0:
            print("Veicoli trovato con successo!")
            return jsonify({"Esito" : "200", "Msg" : "Veicoli trovato con successo!", "veicoli":rows}), 200
        else:
            if "modello" in dati:
                print(f"Non è disponbile nessun veicolo con le seguenti caratteristiche: marca: {marca}, modello: {modello}")
                return jsonify({"Esito" : "404", "Msg" : f"Non è disponbile nessun veicolo con le seguenti caratteristiche: marca: {marca}, modello: {modello}"}), 404
            else:
                print(f"Non è disponbile nessun veicolo con le seguenti caratteristiche: marca: {marca}")
                return jsonify({"Esito" : "404", "Msg" : f"Non è disponbile nessun veicolo con le seguenti caratteristiche: marca: {marca}"}), 404
            
    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/update_product", methods = ["PUT"])
def UpdateProduct():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        id = dati.get("id")
        tipo = dati.get("tipo")
        marca = dati.get("marca")
        modello = dati.get("modello")
        nuovo_prezzo = dati.get("prezzo")
        disponibilita = dati.get("disponibilita")
        nuova_filiale = dati.get("filiale_id")
        if tipo == "automobile":
            query = f"""UPDATE automobili SET prezzo = '{nuovo_prezzo}', disponibilita = '{disponibilita}', filiale_id = '{nuova_filiale}' 
                        WHERE "id" = {id} AND marca = '{marca}' AND modello = '{modello}';"""
        else:
            query = f"""UPDATE motociclette SET prezzo = '{nuovo_prezzo}', disponibilita = '{disponibilita}', filiale_id = '{nuova_filiale}'
                        WHERE "id" = {id} AND marca = '{marca}' AND modello = '{modello}';"""
        if db.write_in_db(connection, query) != -1:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : f"Veicolo modificato con le seguenti informazioni:\nid: {id}, marca: {marca}, modello: {modello}, prezzo: {nuovo_prezzo}, disponibilita: {disponibilita}, filiale_id: {nuova_filiale}"}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : "Query fallita, controlla se l'id esiste"}), 404
    except:
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)

@api.route("/delete_product", methods=["DELETE"])
def DeleteProduct():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        id = dati.get("id")
        marca = dati.get("marca")
        modello = dati.get("modello")
        tipo = dati.get("tipo")
        if tipo == "automobile":
            query = f"""DELETE FROM automobili 
                        WHERE 
                            marca = '{marca}' AND modello = '{modello}' AND "id" = {id};"""
        else:
            query = f"""DELETE FROM motociclette 
                        WHERE 
                            marca = '{marca}' AND modello = '{modello}' AND "id" = {id};"""
    
        if db.write_in_db(connection, query) != -1:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : f"Veicolo id: {id}, marca: {marca}, modello: {modello} eliminato con successo"}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : "Query fallita, controlla se l'id esiste"}), 404
    except:
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)
        
@api.route("/check_filiale", methods = ["GET"])
def CheckFiliale():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        query = "SELECT * FROM filiali"
        rows = db.read_all_row(connection, query)
        if rows and len(rows) > 0:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : "Filiali trovate", "filiali":rows}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : "Query fallita, nessuna filiale trovata"}), 404
    except:
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)
    
@api.route("/balance", methods = ["GET"])
def Balance():
    connection = db.connect()
    if connection is None:
        print("Connessione al DB fallita")
        sys.exit()
    try:
        dati = request.json
        data_inizio = dati.get("data_inizio")
        data_fine = dati.get("data_fine")
        query = f"""SELECT v.id AS vendita_id, v.data_vendita, v.tipo_oggetto, f.nome AS filiale_nome,
                CASE 
                    WHEN v.tipo_oggetto = 'automobile' THEN a.marca || ' ' || a.modello
                    WHEN v.tipo_oggetto = 'motocicletta' THEN m.marca || ' ' || m.modello
                    WHEN v.tipo_oggetto = 'accessorio' THEN ac.nome || ' (' || ac.categoria || ')'
                END AS descrizione_oggetto,
                CASE 
                    WHEN v.tipo_oggetto = 'automobile' THEN a.prezzo
                    WHEN v.tipo_oggetto = 'motocicletta' THEN m.prezzo
                    WHEN v.tipo_oggetto = 'accessorio' THEN ac.prezzo
                END AS prezzo
                FROM vendite v
                JOIN filiali f ON v.filiale_id = f.id
                LEFT JOIN automobili a ON v.oggetto_id = a.id AND v.tipo_oggetto = 'automobile'
                LEFT JOIN motociclette m ON v.oggetto_id = m.id AND v.tipo_oggetto = 'motocicletta'
                LEFT JOIN accessori ac ON v.oggetto_id = ac.id AND v.tipo_oggetto = 'accessorio'
                WHERE v.data_vendita BETWEEN '{data_inizio}' AND '{data_fine}'
                ORDER BY v.data_vendita ASC;
                """
        rows = db.read_all_row(connection, query)
        if rows and len(rows) > 0:
            print("Query eseguita con successo")
            return jsonify({"Esito" : "200", "Msg" : "Ecco il bilancio", "vendite":rows}), 200
        else:
            print("Query fallita")
            return jsonify({"Esito" : "404", "Msg" : f"Query fallita, nessuna vendita tra {data_inizio} e {data_fine}"}), 404
    except:
        return jsonify({"Esito" : "500", "Msg" : "Errore con il server, riprova più tardi"}), 500
    finally:
        db.close(connection)
    
api.run(host="127.0.0.1", port=8080, ssl_context="adhoc", debug=True)