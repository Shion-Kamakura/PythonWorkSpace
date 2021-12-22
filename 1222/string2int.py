def str2int(s):
    if type(s) is str:
        if s.isnumerric():
            return int(s)
        else:
            return 0
    else:
        return s

print(str2int('a'))
print(str2int('10'))
print(str2int(100))