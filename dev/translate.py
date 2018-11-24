from zhlib import zh

from zhvocab.util import get_freq, zh_split

all_entries = []

for vocab in zh_split('''
紫苏
竹笋
小黄瓜
香菇
柠檬草
柠檬
小玉米
西红柿
洋葱
青菜
芹菜
茄子
秋葵
青菜花
豌豆
丝瓜
芫荽
柿子椒
甜椒
蒜头
南瓜
木耳
'''):
    entry = [''] * 7
    entry[1] = vocab
    entry[6] = str(round(get_freq(vocab), 3))

    results = zh.Vocab.match(vocab)
    if len(results) > 0:
        entry[0] = '，'.join(r.english for r in results if r.english)
        entry[2] = '，'.join(r.traditional for r in results if r.traditional and r.traditional != vocab)
        entry[3] = '，'.join(r.pinyin for r in results if r.pinyin)

    all_entries.append([entry[3]])

# all_entries = sorted(all_entries, key=lambda x: -float(x[6]))

print('\n'.join('\t'.join(e) for e in all_entries))
