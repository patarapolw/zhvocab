from zhlib import zh

from zhvocab.util import get_freq


for row in '''
商人
画家
学校
下课
睡觉
词典
火车
地方
橘子
榴莲
山竹
苹果
太极拳
出租车
看不见
飞机场
空调机
电影院
对不起
没关系
打电话
帅
千秋万代
瓜田李下
不卑不亢
高风亮节
默默无闻
赤胆忠心
辆
皆大欢喜
盛情难却
闭月羞花
沉鱼落雁
门庭若市
公司
职员
现在
一遍
初一
告诉
笑里藏刀
投石问路
金盆洗手
门口
面食
玩
翻译
小名
男主角
女主角
清迈
华侨
潮州话
幸运
重要
相似
学问
经验
决定
半年
方便
安装
输入
卸载
登录
适
版本
状态
全角
表情
斗图
语音
跨屏
屏幕
编辑器
偏好
外观
关于
同步
通讯录
设置
反馈
脸谱
乐谱
繁体
'''.strip().split('\n'):
    print(round(get_freq(row), 3))
    # result = zh.Vocab.match(row.strip())
    # if len(result) > 0:
    #     print(result[0].pinyin)
    # else:
    #     print()
