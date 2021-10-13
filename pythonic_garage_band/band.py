
from abc import abstractclassmethod


class Musician:
    """
    base class to handle common functionality which particular kinds of musicians will inherit.
    """
    def __init__(self,name="",members=[]):
        self.name=name
        self.members=members
    @abstractclassmethod
    def play_solo():
        pass
    @abstractclassmethod
    def __str__(self):
        pass
    @abstractclassmethod
    def __repr__(self):
        pass
    @abstractclassmethod
    def to_list():
        pass

class Guitarist(Musician):
    """
    Class that Inherit from Musician
    """
    def __str__(self):
        """
        return name of membeer
        """
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        """
        return name of membeer
        """
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
        """
        method that returns string.
        """
        return "guitar"
    def play_solo(self):
        """
        Method that asks each member musician to play a solo, in the order they were added to band
        """
        return "face melting guitar solo"
    

class Bassist(Musician):
    """
    Class that Inherit from Musician
    """
    def __str__(self):
        """
        return name of membeer
        """
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        """
        return name of membeer
        """
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        """
        method that returns string.
        """
        return "bass"
    def play_solo(self):
        """
        Method that asks each member musician to play a solo, in the order they were added to band
        """
        return "bom bom buh bom"
    

class Drummer(Musician):
    """
    Class that Inherit from Musician
    """
    def __init__(self,name="",members=[]):
        self.name=name
        self.members=members
    def __str__(self):
        """
        return name of membeer
        """
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        """
        return name of membeer
        """
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        """
        method that returns string.
        """
        return "drums"
    def play_solo(self):
        """
        Method that asks each member musician to play a solo, in the order they were added to band
        """
        return "rattle boom crash"

class Band(Musician):
    """
    Class that Inherit from Musician
    """
    instances=[]
    def __init__(self,name="",members=[]):
        self.name=name
        self.members=members
        Band.instances.append(self)


    def play_solos(self):
        solos=[]
        for i in self.members:
            # print(i,"dsfd")
            solos.append(i.play_solo())
        # print(solos)
        return solos
    
    def __str__(self):
        pass
    def __repr__(self):
        pass
    @classmethod
    def to_list(cls):
        """
        Returns a list of previously created Band instances
        """
        return cls.instances