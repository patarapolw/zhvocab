import regex
from wordfreq import word_frequency


def zh_split(value):
    return regex.findall(r'\p{IsHan}+', value)


def get_freq(word):
    return word_frequency(word.strip(), 'zh') * 10 ** 6
