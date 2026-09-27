

import os
from pathlib import Path

items_string = """
{
    "model": {
        "type": "minecraft:model",
        "model": "us:item/$NAME$"
    }
}
"""

models_string = """
{
    "parent": "minecraft:item/generated",
    "textures": {
        "layer0": "us:item/$NAME$"
    }
}
"""

def find_json_files_crawl(dir: Path) -> list[Path]:

    json_files = []

    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".json"):
                new_file_path = Path(root) / file
                json_files.append(new_file_path)

    return json_files

def write_json_file(raw: str, file_path: Path) -> None:
    with open(file_path, 'w') as f:
        f.write(raw)

def create_png_files(json_files: list[Path], missing_texture: Path, out: Path) -> None:

    # creates a new missing texture png file with name of the json file in the out directory
    for json_file in json_files:
        new_png_file = out / f'{json_file.stem}.png'
        if not new_png_file.exists():
            print(f'creating {new_png_file}')
            with open(missing_texture, 'rb') as f:
                missing_texture_data = f.read()
            with open(new_png_file, 'wb') as f:
                f.write(missing_texture_data)


if __name__ == "__main__":

    ...