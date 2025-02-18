
class Encomenda:


    def __init__(self, id_cliente , id_encomenda, peso, volume, prazoEntrega, estado):
        self.id_cliente = id_cliente
        self.id_encomenda = id_encomenda
        self.peso = peso
        self.volume = volume
        self.prazoEntrega = prazoEntrega
        self.estado = estado # 1: Por entregar e 0: Entregue

    def setId_Cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def getId_Cliente(self):
        return self.id_cliente
    
    def setId_Encomenda(self, id_encomenda):
        self.id_encomenda = id_encomenda

    def getId_Encomenda(self):
        return self.id_encomenda

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setVolume(self, volume):
        self.volume = volume

    def getVolume(self):
        return self.volume

    def setPrazoEntrega(self, prazo):
        self.prazoEntrega = prazo

    def getPrazoEntrega(self):
        return self.prazoEntrega
    
    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def __str__(self):
        return "Id do Cliente: " + str(self.getId_Cliente()) + "; " + "Id da Encomenda: " + str(self.getId_Encomenda()) + "; " + "Peso: " + str(self.getPeso()) + "; " + "Volume: " + str(self.getVolume()) + "; " + "Prazo de Entrega: " + str(self.getPrazoEntrega()) + "; " + "Estado: " + str(self.getEstado())

    def __eq__(self, other):
        if(isinstance(other,Encomenda)):
            return self.getId_Cliente == other.getId_Cliente and self.getId_Encomenda == other.getId_Encomenda and self.getPeso == other.getPeso and self.getVolume == other.getVolume and self.getPrazoEntrega == other.getPrazoEntrega and self.getEstado == other.getEstado
        return False
    
