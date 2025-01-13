from pathlib import Path

root_dir = Path('../files')
files_path = root_dir.glob("**/*")

for path in files_path:
    if path.is_file():
        parent_folder = path.parts
        subfolders = path.parts[1:3]
        new_filename = "-".join(subfolders) + '-' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)