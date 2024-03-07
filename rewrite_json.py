import json
import pathlib


def main():
    folder = pathlib.Path(__file__).parent.resolve()

    for file in folder.glob('*.ipynb'):
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


if "__main__" == __name__:
    main()
