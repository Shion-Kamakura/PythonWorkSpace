a = int(input("数字を入力：1～3："))
b = int(input("数字を入力：2～6："))
sum = 0
while a <= b:
    sum += a
    a += 1
print(f"{a}から{b}までの合計は{sum}")
