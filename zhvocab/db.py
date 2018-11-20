import peewee as pv
from playhouse import signals
from playhouse.shortcuts import model_to_dict

from .util import zh_split, get_freq
from .dir import BASE

database = pv.SqliteDatabase(str(BASE.joinpath('zhvocab.db')))


class ZhListField(pv.TextField):
    def db_value(self, value):
        if value and value.strip():
            return '，'.join(zh_split(value))


class FilledTextField(pv.TextField):
    def db_value(self, value):
        if value and value.strip():
            return value.strip()


class BaseModel(signals.Model):
    class Meta:
        database = database


class Tag(BaseModel):
    name = pv.TextField(collation='NOCASE', unique=True)

    @property
    def vocabs(self):
        return [model_to_dict(v) for v in self._vocabs]


class Vocab(BaseModel):
    english = FilledTextField(unique=True)
    simplified = FilledTextField(unique=True)
    pinyin = FilledTextField()
    traditional = ZhListField(null=True)
    japanese = ZhListField(null=True)
    related = ZhListField(null=True)
    frequency = pv.FloatField(null=True)
    _tags = pv.ManyToManyField(Tag, backref='_vocabs')

    @property
    def tags(self):
        return [t.name for t in self._tags]

    @tags.setter
    def tags(self, value):
        for tag in zh_split(value):
            Tag.get_or_create(name=tag)[0]._vocabs.add(self)

    def to_dict(self):
        return model_to_dict(self, extra_attrs=['tags'])


VocabTag = Vocab._tags.get_through_model()


@signals.pre_save(sender=Vocab)
def vocab_pre_save(model_class, instance, created):
    if not instance.frequency:
        instance.frequency = get_freq(instance.simplified)
