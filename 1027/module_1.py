import calendar
year = int(input("年を入力してください"))
month = int(input("月を入力してください"))
kei = calendar.monthrange(year, month)

print(f"{year}年{month}月は{kei[1]}日間あります")
