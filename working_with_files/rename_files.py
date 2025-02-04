from pathlib import Path

root_dir = Path('../files')
files_path = root_dir.iterdir()

for path in files_path:
    new_file_name = "new-" + path.stem + path.suffix
    new_file_path = path.with_name(new_file_name)
    path.rename(new_file_path)
