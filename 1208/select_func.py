def func1():
    print("Hello")

def func2():
    print('Goodbye')

run_list = {'a':func1, 'b':func2}
while True:
    print("a=>Hello,b=>Goodbye")
    value = str(input("どちらを実行しますか？："))
    if value in run_list.keys():
        run_list[value]()
    elif value == "":
        break
    else :
        print("どちらかを選択してください")
    

    