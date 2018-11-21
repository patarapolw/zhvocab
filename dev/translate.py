from zhlib import zh

from zhvocab.util import get_freq


for row in '''
流血
肺核
远视
近视
脑出血
盲肠炎
头晕
发抖
寒冷
心脏衰竭
累
有食欲
胃口好
疲倦
发炎
食物中毒
消化不良
咳嗽
泌尿道感染
痔疮
'''.strip().split('\n'):
    print(round(get_freq(row), 3))

    # result = zh.Vocab.match(row.strip())
    # if len(result) > 0:
    #     print(result[0].pinyin)
    # else:
    #     print()
