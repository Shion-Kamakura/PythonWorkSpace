wordList = []
while True:
    word = str(input("単語を入力してください："))
    if word == "":
        print("終了します")
        break
    elif word == "LIST":
        print(f"単語リスト：{wordList}")
    else :
        i = 0
        flag = 0
        while i < len(wordList) :
            if word == wordList[i] :
                print("すでに登録済みです")
                flag = 1
                break
            i += 1
        if flag == 0:
            wordList.append(word)
print(f"これまで覚えた単語：{wordList}")


