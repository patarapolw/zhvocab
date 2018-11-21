import csv

from .dir import BASE
from . import db


def import_csv():
    for csv_filename in BASE.joinpath('csv').glob('**/*.csv'):
        with csv_filename.open() as f:
            print(csv_filename.stem)

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
                db_vocab.traditional = row['traditional']
                db_vocab.japanese = row['japanese']
                db_vocab.related = row['related']
                db_vocab.frequency = float(row.get('frequency'))
                db_vocab.add_tags(row.get('tags', '') + '\n' + csv_filename.stem)
                db_vocab.save()
