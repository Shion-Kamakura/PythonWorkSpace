import random

marks = ('S', 'H', 'C', 'D')

cards=[]
for m in marks:
    for n in range(1,14):
        t = (m,n)
        cards.append(t)

# 5枚選択
select_cards = random.sample(cards,5)
# reverseは降順、昇順を選択する
select_cards.sort(reverse=True, key=lambda x: x[1])

print(select_cards)
