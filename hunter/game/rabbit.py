import random

class Rabbit:
    def __init__(self):
        self.distance = range(1,1001)
        self.location = random.randint(1,1001)
        print(self.location)

    def get_hint(self):
        pass

    def watch(self,location):
        pass