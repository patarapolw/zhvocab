from zhlib import zh

from zhvocab.util import get_freq


for row in '''
鱼鳔汤
面条
炸虾
腊肠
煎饺
白菜豆腐汤
枸杞炖鸡
宫保鸡丁
烧鸡
烧卖
面包
甜点
开胃菜
米饭
咖喱饭
炒饭
鸡蛋和培根
火腿煎蛋
粥
海参汤
清汤
寿司
三明治
麻婆豆腐
臭豆腐
凉面
熏鲑鱼
清蒸鱼
糖醋鱼
蟹肉并
北京烤鸭
红烧暴雨
泡菜
炒青菜
炒面
佛跳墙
鱼香肉丝
披萨
西红柿炒鸡蛋
拉面
牛排
意大利面
蔬菜沙拉
寿喜烧
小笼包
香肠
火锅
麻辣烫
烤乳猪
鱼翅汤
快餐
海鲜
素食
热狗
汉堡包
早餐
午餐
晚餐
'''.strip().split('\n'):
    # print(round(get_freq(row), 3))

    result = zh.Vocab.match(row.strip())
    if len(result) > 0:
        print(result[0].pinyin)
    else:
        print()
