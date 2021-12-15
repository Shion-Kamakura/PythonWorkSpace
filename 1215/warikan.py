import math
def input_int(message):
    value = input(f'{message}を入力してください:')
    if value.isnumeric():
        value = int(value)
    else:
        value = 0
    return value

def calc_payment(total, num_people):
    pay_people = total / num_people
    pay_people = math.ceil(pay_people / 100) * 100
    pay_coodinator = total - pay_people * (num_people - 1)
    return (pay_people, pay_coodinator)

def output_payment(peoplepay,coodinatorpay,peoplenum):
    return print(f"支払金額:{peoplepay}円({peoplenum - 1}人)"),print(f"幹事金額:{coodinatorpay}円")


total = input_int("支払合計金額")
num_people = input_int("参加者人数")
[pay_people, pay_coodinator] = calc_payment(total, num_people)
output_payment(pay_people,pay_coodinator, num_people)