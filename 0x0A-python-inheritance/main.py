class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()
    def play(self):
        print("pampam")

class ElectricGuitar(Guitar):
    def playLouder(self):
        print("pampam".upper())


my_guitar=ElectricGuitar()
my_guitar.playLouder()
print(my_guitar.n_strings)
