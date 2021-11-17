def list2int(s):
    """str2int 文字列を数値に変換した値を返す"""
    if type(s) is list:
        for a in range(len(s)):
            if type(s[a]) is str:
                if s[a].isnumeric():
                    s[a] = int(s[a])
                else:
                    s[a] = 0
        return s
    elif type(s) is str:
        if s.isnumeric():
            return int(s)
        else:
            return 0
    else:
        return s
        
print(list2int(['5','ab','100',10,1]))
print(list2int('100'))
print(list2int('xyz'))
