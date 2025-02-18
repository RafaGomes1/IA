import math
from Node import Node
from queue import Queue
from math import radians, sin, cos, sqrt, atan2
import heapq

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class EstadoFilaPrioridade:
    def __init__(self, custo, nodo_atual, caminho_atual):
        self.custo = custo
        self.nodo_atual = nodo_atual
        self.caminho_atual = caminho_atual

    def __lt__(self, other):
        return self.custo < other.custo


class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para armazenar as heuristicas para cada nodo -< pesquisa informada

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out


    #############################
    #   encontrar nodo pelo nome
    #############################

    def verification(self, name):
        # search_node = Node(name)
        for node in self.m_nodes:
            if name == node.getName():
                return node
        return None

    
    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + "->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA
    

    def add_node(self,name,latitude,longitude):
       coordinates = (latitude,longitude)
       new_node = Node(name,coordinates)
       self.m_nodes.append(new_node)
       self.m_graph[new_node] = []
    

    ##############################
    #   adicionar aresta no grafo
    ##############################


    def add_edge(self, node1, node2, weight):
        
        n1 = self.verification(node1)
        n2 = self.verification(node2)

        if (n1 == None or n2 == None):
            print(n1.getName())
            print(n2)
            print("Nodos nao encontrados")
            return -1            

        self.m_graph[n1].append((n2, weight))  # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
              self.m_graph[n2].append((n1, weight))


    #################
    # devolver nodos
    #################
    
    def getNodes(self):
        return self.m_nodes
    
    

    ####################################
    #    devolver o custo de uma aresta 
    ####################################

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]

        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT
    

    ##########################
    #    calcular a eurística 
    ##########################

    def calcula_heuristica(self, coord1, coord2):
        # Radius of the Earth in kilometers
        R = 6371.0

        # Convert latitude and longitude from degrees to radians
        lat1, lon1 = map(radians, coord1)
        lat2, lon2 = map(radians, coord2)

        # Differences in coordinates
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine formula
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Distance in kilometers
        distance = R * c

        return distance
    

    ###############################################################################
    #    atribui a heuristica ao grafo após sabermos qual é o grafo inicial e final
    ###############################################################################

    def add_all_heuristica(self, end):
        coord1 = end.getCoordinates()

        for node in self.m_nodes:
            coord2 = node.getCoordinates()
            dist = self.calcula_heuristica(coord2,coord1)
            dist = int(dist)
            self.m_h[node] = []
            self.m_h[node].append(dist)


    #########################################
    #    dado um caminho calcula o seu custo
    #########################################
    
    def calcula_custo(self, caminho):
        aux = caminho
        custo = 0
        i = 0

        while i + 1 < len(aux):
            custo = custo + self.get_arc_cost(aux[i], aux[i+1])
            i = i +1

        return custo
    
    def calcula_heuristica(self, coord1, coord2):

        lat1, lon1 = map(radians, coord1)
        lat2, lon2 = map(radians, coord2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Raio da Terra em quilômetros
        R = 6371.0

        # Distância em quilômetros
        distancia = R * c

        return distancia
    


    ##################
    #     procura DFS
    ##################

    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return (path,round(custoT,1),visited)
        
        for (adjacente,peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente,end,path,visited)
                if resultado is not None:
                    return resultado
        
        path.pop()
        return None


    ##################
    #     procura BFS
    ##################

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node não tem pais
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente,peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        # reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()

            # função que calcula o custo do caminho
            custo = self.calcula_custo(path)
        return (path,round(custo,1),visited)  

    def uniform_cost(self, start, end):
        fila_prioridade = [EstadoFilaPrioridade(0, start, [])]
        visitados = []

        while fila_prioridade:
            estado_atual = heapq.heappop(fila_prioridade)

            custo_atual = estado_atual.custo
            nodo_atual = estado_atual.nodo_atual
            caminho_atual = estado_atual.caminho_atual

            if nodo_atual in visitados:
                continue

            caminho_atual = caminho_atual + [nodo_atual]

            if nodo_atual == end:
                return (caminho_atual, custo_atual, visitados)
            
            visitados.append(nodo_atual)

            for (vizinho, custo) in self.m_graph[nodo_atual]:
                if vizinho not in visitados:
                    novo_custo = custo_atual + custo
                    novo_estado = EstadoFilaPrioridade(novo_custo, vizinho, caminho_atual)
                    heapq.heappush(fila_prioridade, novo_estado)

        return (None,None,None)  

    ######################################
    #    define heuristica para cada nodo 
    ######################################

    def add_heuristica(self, n, estima):
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estima
            

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, custo) in self.m_graph[nodo]:
            lista.append((adjacente, custo))
        return lista
    
    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 10000
        else:
            return self.m_h[nodo][0]
        
    ########
    #    A*
    ########

    def procura_aStar(self, start, end):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}  ##  g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start
        #n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                ##if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):  # heuristica ver.....
                if (n == None) or (g[v] + self.getH(v) < g[n] + self.getH(n)):  # heuristica ver.....
                    n = v
            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, round(self.calcula_custo(reconst_path),1),closed_list)

            # for all neighbors of the current node do
            for (m, weight) in self.getNeighbours(n):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
        

    ###########
    #   Gulosa
    ###########

    def greedy(self, start, end):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontra nodo com a menor heuristica
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, round(self.calcula_custo(reconst_path),1),closed_list)
            # para todos os vizinhos  do nodo corrente
            
            for (m, weight) in self.getNeighbours(n):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n


            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    def lat_lon_to_xy(latitude, longitude):
        # Raio médio da Terra em metros
        R = 6371000.0

        # Longitude central (pode ser ajustada conforme necessário)
        longitude_central = 0

        # Conversão de graus para radianos
        lat_rad = math.radians(latitude)
        lon_rad = math.radians(longitude - longitude_central)

        # Fórmulas da Projeção Mercator
        x = R * lon_rad
        y = R * math.log(math.tan(math.pi/4 + lat_rad/2))

        return (x,y)

    
    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()

        for nodo in lista_v:
            n = nodo.getName()
            coordinates = nodo.getCoordinates()
            cord = Graph.lat_lon_to_xy(coordinates[0],coordinates[1])

            g.add_node(n, pos=cord)

            for (adjacente, peso) in self.m_graph[nodo]:
                g.add_edge(n, adjacente.getName(), weight=peso)

        pos = nx.get_node_attributes(g, 'pos')

        node_labels = {node: node.replace(" ", "\n") for node in g.nodes}

        plt.figure(figsize=(20, 8))

        nx.draw_networkx_nodes(g, pos, node_size=300, node_color='lightblue')
        nx.draw_networkx_edges(g, pos, edgelist=g.edges(), edge_color='black', width=2)
        nx.draw_networkx_labels(g, pos, labels=node_labels, font_size=8, font_weight='bold')

        # edge_labels = {(n1, n2): d['weight'] for n1, n2, d in g.edges(data=True)}
        # nx.draw_networkx_edge_labels(g, pos, font_color='red', font_size=5)

        plt.draw()
        plt.show()

    def desenhaComHeuristica(self, nodofinal):
        ##criar lista de vertices
        lista_v = self.m_nodes

        self.add_all_heuristica(nodofinal)

        g = nx.Graph()

        for nodo in lista_v:
            n = nodo.getName()
            coordinates = nodo.getCoordinates()
            cord = Graph.lat_lon_to_xy(coordinates[0],coordinates[1])

            g.add_node(n, pos=cord, heuristic=self.getH(nodo))

            for (adjacente, peso) in self.m_graph[nodo]:
                g.add_edge(n, adjacente.getName(), weight=peso)

        pos = nx.get_node_attributes(g, 'pos')
        heuristics = nx.get_node_attributes(g, 'heuristic')

        formatted_heuristics = {node: "{}".format(heuristic) if heuristic is not None else "N/A" for node, heuristic in heuristics.items()}

        node_labels = {node: "H: {1}\n {0}".format(node.replace(' ', '\n'), formatted_heuristics[node]) for node in g.nodes}

        plt.figure(figsize=(15, 8))

        nx.draw_networkx(g, pos, with_labels=True, node_size=300 , font_weight='bold', font_size=8 , edge_color='b', labels=node_labels)

        plt.draw()
        plt.show()

    def desenhaCaminho(self,caminho):
        
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()

        for nodo in lista_v:
            n = nodo.getName()
            coordinates = nodo.getCoordinates()
            cord = Graph.lat_lon_to_xy(coordinates[0],coordinates[1])

            g.add_node(n, pos=cord)

            for (adjacente, peso) in self.m_graph[nodo]:
                g.add_edge(n, adjacente.getName(), weight=peso)

        pos = nx.get_node_attributes(g, 'pos')

        node_labels = {node: node.replace(" ", "\n") for node in g.nodes}

        path_edges = [(caminho[i].getName(), caminho[i+1].getName()) for i in range(len(caminho)-1)]

        # Destaca o caminho percorrido mudando a cor das arestas
        edge_colors = ['red' if (u, v) in path_edges or (v, u) in path_edges else 'black' for u, v in g.edges()]

        plt.figure(figsize=(15, 8))

        nx.draw_networkx(g, pos, with_labels=True, node_size=300 , font_weight='bold', font_size=8 , edge_color=edge_colors, labels=node_labels)

        plt.draw()
        plt.show()


    def printPath(self, path):
        nodes = path
        print("Nodes:", [node.getName() for node in nodes])
    
    def desenhaVariosCaminhosAnimacao(self, lista, intervalo=2000):

        plt.ion()

        lista_v = self.m_nodes
        g = nx.Graph()

        for nodo in lista_v:
            n = nodo.getName()
            coordinates = nodo.getCoordinates()
            cord = Graph.lat_lon_to_xy(coordinates[0], coordinates[1])
            g.add_node(n, pos=cord)

            for (adjacente, peso) in self.m_graph[nodo]:
                g.add_edge(n, adjacente.getName(), weight=peso)

        pos = nx.get_node_attributes(g, 'pos')
        node_labels = {node: node.replace(" ", "\n") for node in g.nodes}

        plt.figure(figsize=(15, 8))

        # Destaca o caminho inicial
        nx.draw_networkx_nodes(g, pos, node_size=300, node_color='lightblue')
        nx.draw_networkx_edges(g, pos, edgelist=g.edges(), edge_color='black', width=2)
        nx.draw_networkx_labels(g, pos, labels=node_labels, font_size=8, font_weight='bold')

        cores = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'brown', 'pink', 'gray', 'cyan', 'gold', 'silver', 'violet', 'magenta', 'olive', 'coral']

        plt.draw()

        path_edges = []
        i = 0
        nrEstafetas = 0

        for idEstafeta, lista in lista.items():
            path_edges.append((lista,cores[i],idEstafeta))
            nrEstafetas = nrEstafetas + 1
            i = i+1

        # Encontrar a soma total de elementos em cada tuplo
        somas = [len(tuplo[0]) for tuplo in path_edges]

        # Encontrar o máximo entre as somas
        max_soma = max(somas)

        # Função para converter uma sublista em pares
        def converter_em_pares(tuplo):
            lista, cor, estafeta = tuplo
            pares = []
            i=0

            while i < len(lista) - 1:
                if lista[i + 1] != ';':
                    # Cria uma tupla com os elementos consecutivos
                    par = (lista[i].getName(), lista[i + 1].getName())
                    pares.append(par)
                    i += 1  # Avança dois elementos (pula o ponto e vírgula)
                else:
                    # Adiciona o ponto e vírgula diretamente à lista
                    pares.append(lista[i + 1])
                    i += 2  # Avança dois elementos (pula o ponto e vírgula)
            
            return (pares, cor, estafeta)

        # Aplicar a função a cada sublista de cada tuplo
        path_edges = [converter_em_pares(tuplo) for tuplo in path_edges]

        def update(frame):
            plt.clf()

            current_path = []

            for i in range(nrEstafetas):
                current_path.append((path_edges[i][0][:frame],path_edges[i][1],path_edges[i][2]))
                
            edge_colors = []
                   
            for current_pathT in current_path:
                edge_colors.append([current_pathT[1] if (u, v) in current_pathT[0] or (v, u) in current_pathT[0] else 'black' for u, v in g.edges()])

            # Use a função zip para percorrer as listas simultaneamente
            nova_lista = [next((cor for cor in cores if cor != 'black'), 'black') for cores in zip(*edge_colors)]

            nx.draw_networkx_nodes(g, pos, node_size=300, node_color='lightblue')
            nx.draw_networkx_edges(g, pos, edgelist=g.edges(), edge_color=nova_lista, width=2)
            nx.draw_networkx_labels(g, pos, labels=node_labels, font_size=8, font_weight='bold')

            # Adiciona o ID do estafeta e a cor do caminho no canto superior direito
            for i, current_pathT in enumerate(current_path):
                plt.text(-0.15, 1.10 -0.10*i, f'Estafeta: {current_pathT[2]}\nCor: {current_pathT[1]}', transform=plt.gca().transAxes, fontsize=10,
                     verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

            plt.pause(0.1)

            if frame == max_soma:
                self.adiciona_informacoes_finais(plt.gca(), "Entregas Realizadas")
                self.adiciona_botao_fechar()

        ani = FuncAnimation(plt.gcf(), update, frames=max_soma+1, interval=intervalo, repeat=False)
        
        plt.show(block=True)  # Esperar até que a janela seja fechada
        plt.ioff()  # Desativar o modo de interatividade

    
    def desenhaCaminhoAnimacao(self, caminho,estafeta,preco,veiculo,tempo,algoritmo,intervalo=2000):

        if veiculo == 1:
            veiculo = "Bicicleta"
        elif veiculo == 2:
            veiculo = "Mota"
        else:
            veiculo = "Carro"

        plt.ion()  # Ativar modo de interatividade

        lista_v = self.m_nodes
        g = nx.Graph()

        for nodo in lista_v:
            n = nodo.getName()
            coordinates = nodo.getCoordinates()
            cord = Graph.lat_lon_to_xy(coordinates[0], coordinates[1])
            g.add_node(n, pos=cord)

            for (adjacente, peso) in self.m_graph[nodo]:
                g.add_edge(n, adjacente.getName(), weight=peso)

        pos = nx.get_node_attributes(g, 'pos')
        node_labels = {node: node.replace(" ", "\n") for node in g.nodes}

        # Converte o caminho de strings para pares de nós
        path_edges = [(caminho[i].getName(), caminho[i+1].getName()) for i in range(len(caminho)-1)]

        plt.figure(figsize=(15, 8))

        # Destaca o caminho inicial
        nx.draw_networkx_nodes(g, pos, node_size=300, node_color='lightblue')
        nx.draw_networkx_edges(g, pos, edgelist=g.edges(), edge_color='black', width=2)
        nx.draw_networkx_labels(g, pos, labels=node_labels, font_size=8, font_weight='bold')

        plt.draw()

        def update(frame):
            plt.clf()

            current_path = path_edges[:frame]
            edge_colors = ['red' if (u, v) in current_path or (v, u) in current_path else 'black' for u, v in g.edges()]

            nx.draw_networkx_nodes(g, pos, node_size=300, node_color='lightblue')
            nx.draw_networkx_edges(g, pos, edgelist=g.edges(), edge_color=edge_colors, width=2)
            nx.draw_networkx_labels(g, pos, labels=node_labels, font_size=8, font_weight='bold')

            if frame == len(path_edges):
                self.adiciona_informacoes_finais(plt.gca(), "Entrega Realizada")
                # self.adiciona_informacoes(plt.gca(),f'Estafeta: {estafeta}; Preço: {preco}; Veículo: {veiculo}; Tempo: {round((tempo*60),2)}min; Algoritmo: {algoritmo}')
                self.adiciona_botao_fechar()

            plt.pause(0.1)  # Pausa para permitir a atualização do gráfico

        ani = FuncAnimation(plt.gcf(), update, frames=len(path_edges)+1, interval=intervalo, repeat=False)

        plt.show(block=True)  # Esperar até que a janela seja fechada
        plt.ioff()  # Desativar o modo de interatividade

    def adiciona_botao_fechar(self):
        # Adiciona um botão de fechar no último frame
        ax_button = plt.axes([0.85, 0.02, 0.1, 0.05], frame_on=False)  # Define as coordenadas e tamanho do botão
    
        def on_button_click(event):
            plt.close()
    
        # Adiciona um texto como botão
        button_text = plt.text(ax_button.get_position().x0 - 0.80, ax_button.get_position().y0 + 0.35, 'Fechar',
                           color='black', fontsize=20, bbox=dict(facecolor='lightgray', edgecolor='black'))
        button_text.set_picker(True)  # Torna o texto clicável

        ax_button.figure.canvas.mpl_connect('pick_event', on_button_click)

        # Oculta os números esquisitos
        ax_button.xaxis.set_visible(False)
        ax_button.yaxis.set_visible(False)

    def close_button_callback(self,event):
        plt.close()

    def adiciona_informacoes(self,ax, informacoes, cor='black'):
        ax.text(0.5, -0.05, informacoes, ha='center', va='center', transform=ax.transAxes, fontsize=12, fontweight='bold', color=cor)

    def adiciona_informacoes_finais(self,ax, informacoes):
        # Adicione aqui o código para desenhar as informações adicionais
        ax.text(0.5, 1.05, informacoes, ha='center', va='center', transform=ax.transAxes, fontsize=12, fontweight='bold')










