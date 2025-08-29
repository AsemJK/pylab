import time
import os

filename = os.path.join(os.path.dirname(__file__), 'data.txt')
#Read
with open(filename,"r") as file:
    data = file.read()
    print(data)

while True:
    with open(filename,"a") as file:
        file.write(time.ctime() + "\n")
        if(time.ctime().startswith("21")):
            break
        time.sleep(60)
        file.flush()
        #file.close()
   
