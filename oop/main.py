from stack import Stack

def main():
    '''Main function to execute the script.
       It prints a greeting message to the console.
    '''
    stack = Stack()
    stack.push("Hello")
    stack.push("World")    
    print(stack._items)  # Output: ['Hello', 'World']

if __name__ == "__main__":
    main()