import asyncio
import sys
from basics.asyncmanager import AsyncManager
from basics.functions import some_func
from maths import add
import math as mt

def main():
    '''Main function to execute the script.
       It prints a greeting message to the console.
    '''
    print("Hello from basics!")
async def make_greeting(name) -> str:
    '''Asynchronous function to create a greeting message.
       It returns a string greeting.
    '''
    return f"{name}: Hello from basics async!"
async def async_main(name) -> None:
    a = await make_greeting(name)
    print(a)

async def main2():
    async with AsyncManager(42) as m:
        await m.yow()

if __name__ == "__main__":
    #a = asyncio.run(async_main('Asem'))
    #a
    #asyncio.run(main)
    some_func(1,200)
    print(add.sum(34,66))
    print(mt.log2(64))
    print(sys.path[5])