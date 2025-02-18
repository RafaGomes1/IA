

class Entrega:

    def __init__( self, id, cliente, estafeta, classificacao, preco, veiculo, caminho, distancia, tempoPrevisto, encomenda, algoritmo):
        self.id = id
        self.cliente = cliente
        self.estafeta = estafeta
        self.classificacao = classificacao
        self.preco = preco
        self.veiculo = veiculo
        self.caminho = caminho
        self.distancia = distancia
        self.tempoPrevisto = tempoPrevisto
        self.encomenda = encomenda
        self.algoritmo = algoritmo

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setCliente(self, cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
    
    def setEstafeta(self, estafeta):
        self.estafeta = estafeta
        
    def getEstafeta(self):
        return self.estafeta
    
    def setClassificacao(self, classificacao):
        self.classificacao = classificacao
        
    def getClassificacao(self):
        return self.classificacao
    
    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    
    def setVeiculo(self, veiculo):
        self.veiculo = veiculo
    
    def getVeiculo(self):
        return self.veiculo
    
    def setCaminho(self, caminho):
        self.caminho = caminho

    def getCaminho(self):
        return self.caminho
    
    def setDistancia(self, distancia):
        self.distancia = distancia

    def getDistancia(self):
        return self.distancia
    
    def setTempoPrevisto(self, tempoPrevisto):
        self.tempoPrevisto = tempoPrevisto

    def getTempoPrevisto(self):
        return self.tempoPrevisto
    
    def setEncomenda(self, encomenda):
        self.encomenda = encomenda
        
    def getEncomenda(self):
        return self.encomenda
    
    def setAlgoritmo(self, algoritmo):
        self.algoritmo = algoritmo

    def getAlgoritmo(self):
        return self.algoritmo
    
    def converte_TempoPrevisto(self,tempo):
        horas = int(tempo)

        minutos = int((tempo - horas) * 60)

        segundos = int(((tempo - horas) * 60 - minutos) * 60)

        resultado_formatado = f'{horas}H:{minutos}m:{segundos}s'

        return resultado_formatado
    
    def converte_Veiculo(self,veiculo):
        
        if veiculo == 1:
            return "Bicicleta"
        elif veiculo == 2:
            return "Mota"
        elif veiculo == 3:
            return "Carro"
    
    # TODO Metodo toString
    def __str__(self):
        encomendas = self.getEncomenda()
        caminho = self.getCaminho()
        listaIds = []
        listaCaminho = []

        for enc in encomendas:
            listaIds.append(enc)

        ids = ','.join(map(str, listaIds))

        for freguesia in caminho:
            listaCaminho.append(freguesia.getName())

        return "Id da Entrega: " + str(self.getId()) + "; " + "Id do Cliente: " + str(self.getCliente()) + "; " + "Id do Estafeta: " + str(self.getEstafeta()) + "; " + "Classificação: " + str(self.getClassificacao()) + "; " + "Preço: " + str(self.getPreco()) + "; " + "Veículo: " + str(self.getVeiculo()) + "; " + "Caminho: " + str(listaCaminho) + "; " + "Distância: " + str(self.getDistancia()) + "; " + "Tempo Previsto: " + str(self.getTempoPrevisto()) + "; " + "Id da Encomenda: " + str(ids) + "; " + "Algoritmo: " + str(self.getAlgoritmo())
    
    def strFormat(self):
        encomendas = self.getEncomenda()
        caminho = self.getCaminho()
        listaIds = []
        listaCaminho = []

        for enc in encomendas:
            listaIds.append(enc)

        ids = ','.join(map(str, listaIds))

        for freguesia in caminho:
            listaCaminho.append(freguesia.getName())

        print ("Id da Entrega: " + str(self.getId()) + "; " + "Id do Cliente: " + str(self.getCliente()) + "; " + "Id do Estafeta: " + str(self.getEstafeta()) + "; " + "Classificação: " + str(self.getClassificacao()) + "⭐️ ; " + "Preço: " + str(round(self.getPreco(),2)) + "€ ; " + "Veículo: " + str(self.converte_Veiculo(self.getVeiculo())) + "; " + "Caminho: " + str(listaCaminho) + "; " + "Distância: " + str(round(self.getDistancia(),2)) + "KM ; " + "Tempo Previsto: " + str(self.converte_TempoPrevisto(self.getTempoPrevisto())) + "; " + "Id da Encomenda: " + str(ids) + "; " + "Algoritmo: " + str(self.getAlgoritmo()))
    
    def __eq__(self, other):
        if(isinstance(other,Entrega)):
            return self.id == other.id and self.cliente == other.cliente and self.estafeta == other.estafeta and self.classificacao == other.classificacao and self.preco == other.preco and self.veiculo == other.veiculo and self.caminho == other.caminho and self.tempoPrevisto == other.tempoPrevisto and self.encomenda == other.encomenda and self.algoritmo == other.algoritmo
        return False

    
    # TODO Metodo Equals
    