#getrefcount

#the object has reference counts came from assign new name for same value location right ?

import sys
a = 45

b= a
print(sys.getrefcount(a))
print(sys.getrefcount(b))
