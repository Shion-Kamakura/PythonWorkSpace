import os
file = 'word.txt'

with open(file) as f:
    line_num = 1
    for line in f:
        print('{0:04d}:{1}'.format(line_num, line.strip()))
        line_num += 1