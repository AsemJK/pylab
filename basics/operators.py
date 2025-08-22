#unpacking
datetime = (4,45,10)
hour, minute, second = datetime
print(hour)
print(minute)
print(second)

hour,*others = datetime
print(hour)
print(others)

'''


print('===============')
import fractions
c = [2,3,4]

print(c * 4) #strange
print(fractions.Fraction(1, 3))
print(fractions.Fraction(1, 3) + fractions.Fraction(1, 6))  # Output: 1/2

x = (2, 3, 4)
y= (5, 6, 7)
print(x @ y) # Output: 56

'''