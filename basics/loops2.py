a = [1,2,3,4,5,6,7,8,9,10]
credit_card = "1234-5678-9012-3456"

for i in a:
    print(a[i-1])

for i in credit_card.split('-'):
    print(i)