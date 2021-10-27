fruits = ['バナナ','リンゴ','オレンジ']

while True:
    n = input("果物をカタカナで入力してください")
    n = str(n)
    if n == "":
        break
    flg = 0
    count = len(fruits)
    while count > 0:
        if fruits[count - 1] == n:
            print (f"{n}は、知っています！")
            count = 0
            flg = 1
        else :
            count -= 1
        
    if flg == 0:
        print (f"{n}は、知りませんでした。覚えておきます。")
        fruits.append(n)
print ('知っている果物')
print (fruits)