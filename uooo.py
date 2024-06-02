import os
import pyperclip

def read_all_files_in_directory(directory, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = {'.git', '.venv', '__pycache__', 'main.py'}

    all_text = ""
    for root, dirs, files in os.walk(directory):
        # Filtrar diretórios ignorados
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            # Ignorar arquivos .git
            if file == '.git':
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    all_text += f"--- {file_path} ---\n{file_content}\n\n"
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return all_text

def main():
    project_directory = '.'  # Altere para o diretório do seu projeto, se necessário
    all_text = read_all_files_in_directory(project_directory)

    # Salvar todo o conteúdo em um arquivo de texto
    output_file = 'output.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(all_text)

    # Copiar o conteúdo para a área de transferência
    pyperclip.copy(all_text)
    print(f"All text copied to clipboard and saved to {output_file}.")

if __name__ == "__main__":
    main()
