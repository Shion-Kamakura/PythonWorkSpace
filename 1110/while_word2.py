import os
DATA_FILENAME = 'word.txt'

if os.path.isfile(DATA_FILENAME): #ファイルがあるか確認
   #ここからファイルを読み込む
    with open(DATA_FILENAME) as f:#開いたファイルを[f]として扱う

       # 単語リストに格納
        words_list = [word.strip() for word in f]
        #strip()の時は空白文字を除去している
        #ファイルがない時
else:
    word_list = []#リストの作成

while True:
    a = input("単語を入力してください：") #aに入力値格納
    if a == "": #入力値が""(空)の場合
        break #breakで抜ける
    if a == 'LIST': #LISTと入力された時の処理
        print('単語リスト：',word_list) #単語が入っているリストを出力
        continue #continueで続ける
    if word_list == a: #入力された値がリストに存在してる場合
        print('既に登録済みです。')
        continue #continueで続ける
    else: #入力された値がリストに存在してない場合
        word_list.append(a) #入力値をリスト(word_list)に繋げている

#終了メッセージ
print('終了します')
print('これまでに覚えた単語：',words_list)

#ファイルに単語リストを書き込む
with open(DATA_FILENAME,'w') as f:
    for word in words_list:
        f.write(f'{word}\n')