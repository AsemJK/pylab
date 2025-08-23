


import os
#read data file
filename = os.path.join(os.path.dirname(__file__), 'data.txt')
with open(filename, 'r') as f:
    try:
        data = f.readlines()
        for line in data:
            print(line)
    except FileNotFoundError:
        print("Error: data.txt file not found")
    except IOError as e:
        if isinstance(e, IOError):
            print(f"Error reading file: {e}")
