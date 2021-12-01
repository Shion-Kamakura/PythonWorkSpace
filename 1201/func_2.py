def tax_included(price, tax=10):
    if tax < 0:
        return None
    else:
        return int(price * (1+tax/100))

print('{}の税込金額は{}円'.format(5000,tax_included(5000)))
print('{}の税込金額は{}円'.format(5000,tax_included(5000,8)))
print('{}の税込金額は{}円'.format(5000,tax_included(5000,-5)))
