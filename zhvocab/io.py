import csv

from .dir import BASE
from . import db


def import_csv():
    csv_path = BASE.joinpath('csv')

    for csv_filename in csv_path.glob('**/*.csv'):
        with csv_filename.open() as f:
            filename_tag = str(csv_filename.relative_to(csv_path))

            reader = csv.DictReader(f)
            for row in reader:
                db_vocab = db.Vocab.get_or_none(
                    simplified=row['simplified']
                )
                if not db_vocab:
                    db_vocab = db.Vocab.create(
                        simplified=row['simplified'],
                        english=row['english'],
                        pinyin=row['pinyin']
                    )

                db_vocab.english = row['english']
                db_vocab.pinyin = row['pinyin']
                db_vocab.traditional = row.get('traditional')
                db_vocab.japanese = row.get('japanese')
                db_vocab.related = row.get('related')

                try:
                    db_vocab.frequency = float(row.get('frequency'))
                except ValueError:
                    pass

                db_vocab.add_tags(row.get('tags', '') + '\n' + filename_tag)
                db_vocab.save()
