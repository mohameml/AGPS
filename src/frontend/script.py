import os

# Ici, on parcourt le dossier courant
frontend_path = '.'
output_file = 'frontend_code.txt'

# Extensions des fichiers à inclure
extensions_to_include = ['.js', '.jsx', '.ts', '.tsx', '.json', '.css', '.html']

def should_include(file_name):
    return any(file_name.endswith(ext) for ext in extensions_to_include)

with open(output_file, 'w', encoding='utf-8') as output:
    for root, dirs, files in os.walk(frontend_path):
        # Ignore node_modules
        if 'node_modules' in dirs:
            print(f"Ignoring node_modules in: {root}")
            dirs.remove('node_modules')

        print(f"Looking in: {root}")
        print(f"Files found: {files}")

        for file in files:
            if should_include(file):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, frontend_path)
                print(f"Adding file: {relative_path}")

                output.write(f'--- Start of {relative_path} ---\n\n')
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        output.write(content)
                except Exception as e:
                    print(f"Error reading {relative_path}: {e}")
                    output.write(f'Could not read {relative_path}: {e}\n')
                
                output.write(f'\n\n--- End of {relative_path} ---\n\n\n')

print(f"\n✅ Terminé ! Le contenu est dans : {output_file}")
