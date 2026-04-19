import csv
import pprint

# Fichier de données
file_mensajes = r".\source\Mensajes"
file_airport = r".\source\airports.csv"

# Code possible à tester :
possibilite = {1:[2, 3, 2],
               2:[2, 3, 1, 3],
               3:[1, 3, 2],
               4:[3, 2, 2, 4],
               5:[4, 1, 3, 2],
               6:[6, 1, 4]
                }


# Formatage des différents messages dans une collection
def open_file(file_path):
    """Fichier de texte en utf8"""
    with open(file_path, 'r', encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def decoupe_message(file_contenu, filtre: bool):
    """Fait un nouveau message dès qu'une nouvelle ligne commence par 'Mensaje'"""
    messages = {}
    titre_courant = None
    code_courant = {}  # Dictionnaire pour stocker les lignes du message courant

    for ligne in file_contenu:
        # Suppression de la ligne '1 2 3 4 5 6 7 8 9 10 11 12'
        if not ligne == "1 2 3 4 5 6 7 8 9 10 11 12":
            if ligne.startswith("Mensaje"):
                if code_courant:  # Si le message courant n'est pas vide, on le sauvegarde
                    if not filtre or 'Yahuar Huácac' in titre_courant:
                        messages[titre_courant] = code_courant
                titre_courant = ligne
                code_courant = {}  # On réinitialise pour le prochain message
            else:
                # on retire les 2 premiers caractères de la ligne
                numero_ligne = int(ligne[:1])
                # On decoupe le texte les caractères espaces
                code = ligne[2:].split(" ")
                if len(code) != 12:
                    raise ValueError("Une ligne du fichier source ne comprend pas 12 caractères :\n"
                                     f"{titre_courant} - {ligne}")
                # On ajoute la ligne au message courant
                code_courant[numero_ligne] = code

    return messages


def parsing_airports(csv_file, filtre: bool):
    """En tête de colonne ligne 1 du csv :
    code,icao,name,latitude,longitude,elevation,url,time_zone,city_code,country,city,state,county,type
    Recuperation uniquement de code, name et country
    Filtre sur les aéroport français et sud Américain"""
    airports = {}
    with open(csv_file, 'r', encoding="utf-8") as csv_file:
        file_read = csv.reader(csv_file, delimiter=",")

        array = list(file_read)

    # Recuperer le code pour faire un dictionnaire
    for ligne in array:
        # Si filtre Amerique du sud et france
        if not filtre or (ligne[9] == "FR" or (ligne[7].startswith("America") and float(ligne[3]) < 5)):
            # Si ligne 9 contient "FR" ou ligne 7 commence par "America"
            airports[ligne[0]] = [ligne[2], ligne[7], ligne[9]]

    return airports


def decode_mesaje(code, mesaje):
    """Trouver les 6 caractères du code dans un mesaje"""
    caractere = ""
    ligne = 1
    for numero in code:
        try:
            caractere += mesaje[ligne][numero-1]
        except IndexError:
            caractere += "!"
        ligne = ligne+1

    return caractere[:3], caractere[3:]

def verify_airport(code, airport_list):
    """Verify airport code in the list of airports"""
    if code in airport_list.keys():
        return airport_list[code]
    else:
        return False


if __name__ == '__main__':

    # Lire le fichier
    contenu = open_file(file_mensajes)

    # Découpage des messages
    Mensajes = decoupe_message(contenu, False)
    print(Mensajes)

    # Recuperation des aeroports
    Aeroports = parsing_airports(file_airport, True)
    print(Aeroports)
    print(len(Aeroports.keys()))

    # Faire tous les decodages
    results = {}
    count = 0
    for mensaje in Mensajes:
        count += 1
        message = ""
        for num_ligne in range(1, 6):
            for noeud in possibilite[num_ligne]:
                message += str(Mensajes[mensaje][num_ligne][noeud-1])

        air_dep = verify_airport(message[:3], Aeroports)
        air_arr = verify_airport(message[3:6], Aeroports)
        air_arr2 = verify_airport(message[-3:], Aeroports)

        results[count] = (message, air_dep, air_arr, air_arr2)

    pprint.pp(results)

