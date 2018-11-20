import re


def zh_split(value):
    return [x.strip() for x in re.split(r'[,，\n]', value) if x.strip()]
