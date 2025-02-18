
class Cliente:

    def __init__(self, id=None, freguesia=None, nome=None, password=None):
        self.id = id
        self.freguesia = freguesia
        self.nome = nome
        self.password = password

    # def __init__(self, id, freguesia, nome, password):
    #     self.id = id
    #     self.freguesia = freguesia
    #     self.nome = nome
    #     self.password = password

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFreguesia(self, freguesia):
        self.freguesia = freguesia

    def getFreguesia(self):
        return self.freguesia
    
    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def __str__(self):
        return "Id: " + str(self.getId()) + "; " + "Freguesia: " + str(self.getFreguesia()) + "; " + "Nome: " + str(self.getNome()) + "; " + "Password: " + str(self.getPassword())

    def __eq__(self, other):
        if(isinstance(other, Cliente)):
            return self.id == other.id and self.freguesia == other.freguesia and self.nome == other.nome
        return False
    
    

    

            
