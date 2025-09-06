class Animal:
    def __init__(self) -> None:
        print('Breathing..')
class Fish(Animal):
    def __init__(self) -> None:
        self.name = 'Nimo'
        print(self.name)
        super().__init__()
    def breath(self) -> None:
        print('Undewater')

nimo = Fish()
nimo.breath()
