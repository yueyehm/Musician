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
    def __init__(self):
        super().__init__(["Bang", "Bong", "Dang"])
    
    def count(self):
        print("1, 2, 3, 4")
        
    def Combust(self):
        print("Spontaneously combust")
        

class Band():
    def __init__(self, musicians):
        for mus in musicians:
            if(type(mus) == Drummer):
                self.drummer = mus
            self.musiciansInBand = musicians
            
    def hire(self, musician):
        self.musiciansInBand.append(musician)
        if(type(musician) == Drummer):
            drummer = musician
        print("Hire musician: {}".format(type(musician)))
        
    def fire(self, musician):
        if musician in self.musiciansInBand:
            self.musiciansInBand.remove(musician)

    def play(self):
        self.drummer.count()
        for musician in self.musiciansInBand:
            musician.solo(4)
    
if __name__ == "__main__":
    john = Guitarist()
    paul = Bassist()
    george = Guitarist()
    ringo = Drummer()
    
    # Create the initial band
    band = Band([john, paul, ringo])
    
    # Hire a new member and let him tune up
    band.hire(george)
    george.tune()
    
    # Now let's play!
    band.play()
    
    # Fire ringo, he's terrible
    band.fire(ringo)
    
    # Try to play again
    band.play()