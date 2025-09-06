import random
#generate string random
import string

b = random.choice(string.ascii_letters)
print(b)
#generate random string with length 10
c = ''.join(random.choice(string.ascii_letters) for i in range(10))
print(c)
#generate random string with length 10 and only lowercase
d = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
print(d)
