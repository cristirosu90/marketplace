"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import json
import datetime


def genereaza_id_comanda(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda():
    with open('baza_de_date/marketplace.json', 'r') as j:
        d = json.load(j)
    while True:
        data_inregistrare = str(datetime.datetime.now())
        id_comanda = {
            'id_comanda': data_inregistrare,
            'detalii_comanda': []
        }

        while True:
            nume_produs = input("Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n")
            if nume_produs == 'stop':
                break
            for i in d['produse']:
                if d['produse'][i]['nume produs'] == nume_produs:
                    id_produs = 1
                    break
                else:
                    print(f'Produsul {nume_produs} nu exista.')
                    continue
                cantitate = int(input('Introduceti cantitatea produsului selectat: '))
                id_comanda['detalii_comanda'].append({id_produs: cantitate})
                idcomanda = str(genereaza_id_comanda(json.dumps(id_comanda)))
                id_comanda['id_comanda'] = idcomanda
                d['comenzi'][idcomanda] = id_comanda
                alt_produs = input('Doriti sa mai adaugati un produs? da/stop: ')
                if alt_produs == 'stop':
                    break
            break
        with open('baza_de_date/marketplace.json', 'w') as j:
            j.write(json.dumps(d, indent=4))

    """
    Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
    Ca prim input dam Produsul, apoi Cantitatea
    Generam ID-ul unic comenzii
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """
    pass


def modifica_comanda():
    """
    Introduceti de la tastatura textul: "Introduceți identificatorul comenzii care se modifica: "
    Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
        "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        Creeam logica pentru cele 4 variante
        Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
        Din nou, Citim, Actionam, Scriem
    """

    pass


def listeaza_toate_comenzile():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """
    pass


def sterge_o_comanda():
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """

    pass
