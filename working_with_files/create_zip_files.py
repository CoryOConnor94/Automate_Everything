from pathlib import Path
import zipfile

from rename_files import root_dir

root_dir = Path('../files')
zip_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(zip_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)