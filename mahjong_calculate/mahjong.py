import pandas as pd
import numpy as np
import re

# 固定参数
## 底
base = 1
## 番数
fan_amt = {'门清': 1, '自摸': 1, '庄': 1, '七对': 1, '一条龙': 1, '没混': 1, '海底捞': 1, '海捞': 1,
'杠开花': 1, '杠开': 1, '杠上开花': 1, '捉五魁': 1, '捉五': 1, '混一色': 1, '混清': 1,
'豪华七对': 2, '豪七': 2, '本混龙': 2, '十三幺': 3, '双豪七': 3, '清一色': 3, '风一色': 4, '三豪七': 4}
## 锅外钱数
# money_amt_out = {'四混': 40, '天胡': 80, '地胡': 80, '炸胡': -30, '跟一轮': 10}
## 锅内钱数
# money_amt_in = {'明杠': 2, '暗杠': 4}

# 计算函数
def Mahjong_settle(hu_type,base = 2):
    # type = list(set(fan_amt).intersection(set(re.split('[，,]', re.sub(' ', '', hu_type)))))
    # other_out = zhuang_out = 0
    # is_zhuang = list(set(['庄']).intersection(set(re.split('[，,\\000]', hu_type))))
    # is_upstairs = list(set(['楼上']).intersection(set(re.split('[，,\\000]', hu_type))))
    type = list(set(fan_amt).intersection(set(hu_type)))
    other_out = zhuang_out = 0
    is_zhuang = list(set(['庄']).intersection(set(hu_type)))
    is_upstairs = list(set(['楼上']).intersection(set(hu_type)))
    if len(is_zhuang) != 0:
        other_out = -2**np.sum([fan_amt[mm] for mm in type])/2*2**len(is_upstairs)*base
        win = 2**np.sum([fan_amt[mm] for mm in type])*3/2*2**len(is_upstairs)*base
    else:
        other_out = -2**np.sum([fan_amt[mm] for mm in type])/2*2**len(is_upstairs)*base
        zhuang_out = -2*2**np.sum([fan_amt[mm] for mm in type])/2*2**len(is_upstairs)*base
        win = 2*2**np.sum([fan_amt[mm] for mm in type])*2**len(is_upstairs)*base
    is_upstairs = ",".join(is_upstairs)
    type.append(is_upstairs)
    type = ",".join(type)
    res = [{"role":'赢家', "limit": win},
            {"role":'庄家', "limit": zhuang_out},
            {"role":'非庄家', "limit": other_out},
            {"role":'牌型', "limit": type}]
    return res

if __name__ == "__main__":
    # 输入参数
    ## 是否庄家胡牌
    is_zhuang = False
    ## 是否楼上
    is_upstairs = False
    ## 胡牌类型
    hu_type = "明杠,本混龙, 明杠，暗杠， 123 ，楼上，庄"
    hu_type = "本混龙"
    hu_type = "门清,没混，捉五魁，一条龙"
    Mahjong_settle(hu_type)
    hu_type = "门清,没混，捉五魁，一条龙，庄"
    hu_type = ["门清","没混","捉五魁","一条龙","庄"]
    Mahjong_settle(hu_type)

    hu_type = ["门清","没混","捉五魁","一条龙","庄","楼上"]
    Mahjong_settle(hu_type, base = 2)
    hu_type = ["门清","没混","捉五魁","一条龙","庄"]
    Mahjong_settle(hu_type)
    hu_type = ["门清","没混","捉五魁","一条龙"]
    Mahjong_settle(hu_type)
    hu_type = ["门清","没混","捉五魁","一条龙","楼上"]
    Mahjong_settle(hu_type)
