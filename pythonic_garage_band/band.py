"""Class object representing a band of musicians"""
class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        Band.instances.append(self)

    # Couldn't figure out how to loop through the list so plugged Band class and test into ChatGPT for solution
    def play_solos(self):
        return [member.play_solo() for member in self.members]

    # method bound to the class and not the instance of the class
    # so it affects the Band class
    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    """
    Super class instantiates a musician
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name == "Joan Jett":
            return f"My name is {self.name} and I play guitar"
        elif self.name == "Sheila E.":
            return f"My name is {self.name} and I play drums"
        elif self.name == "Meshell Ndegeocello":
            return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        if self.name == "Joan Jett":
            return f"Guitarist instance. Name = {self.name}"
        elif self.name == "Sheila E.":
            return f"Drummer instance. Name = {self.name}"
        elif self.name == "Meshell Ndegeocello":
            return f"Bassist instance. Name = {self.name}"


"""Class object representing a guitarist"""
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

"""Class object representing a bassist"""
class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

"""Class object representing a drummer"""
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"