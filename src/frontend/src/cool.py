import os

def collect_code_files(output_file="resultat.txt", extensions=None):
    if extensions is None:
        # Extensions que tu veux inclure (modifiables si besoin)
        extensions = [".jsx", ".js", ".ts", ".tsx", ".css"]

    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, _, files in os.walk("."):
            for file in files:
                # Vérifie l'extension
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    # En-tête de fichier
                    outfile.write(f"\n// ====== Fichier : {file_path} ======\n\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            outfile.write(infile.read() + "\n")
                    except Exception as e:
                        # En cas de problème de lecture
                        outfile.write(f"// Erreur de lecture : {e}\n")

if __name__ == "__main__":
    collect_code_files()

