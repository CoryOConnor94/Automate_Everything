from pathlib import Path

from rename_files import root_dir

root_dir = Path('../destination/files')

for path in root_dir.glob("*.txt"):
    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()