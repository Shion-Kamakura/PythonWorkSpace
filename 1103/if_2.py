while True:
    n = input("好きな文字を入力して下さい：")
    if n == "":
        break
    if n.isalnum():#アルファベットか数字かを判断する
        if n.isnumeric():
            print("数字")
        elif n.isalpha():
            print("アルファベット")
        else:
            print("アルファベットと数字")
    else:
        print("その他")