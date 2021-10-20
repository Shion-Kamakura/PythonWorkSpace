'''
> python str_reverse.py
f
e
d
c
b
a

'''

str1 = "abcdef"
idx = -1
while idx >= -len(str1):
    print(str1[idx])
    idx -= 1