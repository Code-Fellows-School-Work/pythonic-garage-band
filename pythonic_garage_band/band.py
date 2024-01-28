"""Class object representing a band of musicians"""
class Band:
    artists = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.artists.append(self)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def play_solos():
        pass

    @classmethod
    def to_list():
        pass

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
        self.name = name

    # def __str__(self):
    #     return f"My name is {self.name} and I play guitar"

    # def __repr__(self):
    #     return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

"""Class object representing a bassist"""
class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"My name is {self.name} and I play bass"
    
    # def __repr__(self):
    #     return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

"""Class object representing a drummer"""
class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"My name is {self.name} and I play drums"
    
    # def __repr__(self):
    #     return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"