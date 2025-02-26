import os

def save_cpp_headers_to_txt(output_file="output.txt"):
    current_directory = os.getcwd()  # Récupère le répertoire où le script est lancé

    with open(output_file, "w", encoding="utf-8") as outfile:
        found_files = False  # Permet de vérifier si des fichiers ont été trouvés

        for root, _, files in os.walk(current_directory):
            for file in files:
                if file.endswith((".hpp", ".cpp")):
                    found_files = True
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            outfile.write(f"===== {file} =====\n")  # Titre du fichier
                            outfile.write(infile.read() + "\n\n")  # Contenu du fichier
                    except Exception as e:
                        print(f"Erreur lors de la lecture de {file}: {e}")

        if not found_files:
            print("Aucun fichier .hpp ou .cpp trouvé.")

if __name__ == "__main__":
    save_cpp_headers_to_txt()
    print(f"Tous les fichiers .hpp et .cpp ont été enregistrés dans output.txt")

