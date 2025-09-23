import time
import os

filename = os.path.join(os.path.dirname(__file__), 'data.txt')
#Read
with open(filename,"r") as file:
    data = file.read()
    print(data)

while True:
    '''
    with open(filename,"a") as file:
        file.write(time.ctime() + "\n")
        time.sleep(600) #10 minutes
        file.flush()
        #file.close()
    '''
    #create new file
    new_filename = os.path.join(os.path.dirname(__file__),'tmp', 'data' + str(int(time.time())) + '.txt')
    with open(new_filename,"w") as new_file:
        new_file.write(time.ctime() + "\n")
        new_file.flush()
        time.sleep(500)
        #new_file.close()
   
