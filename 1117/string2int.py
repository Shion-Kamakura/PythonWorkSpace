def str2int(s):
    """str2int 文字列を数値に変換した値を返す"""
    if type(s) is str:
        if s.isnumeric():
            return int(s)
        else:
            return 0
    else:
        return s
        
print(str2int('a'))
print(str2int('10'))
print(str2int(100))
