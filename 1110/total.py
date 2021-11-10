file = 'test.csv'

with open(file, 'r', encoding='utf-8') as f:
    person_data = []    #１要素1人分のデータを入れるリスト
    title = f.readline()    #1行目の読込み
    for line in f:  #残りの行を読込み
        line = line.strip() #行末の改行を取り除く
        person_data.append(line.split(',')) #「,」で分割して格納
    
for data in person_data:    #各人のデータを1人分ずつ処理
    name, scores = data[0], data[1:]    #名前と得点に分ける
    scores = [int(num) for num in scores]   #文字列を数字に変換
    total = sum(scores) #合計を求める
    print(name, total)  #1人分ずつ出力