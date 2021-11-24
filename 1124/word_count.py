DATA_FILENAME = 'word_list.txt'

word_dic = {}
with open(DATA_FILENAME)as f:
    for word in f:
        word = word.strip() #改行コードを取り除く
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
for word in sorted(word_dic):
    print(f'{word}:{word_dic[word]}')
