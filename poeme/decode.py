import os

# Ce code est un exemple de décodage d'un message chiffré à l'aide d'une clé de substitution.
# Chaque couple de chiffre représente le numéro de ligne, et la position du caractère dans la ligne
code = [[8, 13], [2, 6], [6, 1], [12, 3], [2, 6], [5, 1], [6, 12]]


# Parse le texte d'un fichier source sous forme en récupérant les lettres codées
def decode(file_tab, code):
    decoded = []
    for code_block in code:
        ligne = code_block[0] - 1
        colonne = code_block[1] - 1
        try:
            decoded.append(file_tab[ligne][colonne])
        except IndexError:
            decoded.append("_")
    return decoded


def convert_file(file_path):
    """Fichier de texte en utf8"""
    with open(file_path, 'r', encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def list_files(directory):
    files = []
    # Lister les fichiers du répertoire
    for file in os.listdir(directory):
        files.append(file)
    return files

def clean_text(tab_texte):
    """Enlève du texte tous les espaces et caractères de ponctuation."""
    nouveau_texte = []
    for ligne_texte in tab_texte:
        texte = ligne_texte.replace(" ", "")
        texte = texte.replace("'", "")
        texte = texte.replace(",", "")
        texte = texte.replace(".", "")
        texte = texte.replace(":", "")
        texte = texte.replace("!", "")
        texte = texte.replace("?", "")
        texte = texte.replace(";", "")
        texte = texte.replace("(", "")
        texte = texte.replace(")", "")
        texte = texte.replace("—", "")
        texte = texte.replace("’", "")
        texte = texte.replace("-", "")
        texte = texte.replace("_", "")
        nouveau_texte.append(texte)
    return nouveau_texte

def reverseCode(resultat : str):
    return resultat[::-1]


# Main
if __name__ == '__main__':
    for file in list_files('./source'):
        tableau = convert_file(os.path.join('source', file))
        result = decode(tableau, code)
        tableau_clean = clean_text(tableau)
        result_clean = decode(tableau_clean, code)
        # convetir liste en string
        res = ''.join(result)
        result_clean = ''.join(result_clean)
        print(res, result_clean, reverseCode(res), reverseCode(result_clean), file, sep=' - ')
