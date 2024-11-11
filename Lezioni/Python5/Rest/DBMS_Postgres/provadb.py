import sys
import os
import os.path
import time

#pip3 install psycopg2-binary
import dbclient as db


print("Inizio programma prova database")
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()

sQuery = "insert into Cittadini (nome, cognome, dataNascita, codFiscale) values ('Walter', 'Albano', '1890-12-07', 'dcfvff70b34h501u')"
db.write_in_db(cur, sQuery)

sQuery = "select * from Cittadini;"
iNumRows = db.read_in_db(cur,sQuery)
for ii in range(0,iNumRows):
	myrow = db.read_next_row(cur)
	print(myrow)
	
