calc = []
kigou = True

while True:
    in_str = input("calc:")
    if in_str == '':
        break
    elif in_str == '=':
        break
    elif kigou == True and in_str.isnumeric():
        calc.append(in_str)
        kigou = False
    elif kigou == False and in_str in ['+', '-', '*', '/']:
        calc.append(in_str)
        kigou = True
    else:
        print("入力が正しくありません")
        continue

formula = ''.join(calc)
print(f'入力した計算式:{formula}\n計算結果:{eval(formula)}')
# eval文字列を式として評価