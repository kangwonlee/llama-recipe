import json
import pathlib


def remove_ipynb_hash(folder:pathlib.Path=pathlib.Path(__file__).parent.resolve()):
    for file in folder.glob('*.ipynb'):
        try:
            data = json.loads(file.read_text(encoding='utf-8'))

            # remove ipynb id and metadata
            for cell in data['cells']:
                if 'id' in cell:
                    del cell['id']
                if 'metadata' in cell:
                    if (
                        ('id' in cell['metadata']) and
                        (cell['metadata']['id'] != "view-in-github")
                    ):
                        del cell['metadata']['id']

            with open(file, 'w') as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("File not found :", file)
        except json.JSONDecodeError:
            print("Invalid JSON file :", file)


if "__main__" == __name__:
    remove_ipynb_hash()
