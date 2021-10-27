
while True:
    n = input("整数を入力してください (終了->0)")
    n = int(n)
    if n == 0:
        break

    if n % 2 == 0:
        print ("偶数です")
    else:
        print ("奇数です")
