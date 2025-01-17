import json
import os

from extract_text import extract_text_by_page


def export_as_json(pdf_path, json_path):  # конвертируем pdf в json
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []

    counter = 1
    for page in extract_text_by_page(pdf_path):
        text = page  # можно ли это убрать?
        print('')
        # page = {'Page_{}'.format(counter): text}
        data['Pages'].append(page)
        print(data)
        counter += 1

    with open(json_path, 'w') as fh:
        json.dump(data, fh, ensure_ascii=False)

if __name__ == '__main__':
    pdf_path = 'Fkko2019.pdf'
    json_path = 'Fkko2019.json'
    export_as_json(pdf_path, json_path)
