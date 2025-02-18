class Estafeta:
    def __init__ (self, id, nome, entregas):
        self.nome = nome
        self.id = id
        self.entregas = entregas 

    def setId(self, id):
        self.id = id
    
    def getId (self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome (self):
        return self.nome
    
    def setEntregas(self, entregas):
        self.entregas = entregas

    def getEntregas(self):
        return self.entregas
    
    def __str__(self):
        return "Id: " + str(self.getId()) + "; " + "Nome: " + str(self.getNome())
