def odd():
    print("奇数")

def even():
    print("偶数")

def choice_func(number):
    func_dic = {1:odd,0:even}
    func = func_dic[number % 2]
    return func

def choice_func2(number):
    if number % 2 == 0:
        func = even
    else:
        func = odd
    return func

while True:
    num = input("数字を入力してください。(0:終了)")
    if num.isnumeric():
        num = int(num)
    else:
        print("入力が正しくありません")
        continue
    if num == 0:
        break
    choice_func(num)()