from pathlib import Path

root_dir = Path('../files')

for path in root_dir.rglob("*.txt"):
    if path.is_file():
        new_file_path = path.with_suffix(".csv")
        path.rename(new_file_path)