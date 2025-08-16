class AsyncManager:
    def __init__(self, value):
        self.value = value

    async def yow(self):
        print(f"Yow! The value is {self.value}")

    async def __aenter__(self):
        print("Entering AsyncManager context")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Exiting AsyncManager context")