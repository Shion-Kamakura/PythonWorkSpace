import time

cttime = 0.1
ct = 1
sheep = int(input("何匹数えますか？："))
if sheep <= 100:
    while ct < 100:
        if ct == sheep + 1:
            break
        print(f"羊が{ct}匹")
        ct += 1
        time.sleep(cttime)
        cttime += 0.01
else :
    print("100匹以下にしてください")