from pathlib import Path
import zipfile

root_dir = Path('../files')
destination_path = Path('../destination')

for path in root_dir.glob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zf:
        zf.extractall(path=destination_path)