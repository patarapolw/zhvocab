from zhlib import zh

from zhvocab.util import get_freq, zh_split

all_entries = []

for vocab in zh_split('''
白菜
包心菜
菠菜
草菇
菜花
葱
冬瓜
豆角
豆芽
芥蓝菜
红萝卜
胡椒
红葱头
茼蒿
金针菇
姜
韭菜
苦橙
空心菜
萝卜
辣椒
'''):
    entry = [''] * 7
    entry[1] = vocab
    entry[6] = str(round(get_freq(vocab), 3))

    results = zh.Vocab.match(vocab)
    if len(results) > 0:
        entry[0] = '，'.join(r.english for r in results if r.english)
        entry[2] = '，'.join(r.traditional for r in results if r.traditional and r.traditional != vocab)
        entry[3] = '，'.join(r.pinyin for r in results if r.pinyin)

    all_entries.append([entry[0]])

# all_entries = sorted(all_entries, key=lambda x: -float(x[6]))

print('\n'.join('\t'.join(e) for e in all_entries))
