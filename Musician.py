class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
        
class Drummer(Musician):
    def __init__(self, sounds):
        super().__init__(["Bang", "Bong", "Dang"])
    
    def count(self):
        print("1, 2, 3, 4")
        
    def Combust(self):
        print("Spontaneously combust")
        

class Band():
    musicians = []
    drummer = ""
    def hire(self, musician):
        musicians.append(musicians)
        if(type(musician) == type(Drummer)):
            drummer = musician
        print("Hire musician: {}".format(type(musician)))
        
    def fire(self, musician):
        if (musician in musicians):
            print("Fire musician: {}".format(type(musician)))
            
    def play(self):
        drummer.count()
        for(musician in musicians):
            musician.solo(4)
    