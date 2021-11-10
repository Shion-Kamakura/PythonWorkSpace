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

# -----------------------------------------------------------------------------------------------
# import os
# DATA_FILENAME = 'word.txt'

# if os.path.isfile(DATA_FILENAME): #ファイルがあるか確認
#    #ここからファイルを読み込む
#     with open(DATA_FILENAME) as f:#開いたファイルを[f]として扱う

#        # 単語リストに格納
#         words_list = [word.strip() for word in f]
#         #strip()の時は空白文字を除去している
#         #ファイルがない時
# else:
#     word_list = []#リストの作成


# 続きを書く



# #終了メッセージ
# print('終了します')
# print('これまでに覚えた単語：',words_list)

# #ファイルに単語リストを書き込む
# with open(DATA_FILENAME,'w') as f:
#     for word in words_list:
#         f.write(f'{word}\n')





