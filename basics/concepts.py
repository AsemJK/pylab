a = 23
n = a.numerator
print(n)  # Output: 23, as 23 is an integer and its numerator
############
a = 23.5
# To get the numerator, you can convert it to a Fraction first
a_int = int(a)
n = a_int.numerator
print(n)  # Output: 47, as 23.5 = 47/2
