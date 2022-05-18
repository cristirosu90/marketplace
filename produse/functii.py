"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import json
import datetime


def genereaza_id_produs(nume_produs, pret, cantitate):
    hash_object = hashlib.md5(bytes(nume_produs + pret, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs():
    while True:
        nume_produs = input('Introduceti numele produsului de adaugat: ')
        if len(nume_produs) in range(0, 51):
            pret = input('Introduceti pretul produsului de adaugat: ')
            cantitate = input('Introduceti cantitatea produslui de adaugat: ')
            id_produs = str(genereaza_id_produs(nume_produs, pret, cantitate))
            data_inregistrare = str(datetime.datetime.now())
            with open('baza_de_date/marketplace.json', 'r') as j:
                d = json.load(j)
                d['produse'][id_produs] = {
                    'nume produs': nume_produs,
                    'pret': pret,
                    'cantitate': cantitate,
                    'data_inregistrare': data_inregistrare
                }
            with open('baza_de_date/marketplace.json', 'w') as j:
                j.write(json.dumps(d, indent=4))
                alt_produs = input('Doriti sa adaugati alt produs? da/nu: ')
                if alt_produs == 'nu':
                    break
        else:
            print('Nume invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere.')


    '''
    Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'Introduceti pretului produsului de adaugat: '
    Generam ID-ul unic produsului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    '''
    pass


def listeaza_toate_produsele():
    with open('baza_de_date/marketplace.json', 'r') as f:
        d = json.load(f)
        print(json.dumps(d['produse'], indent=4))

    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    pass


def sterge_produs():
    while True:
        produs_de_sters = input('Introduceti produsul pe care doriti sa-l stergeti: ')
        with open('baza_de_date/marketplace.json', 'r') as j:
            d = json.load(j)
            for i in d['produse']:
                if d['produse'][i]['nume produs'] == produs_de_sters:
                    del d['produse'][i]
                    break
            else:
                print('Produs inexistent.')
        with open('baza_de_date/marketplace.json', 'w') as j:
            j.wirte(json.dumps(d, indent=4))
        alt_produs_de_sters = input('Doriti sa stergeti alt produs? da/nu: ')
        if alt_produs_de_sters == 'nu':
            break
    pass
