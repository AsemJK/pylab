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
    def __repr__(self) -> str:
        return super().__repr__() + f' {self.name}'

nimo = Fish()
nimo.breath()

print(repr(nimo))