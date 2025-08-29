rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
symbol = input("Enter symbol: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()