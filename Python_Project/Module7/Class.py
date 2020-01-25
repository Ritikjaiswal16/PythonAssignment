import random
class Coin:
    def __init__(self):
        self.sideups='Heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideups='Heads'
        else:
            self.sideups='Tails'
    def get_sideup(self):
        return self.sideups
con=Coin()
con.toss()
print(con.get_sideup())

