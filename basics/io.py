try:
    int('6.3')
except Exception as e:
    print(f'An error occurred: {e}')

'''
try:
    print(1//0)
except (TypeError,ValueError) as e:
    print('TypeError Or ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except Exception as e:
    print('Exception:',e)

try:
    int('er')
except TypeError as e:
    print('TypeError:',e)
except ValueError as e:
    print('ValueError:',e)


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
'''