'''
python3 list4.py
整数を入力してください：5
1〜5 までの合計：15
平均：3.0

'''

n=input("整数を入力してください")
sum = 0
average = 0
num = int(n)
count = 0

while count <= num:
    sum += count
    count += 1

print(f"1～{num} までの合計：{sum}")
average = sum / num
print(f"平均：{average}")