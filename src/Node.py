class Node:
    def __init__(self, name, coordinates: tuple):     #  construtor do nodo....."
        self.m_name = name
        self.m_coordinates = coordinates

    def __str__(self):
        return "Node: {self.m_name}, Coordinates: {self.m_coordinates}"
    
    def getCoordinates(self):
        return self.m_coordinates

    def setCoordinates(self, latitude, longitude):
        self.m_coordinates = (latitude, longitude)

    def getName(self):
        return self.m_name
    
    def setName(self, name):
        self.m_name = name

    def __eq__(self, other):
        if(isinstance(other,Node)):
            return (self.m_name == other.m_name and self.m_coordinates == other.m_coordinates)
        return False
    
    def __hash__(self):
        return hash(self.m_name)