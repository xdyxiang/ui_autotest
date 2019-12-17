

def get_num(str_num,length):
    print("字符串长为：{0}".format(len(str_num)))
    # 小于等于指定长度，则正常显示
    if len(str_num) <= length:
        result = str_num
    else:
        # 结果：字符串切片，取字符串索引位（0,length)的值
        result = str_num[:length]
        if str_num[length-1] == ".":
            result = str_num[:length-1]
    print(result)

# 维持显示12位
# 12亿 ：1234451116.12345678
# 100万： 1000000.12345678
#
get_num("0.12345678",12)
get_num("100.12345678",12)
get_num("1000.12345678",12)
get_num("1000000.12345678",12)
get_num("1234451116.12345678",12)
get_num("12344511167.12345678",12)
get_num("123445111678.12345678",12)
get_num("1234451116789.12345678",12)
