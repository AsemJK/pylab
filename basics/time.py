import time

#count down

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("blast off!")


#watch

while True:
    print(time.ctime()) #ctime stands for current time
    time.sleep(1)
    if time.ctime().endswith("00:00:00"):
        break


# print(time.time())
# print(time.ctime())

