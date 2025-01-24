from pathlib import Path

files_dir = Path('files')
for file_path in files_dir.iterdir():
    with open(file_path, 'r') as file:
        content = file.read()
        new_content = content[:-1]

    with open(file_path, 'w') as file:
        file.write(new_content)

