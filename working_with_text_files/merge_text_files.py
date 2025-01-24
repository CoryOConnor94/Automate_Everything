from pathlib import Path


files_dir = Path('files')
merged = ''

for index, file_path in enumerate(files_dir.iterdir()):
    with open(file_path, 'r') as file:
        content = file.readlines()
        new_content = content[1:]
    if index == 0:
        content = ''.join(content)
        merged = merged + content + '\n'
    else:
        new_content = ''.join(new_content)
        merged = merged + new_content + '\n'

print(merged)

with open('merged.txt', 'w') as file:
    file.write(merged)