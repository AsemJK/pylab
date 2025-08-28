#this is a calculator for investment return

principle = 0
interest_rate = 0
years = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("Principle should be greater than zero")
while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate: "))
    if interest_rate <=0:
        print("Interest Rate should be greater than zero")
while years <= 0:
    years = int(input("Enter the number of years: "))
    if years <=0:
        print("Years should be greater than zero")



balance = principle * (1 + interest_rate/100) ** years

print(f"Interest: ${balance:.2f}")