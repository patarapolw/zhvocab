from zhlib import zh

from zhvocab.util import get_freq, zh_split

all_entries = []

for vocab in zh_split('''
秋葵 [qiū kuí] กระเจี๊ยบขาว
山茄 [shān qié] กระเจี๊ยบแดง
蒜 [suàn] กระเทียม
蒜头 [suàn tóu] กระเทียม
菜花 [cài huā] กะหล่ำดอก
包心菜 [bāo xīn cài]，卷心菜 [juǎn xīn cài] กะหล่ำปลี
韭菜 [jiǔ cài] กุยช่าย
小玉米 [xiǎo yù mǐ] ข้าวโพดอ่อน
姜 [jiāng] ขิง
芹菜 [qín cài] ขึ้นช่าย
芥菜 [jiè cài] คะน้า
红萝卜 [hóng luó bǔ] แครอท
马铃薯 [mǎ líng shǔ] มันฝรั่ง
葱 [cōng] ต้นหอม
香芋 [xiāng yù] ตะไคร้
黄瓜 [huáng guā] แตงกวา
豌豆 [wān dòu] ถั่ว
豆芽 [dòu yá] ถั่วงอก
豆角 [dòu jiǎo] ถั่วฝักยาว
豌豆 [wān dòu] ถั่วลันเตา
青菜花 [qīng cài huā] บรอกโคลี
丝瓜 [sī guā] บวบ
菠菜 [bō cài] ปวยเล้ง,  ผักโขม
酸泡菜 [suān pào cài] ผักดอง
芹菜 [qín cài] ผักคึ่นช่าย
茄子 [qié zǐ] มะเขือเปราะ
蕃茄 [fān qié] มะเขือเทศ
青菜 [qīng cài] ผักกวางตุ้ง
白菜 [bái cài] ผักกาดขาว
芫荽 [yuán suī] ผักชี
空心菜 [kōng xīn cài] ผักบุ้ง
辣椒 [là jiāo] พริก
胡椒 [hú jiāo] พริกไทย
柿子椒 [shì zǐ jiāo] พริกหยวก
甜椒 [tián jiāo] พริกหวาน
冬瓜 [dōng guā] ฟัก
南瓜 [nán guā] ฟักทอง
苦橙 [kǔ chéng] มะกรูด
西红柿 [xī hóng shì] มะเขือเทศ
小茄子 [xiǎo qié zǐ] มะเขือเปราะ
茄子 [qié zǐ] มะเขือยาว
苦瓜 [kǔ guā] มะระ
葱 [cōng] หัวหอม
笋 [sǔn] หน่อไม้
芦笋 [lú sǔn] หน่อไม้ฝรั่ง
竹笋 [zhú sǔn] หน่อไม้
红葱头 [hóng cōng tóu] หอมแดง
洋葱 [yáng cōng] หอมใหญ่
萝卜 [luó bǔ] หัวไชเท้า
金针菇 [jīn zhēn gū] เห็ดเข็มทอง
草菇 [cǎo gū] เห็ดฟาง
香菇 [xiāng gū] เห็ดหอม
木耳 [mù ěr] เห็ดหูหนู
紫苏 [zǐ sū] โหระพา
'''):
    entry = [''] * 7
    entry[1] = vocab
    entry[6] = str(round(get_freq(vocab), 3))

    results = zh.Vocab.match(vocab)
    if len(results) > 0:
        entry[0] = '，'.join(r.english for r in results if r.english)
        entry[2] = '，'.join(r.traditional for r in results if r.traditional and r.traditional != vocab)
        entry[3] = '，'.join(r.pinyin for r in results if r.pinyin)

    all_entries.append(entry)

all_entries = sorted(all_entries, key=lambda x: -float(x[6]))

print('\n'.join('\t'.join(e) for e in all_entries))
