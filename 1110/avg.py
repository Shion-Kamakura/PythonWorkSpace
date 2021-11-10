file = 'test.csv'
person_data = []

with open(file,'r',encoding='utf-8')as f:
    title = f.readline().strip().split(',')
    for line in f:
        person_data.append(line.strip().split(','))

col = 1
avg = [0] * len(title)
while col < len(title):
    for score in person_data:
        avg[col] += int(score[col])/len(person_data)
    col += 1

print(title[1:])
print(avg[1:])