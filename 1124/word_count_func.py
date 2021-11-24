def word_lower(string):
    return string.lower()

def delete_char(string):
    ng_list = '.,:()"[]'
    for c in ng_list:
        string = string.replace(c,' ')
    return string

def word_split(string):
    words = string.split(' ')
    return words

def remove_null(words_list):
    if '' in words_list:
        del words_list['']
    if ' ' in words_list:
        del words_list[' ']
    return words_list

DATA_FILENAME = 'sentence.txt'

word_dic = {}
with open(DATA_FILENAME)as f:
    for line in f:
        line = line.strip()
        line = word_lower(line)
        line = delete_char(line)
        words = word_split(line)
        for word in words:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
        word_dic = remove_null(word_dic)
for word in sorted(word_dic):
    print(f'{word}:{word_dic[word]}')


