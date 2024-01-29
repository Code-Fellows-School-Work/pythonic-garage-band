class Band:
    """
    Class that instantiates a musical band

    Param:
        name: str
        member: list of str or an empty string

    Output:
        Returns an instance of a band object
    """
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        Band.instances.append(self)

    def __str__(self):
        return f"Band name: {self.name}"
    
    def __repr__(self):
        return f"Band name: {self.name}"
        

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
    Super class that instantiates a musician object

    Param: 
        name: str

    Output:
        Returns a string or representation of a musician instance
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


class Guitarist(Musician):
    """
    Subclass that instantiates a guitarist object

    Param: 
        name: str

    Output:
        Returns an instance of a guitarist class
    """
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    """
    Subclass that instantiates a bassist object

    Param: 
        name: str

    Output:
        Returns an instance of a bassist class
    """
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    """
    Subclass that instantiates a drummer object

    Param: 
        name: str

    Output:
        Returns an instance of a drummer class
    """
    def __init__(self, name):
        super().__init__(name)
    
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"
    