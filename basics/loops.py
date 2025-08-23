#continue
i=0
while i<5:
    i+=1
    if i==3:#skip the lines of "make some calculations & print"
        continue
    #make some calculations
    print(i)


s=[(1,2),(3,4)]
for a,b in s:
    print(a,b)

for x,y in enumerate(s):
    print(x,y)