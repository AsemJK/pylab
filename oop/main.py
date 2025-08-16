from stack import Stack

def main():
    '''Main function to execute the script.
       It prints a greeting message to the console.
    '''
    stack = Stack()
    stack.push("Hello")
    stack.push("World")
    stack.print()

if __name__ == "__main__":
    main()