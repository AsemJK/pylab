#formula: string[start:end:step]
credit_card = '4526-1234-5678-9012'

# print(credit_card[0:4])
# print(credit_card[5:9])
# print(credit_card[10:14])
# print(credit_card[15:])
# print(credit_card[::])
'''
last_4 = credit_card[-4:]
print(last_4)

reversed = credit_card[::-1]
print(reversed)
'''
#Fromatting

price1 = 12.64
price2 = -56.354
price3 = 1500

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price2:+,.2f}")
print(f"Price 1 is ${price3:+,.2f}")



print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price2:.2f}")
print(f"Price 1 is ${price3:.2f}")

print(f"Price 1 is ${price1:16}")
print(f"Price 1 is ${price2:16}")
print(f"Price 1 is ${price3:16}")

print(f"Price 1 is ${price1:>16}")
print(f"Price 1 is ${price2:>16}")
print(f"Price 1 is ${price3:>16}")

print(f"Price 1 is ${price1:^16}")
print(f"Price 1 is ${price2:^16}")
print(f"Price 1 is ${price3:^16}")
