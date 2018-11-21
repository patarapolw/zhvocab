from zhlib import zh

from zhvocab.util import get_freq


for row in '''
压力
怀孕
癌症
传染
感冒
呕吐
过敏
糖尿病
发烧
头疼
高血压
流感
肺炎
失眠
白血病
性病
哮喘
腹泻
天花
痰
肿胀
打喷嚏
痒痒
便秘
梅毒
神经痛
腹痛
白内障
低血压
宿醉
流鼻涕
脓化
足癣
结膜炎
荨麻疹
小儿麻痹症
消化性溃疡
扁桃体炎
龋齿
'''.strip().split('\n'):
    # print(round(get_freq(row), 3))

    result = zh.Vocab.match(row.strip())
    if len(result) > 0:
        print(result[0].pinyin)
    else:
        print()
