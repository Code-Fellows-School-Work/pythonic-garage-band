"""Class object representing a musician"""
class Musician:
    def __init__(self):
        pass

"""Class object representing a band of musicians"""
class Band(Musician):
    def __init__(self, name, members):
        self.name = name
        self.members = []

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def play_solos():
        pass

    @classmethod
    def to_list():
        pass

"""Class object representing a guitarist"""
class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"

"""Class object representing a bassist"""
class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "bass"

"""Class object representing a drummer"""
class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"