import calendar
year = int(input("年を入力してください"))
month = int(input("月を入力してください"))
day = int(input("日にちを入力してください"))

weekday = calendar.weekday(year, month, day)
weekday = int(weekday)

if weekday == 0:
    print("月曜日です")
if weekday == 1:
    print("火曜日です")
if weekday == 2:
    print("水曜日です")
if weekday == 3:
    print("木曜日です")
if weekday == 4:
    print("金曜日です")
if weekday == 5:
    print("土曜日です")
if weekday == 6:
    print("日曜日です")