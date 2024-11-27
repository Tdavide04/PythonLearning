import json
import jsonschema
import requests
import sys


def JsonSerialize(data, sFile):
    with open(sFile, "w") as write_file:
        json.dump(data, write_file,indent=4)

def JsonDeserialize(sFile):
    with open(sFile, "r") as read_file:
        return json.load(read_file)


def print_list(lData,sRoot):
    for element in lData:
        if type(element) is str:
            print("\t" + element)
        #print(type(dData[keys]))
        if type(element) is dict:
            print_dictionary(element,sRoot)
        if type(element) is list:
            print_list(element,sRoot)

def print_dictionary(dData, sRoot):
    for keys, values in dData.items():
        if sRoot != "":
            print("Trovata chiave " + sRoot + "." + keys)
        else:
           print("Trovata chiave " + keys) 
        #print(values)
        #print(type(dData[keys]))
        if type(dData[keys]) is dict:
            if sRoot != "":
                print_dictionary(dData[keys],sRoot + "." + keys)
            else:
                print_dictionary(dData[keys],keys)
        if type(dData[keys]) is list:
            if sRoot != "":
                print_list(dData[keys],sRoot + "." + keys)
            else:
                print_list(dData[keys],keys)
    
def start():
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi cittadino (es. cert. residenza)")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune)")
    print("5. Esci") 

