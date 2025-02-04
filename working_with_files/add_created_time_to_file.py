from pathlib import Path
from datetime import datetime

root_dir = Path('../files')

for path in root_dir.glob("**/*"):
    if path.is_file():
        date_created = datetime.fromtimestamp(path.stat().st_ctime)
        date_created_str = date_created.strftime('%Y-%m-%d_%H:%M:%S')
        new_file_name = date_created_str + '_' + path.name
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)
