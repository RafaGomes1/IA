from Graph import Graph
import os
from Cliente import Cliente
from Estafeta import Estafeta
from Encomenda import Encomenda
from pathlib import Path
from Entrega import Entrega
import random
import ast
import copy


class Sistema:

    def __init__(self, directed=False):
        self.m_Encomendas = {}
        self.m_Estafetas = {}
        self.m_Clientes = {}
        self.m_Entregas = {}
        self.m_EncPendentes = []
        self.m_Veiculos = []

        self.g = Graph()

        self.g.add_node("Pedralva", 41.5599, -8.3209)
        self.g.add_node("Sobreposta", 41.5537, -8.33608)
        self.g.add_node("Espinho", 41.54778, -8.36172)
        self.g.add_node("Este", 41.565278, -8.369444)
        self.g.add_node("Gualtar", 41.565, -8.388611)
        self.g.add_node("Nogueiró", 41.547778, -8.384167)
        self.g.add_node("Adaúfe", 41.584722, -8.4025)
        self.g.add_node("Crespos", 41.604167, -8.358333)
        self.g.add_node("Santa Lucrécia", 41.594167, -8.371389)
        self.g.add_node("Palmeira", 41.594167, -8.429167)
        self.g.add_node("São Vicente", 41.558611, -8.421389)
        self.g.add_node("São Victor", 41.555278, -8.409722)
        self.g.add_node("Nogueira", 41.5375, -8.399167)
        self.g.add_node("Esporões", 41.50878292648335, -8.415012033023572)
        self.g.add_node("Trandeiras", 41.497437453967216, -8.400597331757433)
        self.g.add_node("Merelim São Paio", 41.58735590474532, -8.46548130918199)
        self.g.add_node("Real", 41.558333, -8.443056)
        self.g.add_node("Maximinos", 41.546111, -8.431667)
        self.g.add_node("Ferreiros", 41.536111, -8.440278)
        self.g.add_node("São Lázaro", 41.54479885287533, -8.419475095217068)
        self.g.add_node("Lomar", 41.526389, -8.428889)
        self.g.add_node("Figueiredo", 41.505094, -8.438016)
        self.g.add_node("Frossos", 41.566667, -8.451944)
        self.g.add_node("Lamas", 41.499089, -8.423101)
        self.g.add_node("Escudeiros", 41.477778, -8.428056)
        self.g.add_node("Mire de Tibães", 41.573680581181236, -8.478269547335858)
        self.g.add_node("Padim da Graça", 41.56313645688693, -8.493290378022113)
        self.g.add_node("Cabreiros", 41.541389, -8.491667)
        self.g.add_node("Sequeira", 41.533333, -8.471111)
        self.g.add_node("Celeirós", 41.519120, -8.453169)
        self.g.add_node("Guisande", 41.483333, -8.446389)
        self.g.add_node("Vilaça", 41.517222, -8.475833)
        self.g.add_node("Tadim", 41.506667, -8.49)
        self.g.add_node("Priscos", 41.495278, -8.474444)
        self.g.add_node("Tebosa", 41.483056, -8.483333)
        self.g.add_node("Ruílhe", 41.498889, -8.499722)
        self.g.add_node("Arentim", 41.491667, -8.508333)

        self.g.add_node("Ucha", 41.577647, -8.517062)
        self.g.add_node("Pousa", 41.552222, -8.517778)
        self.g.add_node("Martim", 41.534444, -8.511944)
        self.g.add_node("Bastuço", 41.502778, -8.527778)
        self.g.add_node("Cambeses", 41.48355648413429, -8.53016418709173)
        self.g.add_node("Oliveira", 41.583889, -8.543889)
        self.g.add_node("Lama", 41.566944, -8.532778)
        self.g.add_node("Areias", 41.557222, -8.543889)
        self.g.add_node("Encourados", 41.533333, -8.536667)
        self.g.add_node("Moure", 41.501389, -8.556111)
        self.g.add_node("Carreira", 41.48605106372157, -8.548704031469768)
        self.g.add_node("Alheira", 41.613333, -8.562778)
        self.g.add_node("Roriz", 41.587222, -8.589167)
        self.g.add_node("São Martinho", 41.554722, -8.567222)
        self.g.add_node("Manhente", 41.542792, -8.574567)
        self.g.add_node("Adães", 41.5275, -8.560833)
        self.g.add_node("Airó", 41.516111, -8.562778)
        self.g.add_node("Silveiros", 41.47653437499974, -8.581327175098656)
        self.g.add_node("Viatodos", 41.448611, -8.5575)
        self.g.add_node("Panque", 41.635278, -8.595)
        self.g.add_node("Alvito", 41.600556, -8.591944)
        self.g.add_node("Santa Maria", 41.563056, -8.5775)
        self.g.add_node("Tamel", 41.5525, -8.589722)
        self.g.add_node("Rio Covo", 41.528333, -8.595)
        self.g.add_node("Várzea", 41.515278, -8.583611)
        self.g.add_node("Carvalhas", 41.47190412921908, -8.597082136691196)
        self.g.add_node("Negreiros", 41.441667, -8.608889)
        self.g.add_node("Cossourado", 41.633056, -8.619444)
        self.g.add_node("Aborim", 41.614167, -8.63)
        self.g.add_node("Campo", 41.592222, -8.62)
        self.g.add_node("Lijó", 41.569167, -8.614722)
        self.g.add_node("Arcozelo", 41.548056, -8.602222)
        self.g.add_node("Gamil", 41.51078821479917, -8.59654242493563)
        self.g.add_node("Remelhe", 41.493611, -8.606111)
        self.g.add_node("Chorente", 41.456944, -8.6125)
        self.g.add_node("Macieira", 41.435556, -8.633333)
        self.g.add_node("Balugães", 41.64, -8.641111)
        self.g.add_node("Aguiar", 41.616667, -8.658333)
        self.g.add_node("Carapeços", 41.584444, -8.633056)
        self.g.add_node("Silva", 41.5675, -8.628889)
        self.g.add_node("Abade de Neiva", 41.562778, -8.651111)
        self.g.add_node("Vila Boa", 41.534950229834074, -8.634566340336457)
        self.g.add_node("Barcelinhos", 41.523889, -8.626667)
        self.g.add_node("Alvelos", 41.50509, -8.61931)
        self.g.add_node("Pereira", 41.494722, -8.629722)
        self.g.add_node("Milhazes", 41.490278, -8.66)
        self.g.add_node("Paradela", 41.460833, -8.680556)
        self.g.add_node("Durrães", 41.631944, -8.688889)
        self.g.add_node("Vilar do Monte", 41.58106433152567, -8.664508572768224)
        self.g.add_node("Mariz", 41.527778, -8.671667)
        self.g.add_node("Carvalhal", 41.511389, -8.6325)
        self.g.add_node("Gilmonde", 41.510278, -8.656667)
        self.g.add_node("Fragoso", 41.614722, -8.703889)
        self.g.add_node("Aldreu", 41.609167, -8.717222)
        self.g.add_node("Palme", 41.585278, -8.718333)
        self.g.add_node("Vila Cova", 41.545556, -8.713333)
        self.g.add_node("Perelhal", 41.52891057189228, -8.700656801797612)
        self.g.add_node("Fornelos", 41.515278, -8.675833)
        self.g.add_node("Vila Seca", 41.501111, -8.685556)
        self.g.add_node("Cristelo", 41.478889, -8.6975)
        self.g.add_node("Barqueiros", 41.481111, -8.7175)

        self.g.add_node("Health Planet", 41.59962882679894, -8.520568667381585)

        self.g.add_node("Airão", 41.455644403526506, -8.411203624816395)
        self.g.add_node("Leitões", 41.4770488263364, -8.392157881602694)
        self.g.add_node("Sande (V.N)", 41.481627464280486, -8.367778046928404)
        self.g.add_node("Balazar", 41.506957349579714, -8.377931364480743)
        self.g.add_node("Longos", 41.52230455239758, -8.365032771279475)
        self.g.add_node("Briteiros", 41.52076226425254, -8.328963217526324)
        self.g.add_node("Sande (S.M)", 41.49461508953319, -8.362818334492216)
        self.g.add_node("Brito", 41.457754106724956, -8.363974181368826)
        self.g.add_node("Ronfe", 41.4376815074542, -8.38426727760226)
        self.g.add_node("Donim", 41.52744524740813, -8.306001328390437)
        self.g.add_node("Barco", 41.50488778964789, -8.331946578497448)
        self.g.add_node("Caldelas", 41.49273763050496, -8.346149426004471)
        self.g.add_node("Ponte", 41.47455390019481, -8.336032687156976)
        self.g.add_node("Silvares", 41.44617451887226, -8.338591812461445)
        self.g.add_node("Selho", 41.4335632836304, -8.359211842288818)
        self.g.add_node("Gondar", 41.42094959779907, -8.370557169755513)
        self.g.add_node("Gondomar", 41.51510689324298, -8.286077682557234)
        self.g.add_node("Prazins", 41.49248046762077, -8.319378920827878)
        self.g.add_node("Corvite", 41.48039266049166, -8.313208255933784)
        self.g.add_node("Fermentões", 41.45826870709897, -8.314912874738413)
        self.g.add_node("Creixomil", 41.436472007392204, -8.315107694710967)
        self.g.add_node("Candoso", 41.428621271249746, -8.337062477275655)
        self.g.add_node("Selho (S.C)", 41.41914744264007, -8.349260232906685)
        self.g.add_node("Serzedelo", 41.407045962892816, -8.368484763219072)
        self.g.add_node("Arosa", 41.551857970978894, -8.216759027064048)
        self.g.add_node("Gonça", 41.51407859087549, -8.245932078945806)
        self.g.add_node("São Torcato", 41.49042312779434, -8.26378438710081)
        self.g.add_node("Gominhães", 41.479826993941266, -8.28694762812082)
        self.g.add_node("Pencelo", 41.46889449308026, -8.302223115429065)
        self.g.add_node("Azurém", 41.455952973262036, -8.287464393682104)
        self.g.add_node("São Sebastião", 41.44373646075035, -8.290944648700657)
        self.g.add_node("Urgezes", 41.42918738452431, -8.294338093243981)
        self.g.add_node("Mascotelos", 41.419444, -8.309722)
        self.g.add_node("Nespereira", 41.40725216555967, -8.326417037282958)
        self.g.add_node("Gandarela", 41.3923666753663, -8.335179011991318)
        self.g.add_node("Guardizela", 41.388194263498626, -8.364360080310028)
        self.g.add_node("Rendufe", 41.481421497830254, -8.229804935426387)
        self.g.add_node("Aldão", 41.46454610090053, -8.275474699989813)
        self.g.add_node("Mesão Frio", 41.4469923, -8.2578177)
        self.g.add_node("Costa", 41.4298, -8.2686)
        self.g.add_node("Pinheiro", 41.414444, -8.281667)
        self.g.add_node("Polvoreira", 41.403610, -8.291603)
        self.g.add_node("Moreira de Cónegos", 41.373716, -8.352456)
        self.g.add_node("Lordelo", 41.36995505489182, -8.376376079791665)
        self.g.add_node("Infantas", 41.429174815455475, -8.246611836255946)
        self.g.add_node("Abação", 41.411603895045566, -8.265151294657391)
        self.g.add_node("Tabuadelo", 41.389444, -8.278889)
        self.g.add_node("Serzedo", 41.404213376120275, -8.238719807111169)


        self.g.add_node("Arnoso", 41.471389637049086, -8.490331087487752)
        self.g.add_node("Portela", 41.45337983869392, -8.465322919461732)
        self.g.add_node("Joane", 41.44416597377157, -8.423728135898342)
        self.g.add_node("Mogege", 41.42151477231898, -8.411372792190745)
        self.g.add_node("Pedome", 41.41636566971283, -8.385289288808046)
        self.g.add_node("Oliveira (S.M)", 41.40812625642692, -8.400390264450671)
        self.g.add_node("Riba de Ave", 41.39164429479458, -8.383916472840541)
        self.g.add_node("Nine", 41.46555006573199, -8.539611560306602)
        self.g.add_node("Lemenhe", 41.451371516652785, -8.519825253624052)
        self.g.add_node("Cruz", 41.4431365451774, -8.496487382176381)
        self.g.add_node("Vale", 41.42975248734589, -8.478640774598748)
        self.g.add_node("Vermoim", 41.42563376047157, -8.448438823313516)
        self.g.add_node("Pousada", 41.43181175280221, -8.43608347960592)
        self.g.add_node("Castelões", 41.413276012197805, -8.42647376783335)
        self.g.add_node("Oliveira (S.Mateus)", 41.39885566734136, -8.40999997622324)
        self.g.add_node("Louro", 41.433769402118074, -8.542890109438803)
        self.g.add_node("Gavião", 41.426663466685156, -8.50609709394895)
        self.g.add_node("Requião", 41.410186207721715, -8.481386406533757)
        self.g.add_node("Ruivães", 41.39988579810819, -8.438829111540947)
        self.g.add_node("Delães", 41.38752315127654, -8.411372792190745)
        self.g.add_node("Gondifelos", 41.41605791744914, -8.564171963509983)
        self.g.add_node("Brufe", 41.41374067711141, -8.544951827392683)
        self.g.add_node("Famalicão", 41.401225748461314, -8.532902633924007)
        self.g.add_node("Antas", 41.40194601065764, -8.510215541851483)
        self.g.add_node("Seide", 41.400915912546964, -8.464912614923646)
        self.g.add_node("Bente", 41.38340174652408, -8.444320375410983)
        self.g.add_node("Bairro", 41.37412763071723, -8.430592215735881)
        self.g.add_node("Fradelos", 41.377246320492404, -8.592490746415958)
        self.g.add_node("Vilarinho das Cambas", 41.38546248155431, -8.561009732649357)
        self.g.add_node("Ribeirão", 41.36588286204006, -8.559636916681853)
        self.g.add_node("Lousado", 41.36155474547839, -8.528786561262057)
        self.g.add_node("Esmeriz", 41.378249623229785, -8.511588357818988)
        self.g.add_node("Avidos", 41.38134094618639, -8.488250486371317)
        self.g.add_node("Landim", 41.382371354518625, -8.463539798956122)


        self.g.add_edge("Pedralva", "Sobreposta", 2.1)
        self.g.add_edge("Pedralva", "Este", 6.5)
        self.g.add_edge("Sobreposta", "Este", 5.2)
        self.g.add_edge("Sobreposta", "Espinho", 2.8)
        self.g.add_edge("Este", "Espinho", 4.8)
        self.g.add_edge("Este", "Nogueiró", 2.9)
        self.g.add_edge("Este", "Gualtar", 2.3)
        self.g.add_edge("Este", "Adaúfe", 5.7)
        self.g.add_edge("Este", "Santa Lucrécia", 5.1)
        self.g.add_edge("Este", "Crespos", 7.2)
        self.g.add_edge("Espinho", "Nogueiró", 4.8)
        self.g.add_edge("Nogueiró", "Gualtar", 3.9)
        self.g.add_edge("Gualtar", "Adaúfe", 4.3)
        self.g.add_edge("Adaúfe", "Santa Lucrécia", 3.1)
        self.g.add_edge("Crespos", "Santa Lucrécia", 2.4)
        self.g.add_edge("Nogueiró", "Nogueira", 4.7)
        self.g.add_edge("Nogueiró", "São Victor", 3.1)
        self.g.add_edge("Gualtar", "São Victor", 2.7)
        self.g.add_edge("Adaúfe", "Palmeira", 6.5)
        self.g.add_edge("Adaúfe", "São Vicente", 6.4)
        self.g.add_edge("Adaúfe", "São Victor", 6.4)
        self.g.add_edge("Palmeira", "São Vicente", 7.7)
        self.g.add_edge("Palmeira", "Real", 6.9)
        self.g.add_edge("Palmeira", "Merelim São Paio", 4.5)
        self.g.add_edge("São Vicente", "São Victor", 2.4)
        self.g.add_edge("São Vicente", "Real", 4.0)
        self.g.add_edge("São Vicente", "Maximinos", 4.3)
        self.g.add_edge("São Vicente", "São Lázaro", 4.1)
        self.g.add_edge("São Victor", "São Lázaro", 2.5)
        self.g.add_edge("São Victor", "Nogueira", 3.9)
        self.g.add_edge("Nogueira", "São Lázaro", 5.4)
        self.g.add_edge("Nogueira", "Lomar", 2.9)
        self.g.add_edge("Nogueira", "Esporões", 3.1)
        self.g.add_edge("Real", "Maximinos", 2.2)
        self.g.add_edge("Real", "Ferreiros", 3.5)
        self.g.add_edge("Real", "Sequeira", 7.1)
        self.g.add_edge("Real", "Mire de Tibães", 4.0)
        self.g.add_edge("Real", "Cabreiros", 5.6)
        self.g.add_edge("São Lázaro", "Maximinos", 2.4)
        self.g.add_edge("São Lázaro", "Lomar", 3.3)
        self.g.add_edge("Maximinos", "Lomar", 3.2)
        self.g.add_edge("Maximinos", "Ferreiros", 1.8)
        self.g.add_edge("Lomar", "Esporões", 4.8)
        self.g.add_edge("Lomar", "Ferreiros", 3.7)
        self.g.add_edge("Esporões", "Figueiredo", 2.5)
        self.g.add_edge("Esporões", "Lamas", 3.6)
        self.g.add_edge("Esporões", "Trandeiras", 1.6)
        self.g.add_edge("Trandeiras", "Lamas", 1.8)
        self.g.add_edge("Trandeiras", "Escudeiros", 3.6)
        self.g.add_edge("Merelim São Paio", "Mire de Tibães", 3.3)
        self.g.add_edge("Mire de Tibães", "Padim da Graça", 1.7)
        self.g.add_edge("Mire de Tibães", "Cabreiros", 4.1)
        self.g.add_edge("Padim da Graça","Cabreiros", 5.1)
        self.g.add_edge("Ferreiros","Sequeira", 3.8)
        self.g.add_edge("Ferreiros","Celeirós", 3.5)
        self.g.add_edge("Lamas","Escudeiros", 3.4)
        self.g.add_edge("Lamas","Figueiredo", 1.0)
        self.g.add_edge("Figueiredo","Celeirós", 2.4)
        self.g.add_edge("Figueiredo","Escudeiros", 3.4)
        self.g.add_edge("Sequeira","Cabreiros", 3.6)
        self.g.add_edge("Sequeira","Vilaça", 1.7)
        self.g.add_edge("Sequeira","Celeirós", 3.4)
        self.g.add_edge("Sequeira","Tadim", 2.9)
        self.g.add_edge("Celeirós","Vilaça", 3.1)
        self.g.add_edge("Celeirós","Priscos", 5.3)
        self.g.add_edge("Celeirós","Guisande", 5.2)
        self.g.add_edge("Celeirós","Escudeiros", 5.4)
        self.g.add_edge("Escudeiros","Guisande", 3.5)
        self.g.add_edge("Cabreiros","Tadim", 6.5)
        self.g.add_edge("Tadim","Vilaça", 1.6)
        self.g.add_edge("Tadim","Priscos", 2.7)
        self.g.add_edge("Tadim","Ruílhe", 2.2)
        self.g.add_edge("Vilaça","Priscos", 2.8)
        self.g.add_edge("Priscos","Ruílhe", 2.6)
        self.g.add_edge("Priscos","Tebosa", 3.2)
        self.g.add_edge("Priscos","Guisande", 5.2)
        self.g.add_edge("Guisande","Tebosa", 4.7)
        self.g.add_edge("Tebosa","Ruílhe", 2.2)
        self.g.add_edge("Tebosa","Arentim", 3.7)
        self.g.add_edge("Ruílhe","Arentim", 2.0)
        self.g.add_edge("Real","Frossos", 1.7)
        self.g.add_edge("Frossos","Palmeira", 6.0)
        self.g.add_edge("Frossos","Merelim São Paio", 2.8)

        self.g.add_edge("Ucha", "Padim da Graça", 9.8)
        self.g.add_edge("Pousa", "Padim da Graça", 4.6)
        self.g.add_edge("Cabreiros", "Martim", 2.8)
        self.g.add_edge("Cabreiros", "Bastuço", 6.3)
        self.g.add_edge("Arentim", "Bastuço", 4.1)
        self.g.add_edge("Arentim", "Cambeses", 2.1)

        self.g.add_edge("Ucha", "Pousa", 5.2)
        self.g.add_edge("Martim", "Pousa", 2.5)
        self.g.add_edge("Martim", "Bastuço", 6.0)
        self.g.add_edge("Bastuço", "Cambeses", 3.6)
        self.g.add_edge("Oliveira", "Ucha", 4.4)
        self.g.add_edge("Oliveira", "Lama", 2.5)
        self.g.add_edge("Ucha", "Lama", 2.7)
        self.g.add_edge("Areias", "Lama", 1.1)
        self.g.add_edge("Pousa", "Lama", 3.2)
        self.g.add_edge("Pousa", "Areias", 2.1)
        self.g.add_edge("Areias", "Encourados", 7.1)
        self.g.add_edge("Pousa", "Encourados", 5.0)
        self.g.add_edge("Martim", "Encourados", 2.8)
        self.g.add_edge("Bastuço", "Encourados", 8.8)
        self.g.add_edge("Moure", "Encourados", 7.5)
        self.g.add_edge("Moure", "Bastuço", 3.1)
        self.g.add_edge("Moure", "Carreira", 2.5)
        self.g.add_edge("Cambeses", "Carreira", 2.5)
        self.g.add_edge("Bastuço", "Carreira", 3.6)
        self.g.add_edge("Alheira", "Oliveira", 6.9)
        self.g.add_edge("Alheira", "Roriz", 4.3)
        self.g.add_edge("Roriz", "Oliveira", 11.1)
        self.g.add_edge("São Martinho", "Lama", 3.0)
        self.g.add_edge("São Martinho", "Areias", 2.5)
        self.g.add_edge("São Martinho", "Encourados", 9.6)
        self.g.add_edge("São Martinho", "Manhente", 2.4)
        self.g.add_edge("Encourados", "Manhente", 12)
        self.g.add_edge("Encourados", "Adães", 3.5)
        self.g.add_edge("Airó", "Adães", 1.8)
        self.g.add_edge("Airó", "Encourados", 5)
        self.g.add_edge("Silveiros", "Moure", 5.8)
        self.g.add_edge("Silveiros", "Carreira", 4.1)
        self.g.add_edge("Silveiros", "Viatodos", 2.9)
        self.g.add_edge("Panque", "Alheira", 5.8)
        self.g.add_edge("Panque", "Alvito", 5.5)
        self.g.add_edge("Alheira", "Alvito", 3.6)
        self.g.add_edge("Roriz", "Alvito", 2.4)
        self.g.add_edge("Roriz", "Santa Maria", 4.8)
        self.g.add_edge("São Martinho", "Santa Maria", 2.2)
        self.g.add_edge("Manhente", "Santa Maria", 2.4)
        self.g.add_edge("Tamel", "Santa Maria", 2.4)
        self.g.add_edge("Tamel", "Manhente", 2.1)
        self.g.add_edge("Tamel", "Rio Covo", 5.3)
        self.g.add_edge("Manhente", "Rio Covo", 5.8)
        self.g.add_edge("Adães", "Rio Covo", 3.3)
        self.g.add_edge("Várzea", "Rio Covo", 3.9)
        self.g.add_edge("Várzea", "Adães", 2.0)
        self.g.add_edge("Várzea", "Airó", 3.7)
        self.g.add_edge("Várzea", "Moure", 4.4)
        self.g.add_edge("Várzea", "Silveiros", 8.2)
        self.g.add_edge("Carvalhas", "Silveiros", 3.0)
        self.g.add_edge("Carvalhas", "Negreiros", 7.0)
        self.g.add_edge("Viatodos", "Negreiros", 6.2)
        self.g.add_edge("Cossourado", "Panque", 3.9)
        self.g.add_edge("Cossourado", "Aborim", 2.2)
        self.g.add_edge("Panque", "Aborim", 6.1)
        self.g.add_edge("Alvito", "Aborim", 6.0)
        self.g.add_edge("Campo", "Aborim", 3.1)
        self.g.add_edge("Campo", "Alvito", 3.6)
        self.g.add_edge("Campo", "Lijó", 4.0)
        self.g.add_edge("Roriz", "Lijó", 3.5)
        self.g.add_edge("Santa Maria", "Lijó", 4.7)
        self.g.add_edge("Arcozelo", "Lijó", 4.1)
        self.g.add_edge("Arcozelo", "Tamel", 4.5)
        self.g.add_edge("Gamil", "Rio Covo", 3.9)
        self.g.add_edge("Gamil", "Várzea", 1.6)
        self.g.add_edge("Gamil", "Silveiros", 7.6)
        self.g.add_edge("Gamil", "Remelhe", 7.5)
        self.g.add_edge("Remelhe", "Silveiros", 5.2)
        self.g.add_edge("Remelhe", "Carvalhas", 3.4)
        self.g.add_edge("Remelhe", "Chorente", 4.5)
        self.g.add_edge("Carvalhas", "Chorente", 3.4)
        self.g.add_edge("Negreiros", "Chorente", 3.6)
        self.g.add_edge("Macieira", "Chorente", 5.6)
        self.g.add_edge("Macieira", "Negreiros", 3.7)
        self.g.add_edge("Balugães", "Cossourado", 4.4)
        self.g.add_edge("Balugães", "Aguiar", 5.8)
        self.g.add_edge("Cossourado", "Aguiar", 5.0)
        self.g.add_edge("Aborim", "Aguiar", 3.6)
        self.g.add_edge("Carapeços", "Aguiar", 4.1)
        self.g.add_edge("Carapeços", "Aborim", 2.8)
        self.g.add_edge("Carapeços", "Campo", 5.2)
        self.g.add_edge("Carapeços", "Lijó", 9.2)
        self.g.add_edge("Carapeços", "Silva", 7.6)
        self.g.add_edge("Lijó", "Silva", 2.3)
        self.g.add_edge("Abade de Neiva", "Silva", 3.8)
        self.g.add_edge("Abade de Neiva", "Vila Boa", 2.6)
        self.g.add_edge("Lijó", "Vila Boa", 3.8)
        self.g.add_edge("Arcozelo", "Vila Boa", 2.2)
        self.g.add_edge("Rio Covo", "Vila Boa", 6.8)
        self.g.add_edge("Barcelinhos", "Vila Boa", 6.1)
        self.g.add_edge("Barcelinhos", "Rio Covo", 2.8)
        self.g.add_edge("Barcelinhos", "Gamil", 5.2)
        self.g.add_edge("Barcelinhos", "Alvelos", 2.9)
        self.g.add_edge("Gamil", "Alvelos", 6.6)
        self.g.add_edge("Remelhe", "Alvelos", 2.6)
        self.g.add_edge("Pereira", "Alvelos", 2.5)
        self.g.add_edge("Pereira", "Remelhe", 4.0)
        self.g.add_edge("Pereira", "Chorente", 6.5)
        self.g.add_edge("Pereira", "Milhazes", 6.1)
        self.g.add_edge("Chorente", "Milhazes", 8.2)
        self.g.add_edge("Paradela", "Milhazes", 6.5)
        self.g.add_edge("Paradela", "Chorente", 7.7)
        self.g.add_edge("Durrães", "Aguiar", 3.3)
        self.g.add_edge("Vilar do Monte", "Carapeços", 11)
        self.g.add_edge("Vilar do Monte", "Silva", 6.8)
        self.g.add_edge("Vilar do Monte", "Abade de Neiva", 4.4)
        self.g.add_edge("Vilar do Monte", "Mariz", 4.9)
        self.g.add_edge("Abade de Neiva", "Mariz", 6.5)
        self.g.add_edge("Vila Boa", "Mariz", 7.0)
        self.g.add_edge("Gilmonde", "Mariz", 8.0)
        self.g.add_edge("Gilmonde", "Vila Boa", 8.5)
        self.g.add_edge("Gilmonde", "Barcelinhos", 3.4)
        self.g.add_edge("Gilmonde", "Carvalhal", 2.3)
        self.g.add_edge("Pereira", "Gilmonde", 4.2)
        self.g.add_edge("Milhazes", "Gilmonde", 2.3)
        self.g.add_edge("Carvalhal", "Barcelinhos", 2.6)
        self.g.add_edge("Carvalhal", "Alvelos", 1.9)
        self.g.add_edge("Carvalhal", "Pereira", 2.6)
        self.g.add_edge("Fragoso", "Durrães", 6.9)
        self.g.add_edge("Fragoso", "Aguiar", 10.2)
        self.g.add_edge("Fragoso", "Carapeços", 5.9)
        self.g.add_edge("Fragoso", "Aldreu", 2.5)
        self.g.add_edge("Palme", "Aldreu", 3.0)
        self.g.add_edge("Palme", "Vila Cova", 7.5)
        self.g.add_edge("Vilar do Monte", "Vila Cova", 4.3)
        self.g.add_edge("Mariz", "Vila Cova", 4.7)
        self.g.add_edge("Perelhal", "Vila Cova", 2.2)
        self.g.add_edge("Perelhal", "Mariz", 2.6)
        self.g.add_edge("Perelhal", "Fornelos", 11.2)
        self.g.add_edge("Mariz", "Fornelos", 9.1)
        self.g.add_edge("Gilmonde", "Fornelos", 2.5)
        self.g.add_edge("Vila Seca", "Fornelos", 3.5)
        self.g.add_edge("Vila Seca", "Gilmonde", 3.5)
        self.g.add_edge("Vila Seca", "Milhazes", 2.7)
        self.g.add_edge("Vila Seca", "Cristelo", 3.3)
        self.g.add_edge("Milhazes", "Cristelo", 5.8)
        self.g.add_edge("Paradela", "Cristelo", 2.9)
        self.g.add_edge("Barqueiros", "Cristelo", 3.6)

        self.g.add_edge("Escudeiros","Airão", 3.0)
        self.g.add_edge("Airão","Leitões", 6.0)
        self.g.add_edge("Leitões","Escudeiros", 4.7)
        self.g.add_edge("Leitões","Trandeiras", 4.4)
        self.g.add_edge("Leitões","Sande (V.N)", 5.9)
        self.g.add_edge("Sande (V.N)","Trandeiras", 7.8)
        self.g.add_edge("Sande (V.N)","Balazar", 5.7)
        self.g.add_edge("Balazar","Trandeiras", 3.4)
        self.g.add_edge("Balazar","Esporões", 4.9)
        self.g.add_edge("Balazar","Longos", 2.8)
        self.g.add_edge("Longos","Nogueira", 8.3)
        self.g.add_edge("Longos","Nogueiró", 8.4)
        self.g.add_edge("Longos","Espinho", 8.1)
        self.g.add_edge("Briteiros","Espinho", 9.5)
        self.g.add_edge("Briteiros","Sobreposta", 6.8)
        self.g.add_edge("Briteiros","Pedralva", 8.7)
        self.g.add_edge("Briteiros","Longos", 5.1)
        self.g.add_edge("Briteiros","Balazar", 7.8)
        self.g.add_edge("Sande (S.M)","Balazar", 3.9)
        self.g.add_edge("Sande (S.M)","Sande (V.N)", 2.0)
        self.g.add_edge("Sande (V.N)","Brito", 5.8)
        self.g.add_edge("Brito","Leitões", 5.1)
        self.g.add_edge("Brito","Airão", 7.5)
        self.g.add_edge("Brito","Ronfe", 3.9)
        self.g.add_edge("Ronfe","Airão", 5.2)
        self.g.add_edge("Donim","Pedralva", 8.6)
        self.g.add_edge("Donim","Briteiros", 3.1)
        self.g.add_edge("Donim","Barco", 4.5)
        self.g.add_edge("Barco","Briteiros", 3.5)
        self.g.add_edge("Barco","Balazar", 8.4)
        self.g.add_edge("Barco","Caldelas", 2.4)
        self.g.add_edge("Caldelas","Balazar", 7.1)
        self.g.add_edge("Caldelas","Sande (S.M)", 2.4)
        self.g.add_edge("Caldelas","Sande (V.N)", 3.0)
        self.g.add_edge("Caldelas","Ponte", 2.6)
        self.g.add_edge("Ponte","Sande (V.N)", 3.9)
        self.g.add_edge("Ponte","Brito", 6.2)
        self.g.add_edge("Ponte","Silvares", 0.9)
        self.g.add_edge("Silvares","Brito", 5.8)
        self.g.add_edge("Silvares","Selho", 5.1)
        self.g.add_edge("Selho","Brito", 9.8)
        self.g.add_edge("Selho","Ronfe", 12.5)
        self.g.add_edge("Selho","Gondar", 13.1)
        self.g.add_edge("Gondar","Ronfe", 3.6)
        self.g.add_edge("Gondomar","Donim", 3.2)
        self.g.add_edge("Gondomar","Barco", 7.6)
        self.g.add_edge("Gondomar","Prazins", 7.4)
        self.g.add_edge("Prazins","Barco", 1.8)
        self.g.add_edge("Prazins","Ponte", 2.2)
        self.g.add_edge("Prazins","Corvite", 2.6)
        self.g.add_edge("Corvite","Gondomar", 10.0)
        self.g.add_edge("Corvite","Ponte", 2.2)
        self.g.add_edge("Corvite","Fermentões", 3.6)
        self.g.add_edge("Fermentões","Ponte", 3.9)
        self.g.add_edge("Fermentões","Silvares", 4.8)
        self.g.add_edge("Fermentões","Creixomil", 4.5)
        self.g.add_edge("Creixomil","Silvares", 7.2)
        self.g.add_edge("Candoso","Silvares", 7.6)
        self.g.add_edge("Candoso","Selho", 3.5)
        self.g.add_edge("Candoso","Selho (S.C)", 2.1)
        self.g.add_edge("Selho (S.C)","Selho", 3.0)
        self.g.add_edge("Selho (S.C)","Gondar", 3.5)
        self.g.add_edge("Selho (S.C)","Serzedelo", 4.6)
        self.g.add_edge("Serzedelo","Gondar", 3.5)
        self.g.add_edge("Arosa","Gonça", 8.9)
        self.g.add_edge("Gonça","Gondomar", 6.3)
        self.g.add_edge("Gonça","São Torcato", 4.1)
        self.g.add_edge("São Torcato","Gondomar", 10.3)
        self.g.add_edge("São Torcato","Gominhães", 3.0)
        self.g.add_edge("Gominhães","Gondomar", 9.2)
        self.g.add_edge("Gominhães","Corvite", 5.7)
        self.g.add_edge("Gominhães","Pencelo", 3.3)
        self.g.add_edge("Pencelo","Corvite", 3.9)
        self.g.add_edge("Pencelo","Fermentões", 2.3)
        self.g.add_edge("Pencelo","Azurém", 2.1)
        self.g.add_edge("Azurém","Gominhães", 4.3)
        self.g.add_edge("Azurém","Fermentões", 2.5)
        self.g.add_edge("Azurém","São Sebastião", 3.0)
        self.g.add_edge("São Sebastião","Fermentões", 5.4)
        self.g.add_edge("São Sebastião","Creixomil", 2.2)
        self.g.add_edge("São Sebastião","Urgezes", 2.2)
        self.g.add_edge("Urgezes","Creixomil", 1.9)
        self.g.add_edge("Urgezes","Mascotelos", 3.4)
        self.g.add_edge("Mascotelos","Creixomil", 1.6)
        self.g.add_edge("Mascotelos","Candoso", 3.3)
        self.g.add_edge("Mascotelos","Nespereira", 3.6)
        self.g.add_edge("Nespereira","Candoso", 3.5)
        self.g.add_edge("Nespereira","Selho (S.C)", 5.6)
        self.g.add_edge("Nespereira","Gandarela", 3.1)
        self.g.add_edge("Gandarela","Serzedelo", 2.3)
        self.g.add_edge("Gandarela","Guardizela", 3.1)
        self.g.add_edge("Guardizela","Serzedelo", 3.0)
        self.g.add_edge("Rendufe","Gonça", 7.7)
        self.g.add_edge("Rendufe","São Torcato", 3.9)
        self.g.add_edge("Rendufe","Aldão", 5.3)
        self.g.add_edge("Rendufe","Mesão Frio", 6.7)
        self.g.add_edge("Aldão","São Torcato", 3.9)
        self.g.add_edge("Aldão","Gominhães", 3.6)
        self.g.add_edge("Aldão","Azurém", 3.2)
        self.g.add_edge("Aldão","Mesão Frio", 2.0)
        self.g.add_edge("Mesão Frio","Azurém", 3.4)
        self.g.add_edge("Mesão Frio","Costa", 3.5)
        self.g.add_edge("Costa","Azurém", 3.5)
        self.g.add_edge("Costa","São Sebastião", 2.4)
        self.g.add_edge("Costa","Urgezes", 3.3)
        self.g.add_edge("Costa","Pinheiro", 4.1)#1
        self.g.add_edge("Pinheiro","Urgezes", 2.5)
        self.g.add_edge("Pinheiro","Polvoreira", 3.4)
        self.g.add_edge("Polvoreira","Mascotelos", 3.1)
        self.g.add_edge("Polvoreira","Nespereira", 3.6)
        self.g.add_edge("Moreira de Cónegos","Gandarela", 3.0)
        self.g.add_edge("Moreira de Cónegos","Guardizela", 3.9)
        self.g.add_edge("Moreira de Cónegos","Lordelo", 5.7)
        self.g.add_edge("Lordelo","Guardizela", 2.5)
        self.g.add_edge("Infantas","Mesão Frio", 4.5)
        self.g.add_edge("Infantas","Costa", 8.1)
        self.g.add_edge("Infantas","Abação", 5.1)
        self.g.add_edge("Infantas","Serzedo", 2.6)
        self.g.add_edge("Abação","Costa", 6.4)
        self.g.add_edge("Abação","Pinheiro", 2.7)
        self.g.add_edge("Abação","Tabuadelo", 3.1)
        self.g.add_edge("Abação","Serzedo", 4.4)
        self.g.add_edge("Tabuadelo","Polvoreira", 2.9)

        self.g.add_edge("Arnoso","Cambeses", 4.0)
        self.g.add_edge("Arnoso","Arentim", 4.1)
        self.g.add_edge("Arnoso","Tebosa", 3.9)
        self.g.add_edge("Arnoso","Guisande", 7.8)
        self.g.add_edge("Arnoso","Portela", 10.5)
        self.g.add_edge("Portela","Guisande", 3.3)
        self.g.add_edge("Portela","Escudeiros", 3.3)
        self.g.add_edge("Portela","Airão", 4.1)
        self.g.add_edge("Portela","Joane", 7.0)
        self.g.add_edge("Joane","Airão", 3.0)
        self.g.add_edge("Joane","Ronfe", 3.0)
        self.g.add_edge("Joane","Mogege", 2.4)
        self.g.add_edge("Mogege","Pedome", 3.6)
        self.g.add_edge("Mogege","Oliveira (S.M)", 4.3)
        self.g.add_edge("Pedome","Gondar", 2.4)
        self.g.add_edge("Pedome","Serzedelo", 5.2)
        self.g.add_edge("Pedome","Oliveira (S.M)", 1.7)
        self.g.add_edge("Oliveira (S.M)","Serzedelo", 4.4)
        self.g.add_edge("Oliveira (S.M)","Riba de Ave", 3.9)
        self.g.add_edge("Riba de Ave","Serzedelo", 4.6)
        self.g.add_edge("Riba de Ave","Guardizela", 2.7)
        self.g.add_edge("Riba de Ave","Lordelo", 2.1)
        self.g.add_edge("Nine","Silveiros", 4.9)
        self.g.add_edge("Nine","Carreira", 4.3)
        self.g.add_edge("Nine","Cambeses", 3.6)
        self.g.add_edge("Nine","Arnoso", 4.9)
        self.g.add_edge("Nine","Lemenhe", 2.2)
        self.g.add_edge("Lemenhe","Viatodos", 2.5)
        self.g.add_edge("Lemenhe","Arnoso", 3.3)
        self.g.add_edge("Lemenhe","Cruz", 6.1)
        self.g.add_edge("Cruz","Portela", 7.6)
        self.g.add_edge("Cruz","Vale", 3.6)
        self.g.add_edge("Vale","Portela", 7.6)
        self.g.add_edge("Vale","Vermoim", 5.6)
        self.g.add_edge("Vermoim","Portela", 10.5)
        self.g.add_edge("Vermoim","Pousada", 2.3)
        self.g.add_edge("Vermoim","Castelões", 3.1)
        self.g.add_edge("Pousada","Joane", 3.2)
        self.g.add_edge("Pousada","Mogege", 2.7)
        self.g.add_edge("Castelões","Pousada", 2.4)
        self.g.add_edge("Castelões","Mogege", 3.1)
        self.g.add_edge("Castelões","Oliveira (S.M)", 3.1)
        self.g.add_edge("Castelões","Oliveira (S.Mateus)", 4.3)
        self.g.add_edge("Oliveira (S.Mateus)","Oliveira (S.M)", 2.6)
        self.g.add_edge("Oliveira (S.Mateus)","Riba de Ave", 3.2)
        self.g.add_edge("Louro","Viatodos", 2.6)
        self.g.add_edge("Louro","Lemenhe", 3.2)
        self.g.add_edge("Gavião","Lemenhe", 5.2)
        self.g.add_edge("Gavião","Cruz", 2.2)
        self.g.add_edge("Gavião","Vale", 3.5)
        self.g.add_edge("Gavião","Requião", 5.6)
        self.g.add_edge("Requião","Vale", 3.1)
        self.g.add_edge("Requião","Vermoim", 4.2)
        self.g.add_edge("Ruivães","Vermoim", 4.1)
        self.g.add_edge("Ruivães","Castelões", 2.4)
        self.g.add_edge("Ruivães","Oliveira (S.Mateus)", 3.8)
        self.g.add_edge("Ruivães","Delães", 3.8)
        self.g.add_edge("Delães","Oliveira (S.Mateus)", 1.4)
        self.g.add_edge("Gondifelos","Viatodos", 6.9)
        self.g.add_edge("Gondifelos","Negreiros", 2.4)
        self.g.add_edge("Gondifelos","Louro", 7.8)
        self.g.add_edge("Gondifelos","Brufe", 7.5)
        self.g.add_edge("Brufe","Louro", 3.4)
        self.g.add_edge("Brufe","Famalicão", 3.8)
        self.g.add_edge("Famalicão","Louro", 5.6)
        self.g.add_edge("Famalicão","Lemenhe", 6.8)
        self.g.add_edge("Famalicão","Gavião", 3.2)
        self.g.add_edge("Famalicão","Antas", 1.9)
        self.g.add_edge("Antas","Gavião", 5.0)
        self.g.add_edge("Antas","Requião", 5.0)
        self.g.add_edge("Seide","Requião", 4.0)
        self.g.add_edge("Bente","Ruivães", 1.9)
        self.g.add_edge("Bente","Delães", 4.2)
        self.g.add_edge("Bente","Bairro", 3.7)
        self.g.add_edge("Bairro","Delães", 2.2)
        self.g.add_edge("Fradelos","Gondifelos", 10.2)
        self.g.add_edge("Fradelos","Vilarinho das Cambas", 7.6)
        self.g.add_edge("Fradelos","Ribeirão", 3.8)
        self.g.add_edge("Vilarinho das Cambas","Gondifelos", 8.8)
        self.g.add_edge("Vilarinho das Cambas","Famalicão", 6.8)
        self.g.add_edge("Vilarinho das Cambas","Ribeirão", 5.6)
        self.g.add_edge("Ribeirão","Lousado", 5.1)
        self.g.add_edge("Lousado","Famalicão", 10.6)
        self.g.add_edge("Lousado","Esmeriz", 4.2)
        self.g.add_edge("Esmeriz","Famalicão", 5.5)
        self.g.add_edge("Esmeriz","Antas", 2.6)
        self.g.add_edge("Esmeriz","Avidos", 3.7)
        self.g.add_edge("Avidos","Antas", 4.8)
        self.g.add_edge("Avidos","Seide", 3.2)
        self.g.add_edge("Avidos","Landim", 1.3)
        self.g.add_edge("Landim","Seide", 2.7)
        self.g.add_edge("Landim","Ruivães", 4.5)
        self.g.add_edge("Landim","Bente", 2.6)

        self.g.add_edge("Health Planet","Ucha", 3.8)
        self.g.add_edge("Health Planet","Oliveira", 3.3)
        self.g.add_edge("Health Planet","Merelim São Paio", 8.6)

        diretorio_atual = os.getcwd()


        nome_pasta_Dataset = 'Dataset'
        nome_pasta_Encomendas = 'Encomendas'
        nome_pasta_Clientes = 'Clientes'
        nome_pasta_Entregas = 'Entregas'
        nome_pasta_Estafetas = 'Estafetas'
        nome_pasta_Veiculos = 'Veiculos'

        pasta_dataset = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta_Dataset)))

        pasta_anterior_Encomendas = Path((os.path.join(pasta_dataset, nome_pasta_Encomendas)))
        pasta_anterior_Clientes = Path((os.path.join(pasta_dataset, nome_pasta_Clientes)))
        pasta_anterior_Entregas = Path((os.path.join(pasta_dataset, nome_pasta_Entregas)))
        pasta_anterior_Estafetas = Path((os.path.join(pasta_dataset, nome_pasta_Estafetas)))
        pasta_anterior_Veiculos = Path((os.path.join(pasta_dataset, nome_pasta_Veiculos)))

        if not pasta_dataset.exists():
            pasta_dataset.mkdir()

        if not pasta_anterior_Encomendas.exists():
            pasta_anterior_Encomendas.mkdir()

        if not pasta_anterior_Clientes.exists():
            pasta_anterior_Clientes.mkdir()

        if not pasta_anterior_Entregas.exists():
            pasta_anterior_Entregas.mkdir()

        if not pasta_anterior_Estafetas.exists():
            pasta_anterior_Estafetas.mkdir()

        if not pasta_anterior_Veiculos.exists():
            pasta_anterior_Veiculos.mkdir()

        # Crie um caminho para o novo arquivo na pasta anterior
        self.caminho_arquivo_Encomendas = os.path.join(pasta_anterior_Encomendas, 'Encomendas.txt')
        self.caminho_arquivo_Encomendas_Pendentes = os.path.join(pasta_anterior_Encomendas, 'Encomendas_Pendentes.txt')
        self.caminho_arquivo_Clientes = os.path.join(pasta_anterior_Clientes, 'Clientes.txt')
        self.caminho_arquivo_Entregas = os.path.join(pasta_anterior_Entregas, 'Entregas.txt')
        self.caminho_arquivo_Estafetas = os.path.join(pasta_anterior_Estafetas, 'Estafetas.txt')
        self.caminho_arquivo_Veiculos = os.path.join(pasta_anterior_Veiculos, 'Veiculos.txt')

        file = open(self.caminho_arquivo_Clientes, 'a+')
        file1 = open(self.caminho_arquivo_Estafetas, 'a+')
        file2 = open(self.caminho_arquivo_Encomendas, 'a+')
        file3 = open(self.caminho_arquivo_Encomendas_Pendentes, 'a+')
        file4 = open(self.caminho_arquivo_Veiculos, 'a+')
        file5 = open(self.caminho_arquivo_Entregas, 'a+')

        self.carrega_Clientes(self.caminho_arquivo_Clientes)

        self.carrega_Estafetas(self.caminho_arquivo_Estafetas)

        self.carrega_Encomendas(self.caminho_arquivo_Encomendas)

        self.carrega_Encomendas_Pendentes(self.caminho_arquivo_Encomendas_Pendentes)

        self.carrega_Veiculos(self.caminho_arquivo_Veiculos)

        self.carrega_Entregas(self.caminho_arquivo_Entregas,self.g)



    def add_Encomenda(self, encomenda):
        if (encomenda == None):
            print("Erro: Encomenda Invalido")
            return -1
        
        if encomenda.getId_Cliente() in self.m_Clientes.keys(): # caso exista um cliente no sistema caso contrario nao faz sentido adicionar
            if encomenda.getId_Cliente() in self.m_Encomendas.keys():
                self.m_Encomendas[encomenda.getId_Cliente()].append(encomenda)
            else:
                self.m_Encomendas[encomenda.getId_Cliente()] = [encomenda]
        else:
            print(encomenda)
            print("Erro: Encomenda Invalida, nao existe Cliente")


    def add_Cliente(self, cliente):

        if (cliente == None):
            print("Erro: Cliente Invalido")
            return -1
        
        if cliente.getId() not in self.m_Clientes:
            self.m_Clientes[cliente.getId()] = cliente
        else:
            print("Ja existe Cliente")

    def cliente_Exists(self, id):
        if id in self.m_Clientes.keys():
            return True
        else: return False

    def verify_Password(self, id, password):
        if (password == self.m_Clientes[id].getPassword()):
            return True
        else: return False

    def estafeta_Exists(self, id):
        if id in self.m_Estafetas.keys():
            return True
        else: return False


    
    def add_Estafeta(self, estafeta):
        if (estafeta == None):
            print("Erro: Estafeta Invalido")
            return -1
        
        if estafeta.getId() not in self.m_Estafetas:
            self.m_Estafetas[estafeta.getId()] = estafeta
        else:
            print("Ja existe Estafeta")

    def possivel_Carro(self,idCliente,peso,prazo):

        freguesia = self.m_Clientes[idCliente].getFreguesia()
        start = "Health Planet"

        caminho = self.escolheCaminho(start,freguesia)

        tempo = self.carroCusto(caminho[1],peso)

        if tempo <= prazo:
            return True
        else:
            return False


    def createEncomenda(self, id_Cliente):

        while True:
            try:

                peso = float(input("Introduza o peso da sua encomenda em KG: "))

                if 0 < peso <= 100:
                    break
                else:
                    raise SystemError("Peso da encomenda tem de ser entre 0.1 e 100 KG!")

            except SystemError as e:
                print(e)
                print('\n')
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
                print('\n')

        while True:
            try:

                volume = float(input("Introduza o volume da sua encomenda em Litros: "))

                if 0 < volume <= 150:
                    break
                else:
                    raise SystemError("Volume da encomenda tem de ser entre 0.1 e 150 Litros!")
                
            except SystemError as e:
                print(e)
                print('\n')
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
                print('\n')

        while True:
            try:

                prazo = float(input("Introduza o prazo de entrega da encomenda em horas: "))

                if prazo > 0:
                    if self.possivel_Carro(id_Cliente,peso,prazo): 
                        break

                    else:
                        raise SystemError("Impossivel entregar a encomenda com esse prazo estipulado, tente outro prazo!")
                
                else:
                    raise SystemError("Prazo da encomenda deve ser superior a 0!") 
                
            except SystemError as e:
                print(e)
                print('\n')
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
                print('\n')

        file = open(self.caminho_arquivo_Encomendas, 'a+')

        file.seek(0)

        id = (len(file.readlines())) + 1

        encomenda = Encomenda(id_Cliente, id, peso, volume, prazo, estado=1)
        self.add_Encomenda(encomenda)

        file.write(str(encomenda) + "\n")
        print("Encomenda criada com sucesso!")

    def create_Account(self, id, freguesia, nome, password):

        if(self.cliente_Exists(id)):
            return False

        file = open(self.caminho_arquivo_Clientes, 'a+')

        cliente = Cliente(id,freguesia,nome,password)
        self.add_Cliente(cliente)
        
        file.write(str(cliente) + "\n")
        print("Criado com sucesso!")

        return True
    
    def create_Estafeta(self, id, nome):

        if(self.estafeta_Exists(id)):
            return False

        diretorio_atual = os.getcwd()

        nome_pasta = 'Estafetas'

        pasta_anterior = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta)))

        caminho_novo_arquivo = os.path.join(pasta_anterior, 'Estafetas.txt')

        file = open(caminho_novo_arquivo, 'a+')

        estafeta = Estafeta(id,nome,[])
        self.add_Estafeta(estafeta)
        
        file.write(str(estafeta) + "\n")
        print("Criado com sucesso!")

        return True
    
    def create_Veiculo(self, veiculo):
        if(veiculo != 1 and veiculo != 2 and veiculo != 3):
            return False

        file = open(self.caminho_arquivo_Veiculos, 'a+')

        self.m_Veiculos.append(veiculo)

        if veiculo == 1:
            s = "Bicicleta"
        elif veiculo == 2:
            s = "Mota"
        else:
            s = "Carro"

        file.write(s + "\n")
        print("Criado com sucesso!")

        return True


    def autentication(self, id, password):

        if(self.cliente_Exists(id)):
            if(self.verify_Password(id, password)):
                return True
        else: return False

    def viewProfile(self,id):
        cliente = self.m_Clientes[id]

        print("ID -> " + str(cliente.getId()))
        print("Nome -> " + str(cliente.getNome()))
        print("Freguesia -> " + str(cliente.getFreguesia()) + "\n")

    def carrega_Clientes(self, caminho):
        file = open(caminho, 'r')

        lista_Clientes = file.readlines()

        for linha in lista_Clientes:
            separado =linha.split(";")
            listaId = separado[0].split("Id: ")
            id = listaId[1]
            listaFreguesia = separado[1].split("Freguesia: ")
            freguesia = listaFreguesia[1]
            listaNome = separado[2].split("Nome: ")
            nome = listaNome[1]
            listaPassword = separado[3].split("Password: ")
            listaPassword2 = listaPassword[1].split("\n")
            password = listaPassword2[0]
            cliente = Cliente(id,freguesia,nome,password)
            
            self.add_Cliente(cliente)


    def carrega_Estafetas(self, caminho):
        file = open(caminho, 'r')

        lista_Estafetas = file.readlines()

        for linha in lista_Estafetas:
            separado =linha.split(";")
            listaId = separado[0].split("Id: ")
            id = listaId[1]
            listaNome = separado[1].split("Nome: ")
            nome = listaNome[1]
            estafeta = Estafeta(id,nome,[])
            
            self.add_Estafeta(estafeta)
    
    def carrega_Encomendas(self, caminho):

        file = open(caminho, 'r')

        lista_Encomendas = file.readlines()

        for linha in lista_Encomendas:
            separado = linha.split(";")
            listaId = separado[0].split("Id do Cliente: ")
            idCliente = listaId[1]
            listaIdEncomenda = separado[1].split(" Id da Encomenda: ")
            idEncomenda = int(listaIdEncomenda[1])
            listaPeso = separado[2].split(" Peso: ")
            peso = float(listaPeso[1])
            listaVolume = separado[3].split(" Volume: ")
            volume = float(listaVolume[1])
            listaPrazo = separado[4].split(" Prazo de Entrega: ")
            prazo = float(listaPrazo[1])
            listaEstado = separado[5].split(" Estado: ")
            estado = int(listaEstado[1])

            encomenda = Encomenda(idCliente,idEncomenda,peso,volume,prazo,estado)
            self.add_Encomenda(encomenda)

    def carrega_Encomendas_Pendentes(self,caminho):

        file = open(caminho, 'r')

        lista_Encomendas_Pendentes = file.readlines()

        for linha in lista_Encomendas_Pendentes:
            separado = linha.split(";")
            listaId = separado[0].split("Id do Cliente: ")
            idCliente = listaId[1]
            listaIdEncomenda = separado[1].split(" Id da Encomenda: ")
            idEncomenda = int(listaIdEncomenda[1])
            listaPeso = separado[2].split(" Peso: ")
            peso = float(listaPeso[1])
            listaVolume = separado[3].split(" Volume: ")
            volume = float(listaVolume[1])
            listaPrazo = separado[4].split(" Prazo de Entrega: ")
            prazo = float(listaPrazo[1])
            listaEstado = separado[5].split(" Estado: ")
            estado = int(listaEstado[1])

            encomenda = Encomenda(idCliente,idEncomenda,peso,volume,prazo,estado)
            self.m_EncPendentes.append(encomenda)




    def carrega_Veiculos(self, caminho):

        file = open(caminho, 'r')

        lista_Veiculos = file.readlines()

        for linha in lista_Veiculos:
            veiculo = linha.strip()

            if veiculo == "Bicicleta":
                self.m_Veiculos.append(1)
            elif veiculo == "Mota":
                self.m_Veiculos.append(2)
            elif veiculo == "Carro":
                self.m_Veiculos.append(3)


    def carrega_Entregas(self, caminho, g):

        file = open(caminho, 'r')

        lista_Entregas = file.readlines()

        for linha in lista_Entregas:

            listaEncomendas = []

            caminho = []

            separado = linha.split(';')
            listaId = separado[0].split("Id da Entrega: ")
            idEntrega = int(listaId[1])
            listaIdCliente = separado[1].split("Id do Cliente: ")
            idCliente = listaIdCliente[1]
            listaIdEstafeta = separado[2].split("Id do Estafeta: ")
            idEstafeta = listaIdEstafeta[1]
            listaClassificacao = separado[3].split("Classificação: ")
            classificacao = listaClassificacao[1]
            listaPreco = separado[4].split("Preço: ")
            preco = float(listaPreco[1])
            listaVeiculo = separado[5].split("Veículo: ")
            veiculo = int(listaVeiculo[1])
            listaCaminho = separado[6].split("Caminho: ")
            caminhoString = listaCaminho[1]
            caminhoAux = ast.literal_eval(caminhoString)

            for freguesia in caminhoAux:
                caminho.append(g.verification(freguesia))

            listaDistancia = separado[7].split("Distância: ")
            distancia = float(listaDistancia[1])
            listaTempo = separado[8].split("Tempo Previsto: ")
            tempo = float(listaTempo[1])
            listaIdEncomendas = separado[9].split("Id da Encomenda: ")
            ids = listaIdEncomendas[1]
            id = ids.split(",")

            for i in id:
                for encomenda in self.m_Encomendas[idCliente]:
                    if int(encomenda.getId_Encomenda()) == int(i):
                        listaEncomendas.append(encomenda.getId_Encomenda())

            listaAlgoritmos = separado[10].split("Algoritmo: ")
            algoritmoAux = listaAlgoritmos[1].split("\n")
            algoritmo = algoritmoAux[0]
            
            entrega = Entrega(idEntrega,idCliente,idEstafeta,classificacao,preco,veiculo,caminho,distancia,tempo,listaEncomendas,algoritmo)

            if idCliente not in self.m_Entregas.keys():
                self.m_Entregas[idCliente] = []

            self.m_Entregas[idCliente].append(entrega)
    

    def lista_Encomendas_Cliente(self, id_cliente):

        if id_cliente not in self.m_Encomendas.keys():
            self.m_Encomendas[id_cliente] = []
        
        for encomenda in self.m_Encomendas[id_cliente]:
            print(str(encomenda) + '\n')
            
    def lista_Estafetas_Classificacao(self):

        lista_Estafetas = {}

        for cliente,entrega in self.m_Entregas.items():
            for entrg in entrega:
                if entrg.getClassificacao() != str(None):
                    if entrg.getEstafeta() not in lista_Estafetas.keys():
                        lista_Estafetas[entrg.getEstafeta()] = []
                        lista_Estafetas[entrg.getEstafeta()].append(float(entrg.getClassificacao()))
                    else:
                        lista_Estafetas[entrg.getEstafeta()].append(float(entrg.getClassificacao()))

        for Estafeta, classificacoes in lista_Estafetas.items():
            lista_Estafetas[Estafeta] = (sum(classificacoes) / len(classificacoes))

        return lista_Estafetas
    
    def ranking_Estafetas_Ecológicos(self):

        lista_Estafetas = {}

        for cliente,entrega in self.m_Entregas.items():
            for entrg in entrega:
                veiculo = int(entrg.getVeiculo())
                estafeta = entrg.getEstafeta()
                if estafeta not in lista_Estafetas.keys():
                    if veiculo == 1:
                        lista_Estafetas[estafeta] = (1,0,0)
                    elif veiculo == 2:
                        lista_Estafetas[estafeta] = (0,1,0)
                    elif veiculo == 3:
                        lista_Estafetas[estafeta] = (0,0,1)
                else:
                    x,y,z = lista_Estafetas[estafeta]

                    if veiculo == 1:
                        lista_Estafetas[estafeta] = (x+1,y,z)
                    elif veiculo == 2:
                        lista_Estafetas[estafeta] = (x,y+1,z)
                    elif veiculo == 3:
                        lista_Estafetas[estafeta] = (x,y,z+1)

        valores_veiculos = {'bicicleta': 0, 'mota': 1, 'carro': 2}

        estafetas_ordenados = sorted(lista_Estafetas.items(), key=lambda item: (sum(valores_veiculos[tipo] * quantidade for tipo, quantidade in zip(['bicicleta', 'mota', 'carro'], item[1])),item[0]))

        print("Ranking Estafetas Ecológicos \n")

        for i in range(len(estafetas_ordenados)):
            print (str(i+1) + " -> " + str(estafetas_ordenados[i][0]) + " | Veiculos: " + "Bicicletas: " + str(estafetas_ordenados[i][1][0]) + " | Motas: " + str(estafetas_ordenados[i][1][1]) + " | Carros: " + str(estafetas_ordenados[i][1][2]) + "\n")



    def lista_Entregas_Cliente(self, id_Cliente):

        listaEntregas = []

        if id_Cliente not in self.m_Entregas.keys():
            self.m_Entregas[id_Cliente] = []

        for entrega in self.m_Entregas[id_Cliente]:
            listaEncomendas = entrega.getEncomenda()
            for enc in listaEncomendas:
                for enco in self.m_Encomendas[id_Cliente]:
                    if int(enc) == int(enco.getId_Encomenda()) and int(enco.getEstado()) == 0:
            # if (int(listaEncomendas[0].getEstado()) == 0):
                        listaEntregas.append(entrega)

        return listaEntregas

    def classificaEntrega(self,lista,escolha):
        
        for entrega in lista:

            if escolha == int(entrega.getId()):

                while True:
                    try:
                        # Solicitar entrada do usuário
                        classificacao = float(input("Digite uma classificação entre 0 e 5: "))

                        # Verificar se o número está dentro do intervalo
                        if 0 <= classificacao <= 5:
                            print("Classificado com sucesso!")
                            break  # Sai do loop se estiver dentro do intervalo
                        else:
                            raise SystemError("Classificação fora do intervalo. Tente novamente.")
                        
                    except SystemError as e:
                        print(e)
                        print('\n')

                    except ValueError as e:
                        print(e)
                        print('\n')
                        # print("Entrada inválida. Por favor, digite um número válido.")

                entrega.setClassificacao(classificacao)
                self.alterar_classificacao_entrega(entrega,classificacao,self.caminho_arquivo_Entregas)

    def alterar_classificacao_entrega(self,entrega,classificacao,pasta):

        with open(pasta, 'r') as file:
            linhas = file.readlines()

        for i, linha in enumerate(linhas):
            idEntrega ,idCliente, idEstafeta, classific, preco, veiculo, caminho, distancia, tempo, idEncomendas, algoritmo = linha.strip().split('; ')
            id = idEntrega.split("Id da Entrega: ")
            if int(id[1]) == entrega.getId():
                linhas[i] = f'{idEntrega}; {idCliente}; {idEstafeta}; Classificação: {classificacao}; {preco}; {veiculo}; {caminho}; {distancia}; {tempo}; {idEncomendas}; {algoritmo}\n'
                break

        with open(pasta, 'w') as file:
            file.writelines(linhas)


    def dividir_lista(self, lista, freg):
        resultado = []
        sublista = []

        for elemento in lista:
            if elemento == freg:
                if sublista:
                    sublista.append(elemento)
                    resultado.append(sublista)
                    sublista = []
                    sublista.append(elemento)
                else:
                    sublista.append(elemento)
            else:
                sublista.append(elemento)

        if sublista:
         resultado.append(sublista)

        return resultado
    
    # def sistemaCalculaCaminho(self, start, listDestinos, g):
    #     entregaCircuito = []

    #     for freg in listDestinos:
    #         if len(entregaCircuito) > 0:
    #             for caminho in entregaCircuito:
    #                     freg2 = g.verification(freg)
    #                     if freg2 in caminho:
    #                         caminho = self.dividir_lista(caminho,freg)
    #                         print(caminho)
    #                     else:
    #                         if start == freg:
    #                             start3 = g.verification(start)
    #                             entregaCircuito.append([start3])
    #                         else:
    #                             start1 = g.verification(start)
    #                             freg1 = g.verification(freg)

    #                             (dfs_caminho, dfs_custo) = g.procura_DFS(start1, freg1, path=[], visited=set())
    #                             (bfs_caminho, bfs_custo) = g.procura_BFS(start1, freg1)
    #                             g.add_all_heuristica(freg1)
    #                             (aEstr_caminho, aEstr_custo) = g.procura_aStar(start1, freg1)
    #                             (greedy_caminho, greedy_custo) = g.greedy(start1, freg1)

    #                             custo = min(dfs_custo, bfs_custo, aEstr_custo, greedy_custo)

    #                             if custo == aEstr_custo:
    #                                 entregaCircuito.append(aEstr_caminho)
    #                             elif custo == dfs_custo:
    #                                 entregaCircuito.append(dfs_caminho)
    #                             elif custo == bfs_custo:
    #                                 entregaCircuito.append(bfs_caminho)
    #                             else:
    #                                 entregaCircuito.append(greedy_caminho)
    #         else:
    #             if start == freg:
    #                         start3 = g.verification(start)
    #                         entregaCircuito.append([start3])
    #             else:
    #                 start1 = g.verification(start)
    #                 freg1 = g.verification(freg)
    #                 (dfs_caminho, dfs_custo) = g.procura_DFS(start1, freg1, path=[], visited=set())
    #                 (bfs_caminho, bfs_custo) = g.procura_BFS(start1, freg1)
    #                 g.add_all_heuristica(freg1)
    #                 (aEstr_caminho, aEstr_custo) = g.procura_aStar(start1, freg1)
    #                 (greedy_caminho, greedy_custo) = g.greedy(start1, freg1)
    #                 custo = min(dfs_custo, bfs_custo, aEstr_custo, greedy_custo)
    #                 if custo == aEstr_custo:
    #                     entregaCircuito.append(aEstr_caminho)
    #                 elif custo == dfs_custo:
    #                     entregaCircuito.append(dfs_caminho)
    #                 elif custo == bfs_custo:
    #                     entregaCircuito.append(bfs_caminho)
    #                 else:
    #                     entregaCircuito.append(greedy_caminho)
    #         start = freg

    #     return entregaCircuito
    
    def escolheCaminho(self,start,end):

        start1 = self.g.verification(start)
        end1 = self.g.verification(end)

        (dfs_caminho, dfs_custo, dfs_expansao) = self.g.procura_DFS(start1, end1, path=[], visited=set())

        (bfs_caminho, bfs_custo, bfs_expansao) = self.g.procura_BFS(start1, end1)

        (uniform_caminho, uniform_custo, uniform_expansao) = self.g.uniform_cost(start1,end1)

        self.g.add_all_heuristica(end1)

        (aEstr_caminho, aEstr_custo, aEstr_expansao) = self.g.procura_aStar(start1, end1)

        (greedy_caminho, greedy_custo, greedy_expansao) = self.g.greedy(start1, end1)

        custo = min(dfs_custo, bfs_custo, uniform_custo, aEstr_custo, greedy_custo)

        if custo == aEstr_custo:
            return (aEstr_caminho,aEstr_custo,aEstr_expansao)
        elif custo == dfs_custo:
            return (dfs_caminho,dfs_custo,dfs_expansao)
        elif custo == bfs_custo:
            return (bfs_caminho,bfs_custo,bfs_expansao)
        elif custo == uniform_custo:
            return (uniform_caminho,uniform_custo,uniform_expansao)
        else:
            return (greedy_caminho,greedy_custo,greedy_expansao)

    
    def escolheVeiculoPeso_Volume(self, encomenda):
        listaVeiculosEncomenda = []
        peso = 0
        volume = 0

        for enco in encomenda:
            peso = peso + float(enco.getPeso())
            volume = volume + float(enco.getVolume())


        if peso <= 5 and volume <= 50:
            listaVeiculosEncomenda = [1,2,3]
        elif peso <= 20 and volume <= 100:
            listaVeiculosEncomenda = [2,3]
        elif peso <= 100 and volume <= 150:
            listaVeiculosEncomenda = [3]

        return (listaVeiculosEncomenda,peso)

    def bicicletaCusto(self,custoCaminho,peso):
        velMax = 10
        decresc = 0.6
        velAtual = 0

        velAtual = velMax - (peso * decresc)

        tempo = custoCaminho/velAtual

        return tempo
    
    def motaCusto(self,custoCaminho,peso):
        velMax = 35
        decresc = 0.5
        velAtual = 0

        velAtual = velMax - (peso * decresc)

        tempo = custoCaminho/velAtual

        return tempo
    
    def carroCusto(self,custoCaminho,peso):
        velMax = 50
        decresc = 0.1
        velAtual = 0

        velAtual = velMax - (peso * decresc)

        tempo = custoCaminho/velAtual

        return tempo
    
    def tempoVeiculosEncomenda(self, listaVeiculos, custoCaminho, peso):
        tempoVeiculos = []
        tempoBicicleta = 0
        tempoMota = 0
        tempoCarro = 0
        
        for veiculo in listaVeiculos:
            if veiculo == 1: # 1 = Bicicleta
                tempoBicicleta = self.bicicletaCusto(custoCaminho,peso)
                tempoVeiculos.append(tempoBicicleta)
            elif veiculo == 2: # 2 = Mota
                tempoMota = self.motaCusto(custoCaminho,peso)
                tempoVeiculos.append(tempoMota)
            else:
                tempoCarro = self.carroCusto(custoCaminho,peso)
                tempoVeiculos.append(tempoCarro)
        
        return tempoVeiculos
    
    def tempoListaVeiculo(self,entrega,g):
        listaDistancias = []
        lista = []
        caminho = entrega.getCaminho()
        encomenda = entrega.getEncomenda()
        veiculo = entrega.getVeiculo()

        aux = caminho

        i = 0

        while i + 1 < len(aux):
            listaDistancias.append(g.get_arc_cost(aux[i],aux[i+1]))
            i= i + 1

        if veiculo == 1:
            for distancia in listaDistancias:
                lista.append(self.bicicletaCusto(distancia,encomenda.getPeso()))
        elif veiculo == 2:
            for distancia in listaDistancias:
                lista.append(self.motaCusto(distancia,encomenda.getPeso()))
        else:
            for distancia in listaDistancias:
                lista.append(self.carroCusto(distancia,encomenda.getPeso()))

        return lista
    
    def decideVeiculo(self,listaTemposVeiculos,prazoEntrega):

        tam = len(listaTemposVeiculos)
        i = 1

        if tam == 3:
            for tempo in listaTemposVeiculos:
                if tempo <= int(prazoEntrega):
                    return (i,tempo)
                i = i + 1

        elif tam == 2:
            i = 2
            for tempo in listaTemposVeiculos:
                if tempo <= int(prazoEntrega):
                    return (i,tempo)
                i = i + 1
        else: return (3,listaTemposVeiculos[0])

    def calculaPrecoServico(self,peso,veiculo,prazo,distancia):
        # Prazo >= 24h = 0$
        # Prazo >= 12h = 2.5$
        # Prazo >= 6h = 5$

        valorPrazo = 0

        if (float(prazo) >= 24):
            valorPrazo = 0
        elif (float(prazo) >= 12):
            valorPrazo = 2.5
        elif (float(prazo) >= 6):
            valorPrazo = 5
        elif (float(prazo) < 6):
            valorPrazo = 8

        custoBicicleta = 1

        custoMota = 3

        custoCarro = 6

        precoServico = 0

        if veiculo == 1:
            precoServico = float(custoBicicleta) + float((distancia * 0.2)) + (float(peso) * 0.1) + float(valorPrazo)
        elif veiculo == 2:
            precoServico = float(custoMota) + float((distancia * 0.5)) + (float(peso) * 0.1) + float(valorPrazo)
        else:
            precoServico = float(custoCarro) + float((distancia * 0.8)) + (float(peso) * 0.1) + float(valorPrazo)

        return precoServico
    
    def createEntregaEncomendas(self,idCliente,ids):

        encomendas = []

        file = open(self.caminho_arquivo_Entregas, 'a+')

        file.seek(0)

        idEntrega = (len(file.readlines())) + 1

        id = ids.split(",")

        for i in id:
            for enc in self.m_EncPendentes:
                if int(enc.getId_Encomenda()) == int(i):
                    self.m_EncPendentes.remove(enc)
                    self.remover_encomendasPendentes_ficheiro(enc)


        print('\n')
        print("Pretende escolher um Algoritmo ou deseja que seja o Sistema a escolher?")
        print('\n')
        print("1 - SIM")
        print("0 - NÃO")

        while True:
            try:

                escolha = input("Introduza a sua opção: ")

                if int(escolha) == 1:
                    print('\n')
                    print("1 - DFS")
                    print("2 - BFS")
                    print("3 - UNIFORM")
                    print("4 - A*")
                    print("5 - GREEDY")
                    print('\n')

                    while True:
                        try:

                            escolhaAlgoritmo = input("Introduza a sua opção: ")

                            for i in id:
                                for encomenda in self.m_Encomendas[idCliente]:
                                    if int(encomenda.getId_Encomenda()) == int(i):
                                        if encomenda.getEstado() != 0:
                                            encomendas.append(encomenda)
                                        else:
                                            print("Encomenda com o Id: " + encomenda.getId_Encomenda() + " já foi entregue!")

                            if len(encomendas) == 0:
                                return None


                            prazo = int(encomendas[0].getPrazoEntrega())

                            for enc in encomendas:
                                if prazo > int(enc.getPrazoEntrega()):
                                    prazo = int(enc.getPrazoEntrega())

                            listaEstafetas = list(self.m_Estafetas.keys())

                            estafeta = random.choice(listaEstafetas)

                            l = self.escolheVeiculoPeso_Volume(encomendas)

                            if len(l) == 0:
                                return None

                            cliente = self.m_Clientes[idCliente]

                            print(cliente.getFreguesia())

                            start = self.g.verification("Health Planet")
                            end = self.g.verification(cliente.getFreguesia())

                            idsEncomendas = []

                            for enc in encomendas:
                                idsEncomendas.append(enc.getId_Encomenda())

                            if int(escolhaAlgoritmo) == 1:
                            
                                caminho = self.g.procura_DFS(start,end)
                                print(caminho)

                                ordemExpansao = []

                                for nodo in caminho[2]:
                                    ordemExpansao.append(nodo.getName())

                                lvt = self.tempoVeiculosEncomenda(l[0],caminho[1],l[1])

                                result = self.decideVeiculo(lvt,prazo)

                                if result != None:
                                    custo = self.calculaPrecoServico(l[1],result[0],prazo,caminho[1])

                                    entrega = Entrega(idEntrega,idCliente,estafeta,None,custo,result[0],caminho[0],caminho[1],result[1],idsEncomendas,'DFS')

                                    if idCliente not in self.m_Entregas.keys():
                                        self.m_Entregas[idCliente] = []

                                    self.m_Entregas[idCliente].append(entrega)

                                    file.write(str(entrega) + "\n")
                                    print("Entrega criada com sucesso! \n")

                                    return (entrega,ordemExpansao)

                                else:
                                    print("Impossivel realizar a entrega no prazo estipulado!")
                                    return None

                            elif int(escolhaAlgoritmo) == 2:
                            
                                caminho = self.g.procura_BFS(start,end)

                                ordemExpansao = []

                                for nodo in caminho[2]:
                                    ordemExpansao.append(nodo.getName())

                                lvt = self.tempoVeiculosEncomenda(l[0],caminho[1],l[1])

                                result = self.decideVeiculo(lvt,prazo)

                                if result != None:
                                    custo = self.calculaPrecoServico(l[1],result[0],prazo,caminho[1])

                                    entrega = Entrega(idEntrega,idCliente,estafeta,None,custo,result[0],caminho[0],caminho[1],result[1],idsEncomendas,'BFS')

                                    if idCliente not in self.m_Entregas.keys():
                                        self.m_Entregas[idCliente] = []

                                    self.m_Entregas[idCliente].append(entrega)

                                    file.write(str(entrega) + "\n")
                                    print("Entrega criada com sucesso! \n")

                                    return (entrega,ordemExpansao)
                                else:
                                    print("Impossivel realizar a entrega no prazo estipulado!")
                                    return None
                                
                            elif int(escolhaAlgoritmo) == 3:

                                caminho = self.g.uniform_cost(start,end)

                                ordemExpansao = []

                                for nodo in caminho[2]:
                                    ordemExpansao.append(nodo.getName())

                                lvt = self.tempoVeiculosEncomenda(l[0],caminho[1],l[1])

                                result = self.decideVeiculo(lvt,prazo)

                                if result != None:
                                    custo = self.calculaPrecoServico(l[1],result[0],prazo,caminho[1])

                                    entrega = Entrega(idEntrega,idCliente,estafeta,None,custo,result[0],caminho[0],caminho[1],result[1],idsEncomendas,'UNIFORM')

                                    if idCliente not in self.m_Entregas.keys():
                                        self.m_Entregas[idCliente] = []

                                    self.m_Entregas[idCliente].append(entrega)

                                    file.write(str(entrega) + "\n")
                                    print("Entrega criada com sucesso! \n")

                                    return (entrega,ordemExpansao)
                                else:
                                    print("Impossivel realizar a entrega no prazo estipulado!")
                                    return None

                            elif int(escolhaAlgoritmo) == 4:
                            
                                self.g.add_all_heuristica(end)

                                caminho = self.g.procura_aStar(start,end)

                                ordemExpansao = []

                                for nodo in caminho[2]:
                                    ordemExpansao.append(nodo.getName())

                                lvt = self.tempoVeiculosEncomenda(l[0],caminho[1],l[1])

                                result = self.decideVeiculo(lvt,prazo)

                                if result != None:
                                    custo = self.calculaPrecoServico(l[1],result[0],prazo,caminho[1])

                                    entrega = Entrega(idEntrega,idCliente,estafeta,None,custo,result[0],caminho[0],caminho[1],result[1],idsEncomendas,'A*')

                                    if idCliente not in self.m_Entregas.keys():
                                        self.m_Entregas[idCliente] = []

                                    self.m_Entregas[idCliente].append(entrega)

                                    file.write(str(entrega) + "\n")
                                    print("Entrega criada com sucesso! \n")

                                    return (entrega,ordemExpansao)
                                else:
                                    print("Impossivel realizar a entrega no prazo estipulado!")
                                    return None

                            elif int(escolhaAlgoritmo) == 5:
                            
                                self.g.add_all_heuristica(end)

                                caminho = self.g.greedy(start,end)

                                ordemExpansao = []

                                for nodo in caminho[2]:
                                    ordemExpansao.append(nodo.getName())

                                lvt = self.tempoVeiculosEncomenda(l[0],caminho[1],l[1])

                                result = self.decideVeiculo(lvt,prazo)

                                if result != None:
                                    custo = self.calculaPrecoServico(l[1],result[0],prazo,caminho[1])

                                    entrega = Entrega(idEntrega,idCliente,estafeta,None,custo,result[0],caminho[0],caminho[1],result[1],idsEncomendas,'GREEDY')

                                    if idCliente not in self.m_Entregas.keys():
                                        self.m_Entregas[idCliente] = []

                                    self.m_Entregas[idCliente].append(entrega)

                                    file.write(str(entrega) + "\n")
                                    print("Entrega criada com sucesso! \n")

                                    return (entrega,ordemExpansao)
                                else:
                                    print("Impossivel realizar a entrega no prazo estipulado!")
                                    return None
                            
                            else:
                                print("Digite um dos nº mostrados na tela!")
                                print('\n')
        
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número válido.")
                            print('\n')

                elif int(escolha) == 0:
                
                    for i in id:
                        for encomenda in self.m_Encomendas[idCliente]:
                            if int(encomenda.getId_Encomenda()) == int(i):
                                if int(encomenda.getEstado()) != 0:
                                    encomendas.append(encomenda)
                                else:
                                    print("Encomenda com o Id: " + str(encomenda.getId_Encomenda()) + " já foi entregue!")

                    if len(encomendas) == 0:
                        return None

                    prazo = encomendas[0].getPrazoEntrega()

                    for enc in encomendas:
                        if prazo > enc.getPrazoEntrega():
                            prazo = enc.getPrazoEntrega()

                    listaEstafetas = list(self.m_Estafetas.keys())

                    estafeta = random.choice(listaEstafetas)

                    l = self.escolheVeiculoPeso_Volume(encomendas)

                    idsEncomendas = []

                    for enc in encomendas:
                        idsEncomendas.append(enc.getId_Encomenda())

                    if len(l) == 0:
                        return None

                    cliente = self.m_Clientes[idCliente]

                    start = "Health Planet"
                    end = cliente.getFreguesia()

                    caminho = self.escolheCaminho(start,end)

                    ordemExpansao = []

                    for nodo in caminho[2]:
                        ordemExpansao.append(nodo.getName())

                    lvt = self.tempoVeiculosEncomenda(l[0],caminho[1],l[1])

                    result = self.decideVeiculo(lvt,prazo)

                    if result != None:
                        custo = self.calculaPrecoServico(l[1],result[0],prazo,caminho[1])

                        entrega = Entrega(idEntrega,idCliente,estafeta,None,custo,result[0],caminho[0],caminho[1],result[1],idsEncomendas,'A*')

                        if idCliente not in self.m_Entregas.keys():
                            self.m_Entregas[idCliente] = []

                        self.m_Entregas[idCliente].append(entrega)

                        file.write(str(entrega) + "\n")
                        print("Entrega criada com sucesso! \n")

                        return (entrega,ordemExpansao)  
                    
                    else:
                        print("Impossivel realizar a entrega no prazo estipulado!")
                        return None

                else:
                    print("Digite um dos nº mostrados na tela!")
                    print('\n')

            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
                print('\n')

    def guardaEncomendas(self, idCliente, ids):

        file = open(self.caminho_arquivo_Encomendas_Pendentes, 'a')

        id = ids.split(",")

        x = 0

        for i in id:
            flag = 0
            for encomenda in self.m_Encomendas[idCliente]:
                if int(encomenda.getId_Encomenda()) == int(i):
                    for enc in self.m_EncPendentes:
                        if enc.getId_Encomenda() == encomenda.getId_Encomenda():
                            flag = flag + 1

                    if int(encomenda.getEstado()) != 0:
                        if flag == 0:
                            self.m_EncPendentes.append(encomenda)
                            file.write(str(encomenda) + '\n')
                            x = x + 1
                        else:
                            print("A encomenda com o Id: " + str(encomenda.getId_Encomenda()) + " já foi registada nas encomendas pendentes!")
                    else:
                        print("A encomenda com o Id: " + str(encomenda.getId_Encomenda()) + " já foi entregue!")

        if x != 0:
            return True
        else:
            return False       
    
    def entregaRealizada(self,entrega,idCliente):
        encomenda = entrega.getEncomenda()
        # print(encomenda)
        for enc in encomenda:
            for encomendas in self.m_Encomendas[idCliente]:
                # print(encomendas)
                if encomendas.getId_Encomenda() == enc:
                    encomendas.setEstado(0)
                    self.alterar_estado_encomenda(encomendas.getId_Encomenda(),0,self.caminho_arquivo_Encomendas)
                    print("Entrega da encomenda: " + str(encomendas.getId_Encomenda()) + " foi entregue com sucesso! \n")

            for enco in self.m_EncPendentes:
                if enco.getId_Encomenda() == enc:
                    self.m_EncPendentes.remove(enco)
                    self.remover_encomendasPendentes_ficheiro(enco)

    def alterar_estado_encomenda(self,id_encomenda, novo_estado,caminho):
        # Abre o arquivo em modo de leitura
        with open(caminho, 'r') as file:
            linhas = file.readlines()

        # Procura a linha correspondente ao ID da encomenda
        for i, linha in enumerate(linhas):
            id_Cliente, id_Encomenda,peso,volume,prazo,estado = linha.strip().split('; ')
            id = id_Encomenda.split("Id da Encomenda: ")
            if int(id_encomenda) == int(id[1]):
                # Atualiza o estado da encomenda
                linhas[i] = f'{id_Cliente}; Id da Encomenda: {id_encomenda}; {peso}; {volume}; {prazo}; Estado: {novo_estado}\n'
                break

        # Abre o arquivo em modo de escrita e escreve as alterações
        with open(caminho, 'w') as file:
            file.writelines(linhas)

    def remover_encomendasPendentes_ficheiro(self,encomenda):

        with open(self.caminho_arquivo_Encomendas_Pendentes, 'r') as file:
            linhas = file.readlines()

        for i, linha in enumerate(linhas):
            id_Cliente, id_Encomenda,peso,volume,prazo,estado = linha.strip().split('; ')
            id = id_Encomenda.split("Id da Encomenda: ")
            if encomenda.getId_Encomenda() == int(id[1]):
                linhas.pop(i)
                break

        with open(self.caminho_arquivo_Encomendas_Pendentes, 'w') as file:
            file.writelines(linhas)


    def listarEncomendasSemEntrega(self, idCliente):
        encomendas_sem_entrega = []

        for encomenda in self.m_Encomendas.get(idCliente, []):
            encomenda_tem_entrega = False

            for entrega in self.m_Entregas.get(idCliente, []):
                if entrega.getEncomenda() == encomenda:
                    encomenda_tem_entrega = True
                    break

            if not encomenda_tem_entrega:
                encomendas_sem_entrega.append(encomenda)

        return encomendas_sem_entrega
    
    def organizaListaHeuristica(self):
        l = []

        self.g.add_all_heuristica(self.g.verification("Health Planet"))

        l = sorted(self.m_EncPendentes, key=lambda encomenda: self.g.getH(self.g.verification(self.m_Clientes[encomenda.getId_Cliente()].getFreguesia())))

        return l
    
    def calculaNrVeiculos(self,lista):

        NrVeiculos = [0,0,0]

        for veiculo in lista:
            if veiculo == 1:
                NrVeiculos[0] += 1
            elif veiculo == 2:
                NrVeiculos[1] += 1
            else:
                NrVeiculos[2] += 1

        return NrVeiculos
    
    def recalculaTempo(self,lista,veiculo):

        pesoEncomendas = 0

        tempoAux = 0

        for tuplo in lista:
            listaEncomenda = tuplo[0]
            for encomenda in listaEncomenda:
                pesoEncomendas += float(encomenda.getPeso())

        for indice, tuplo in enumerate(lista):
            if indice == 0:
                if veiculo == 1:
                   self.g.add_all_heuristica(self.g.verification("Health Planet"))

                   freguesia = self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia()

                   path = self.escolheCaminho("Health Planet", freguesia)

                   tempo = (self.bicicletaCusto(path[1],pesoEncomendas))
                   tempoEntregas = tempo + 0.10
                   tempoAux = tempoEntregas
                   tuplo[1] = tempo
                   tuplo[2] = path

                   for enc in tuplo[0]:
                       pesoEncomendas -= float(enc.getPeso())

                elif veiculo == 2:
                    self.g.add_all_heuristica(self.g.verification("Health Planet"))

                    freguesia = self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia()

                    path = self.escolheCaminho("Health Planet", freguesia)

                    tempo = (self.motaCusto(path[1],pesoEncomendas))
                    tempoEntregas = tempo + 0.10
                    tempoAux = tempoEntregas
                    tuplo[1] = tempo
                    tuplo[2] = path

                elif veiculo == 3:
                    self.g.add_all_heuristica(self.g.verification("Health Planet"))

                    freguesia = self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia()

                    path = self.escolheCaminho("Health Planet", freguesia)

                    tempo = (self.carroCusto(path[1],pesoEncomendas))
                    tempoEntregas = tempo + 0.10
                    tempoAux = tempoEntregas
                    tuplo[1] = tempo
                    tuplo[2] = path

            else:
                if veiculo == 1:
                   
                   self.g.add_all_heuristica(self.g.verification(freguesia))

                   path = self.escolheCaminho(freguesia,self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia())

                   freguesia = self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia()

                   tempoOutras = (self.bicicletaCusto(path[1],pesoEncomendas)) + tempoAux
                   tmpAux = tempoOutras + 0.10
                   tempoAux = tmpAux
                   tuplo[1] = tempoOutras
                   tuplo[2] = path

                   for enco in tuplo[0]:
                       pesoEncomendas -= float(enco.getPeso())
                
                elif veiculo == 2:

                   self.g.add_all_heuristica(self.g.verification(freguesia))

                   path = self.escolheCaminho(freguesia,self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia())

                   freguesia = self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia()

                   tempoOutras = (self.motaCusto(path[1],pesoEncomendas)) + tempoAux
                   tmpAux = tempoOutras + 0.10
                   tempoAux = tmpAux
                   tuplo[1] = tempoOutras
                   tuplo[2] = path

                elif veiculo == 3:

                   self.g.add_all_heuristica(self.g.verification(freguesia))

                   path = self.escolheCaminho(freguesia,self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia())

                   freguesia = self.m_Clientes[tuplo[0][0].getId_Cliente()].getFreguesia()

                   tempoOutras = (self.carroCusto(path[1],pesoEncomendas)) + tempoAux
                   tmpAux = tempoOutras + 0.10
                   tempoAux = tmpAux
                   tuplo[1] = tempoOutras
                   tuplo[2] = path

        return lista

    def tentaAdicionar(self,listaEntregas,listaRemovidas,veiculo):

        # print(len(listaRemovidas))
        # print(veiculo)
        # for enco in listaEntregas:
        #     print(enco[0])

        # print('\n')

        # for enc in listaRemovidas:
        #     print(enc[0])

        # print('\n')

        if (len(listaRemovidas) == 0):
            return listaEntregas
        else:
            while (len(listaRemovidas) != 0):

                for encomenda in listaRemovidas[:]:

                    # print(encomenda)
                    # print(encomenda[3])
                    # print('\n')
                    
                    flag = 0

                    # print(encomenda)

                    copia = copy.deepcopy(listaEntregas) 

                    # for encom in copia:
                    #     print(encom[0])
                    #     print(encom[1])
                    # print('\n')

                    for item in copia:
                        if encomenda[0][0].getId_Cliente() == item[0][0].getId_Cliente():
                            item[0].extend(encomenda[0])
                            item[0] = sorted(item[0], key=lambda encomenda: float(encomenda.getPrazo()))
                            flag = flag + 1

                    if flag == 0:
                        copia.insert(encomenda[3], encomenda)

                    # for encome in copia:
                    #     print(encome)
                    #     print(encome[1])
                    # print('\n')

                    l = self.recalculaTempo(copia,veiculo)

                    # for encomem in l:
                    #     print(encomem[0])
                    #     print(encomem[1])
                    # print('\n')

                    for tuplo in l:

                        if tuplo[1] > float(tuplo[0][0].getPrazoEntrega()):
                            # print('aqui')
                            listaRemovidas.remove(encomenda)
                            break

                if (len(listaRemovidas) == 0):
                    return listaEntregas
                else:

                    peso = 101

                    for tuplo in listaRemovidas:
                        pesoEnco = 0
                        for encomen in tuplo[0]:
                            pesoEnco += float(encomen.getPeso())

                        # pesoE = float(tuplo[0].getPeso())
                        if pesoEnco < peso:
                            peso = pesoEnco
                            t = tuplo
                    
                    # print(t[1])
                    # print(t)
                            
                    for item in listaEntregas:
                        if t[0][0].getId_Cliente() == item[0][0].getId_Cliente():
                            item[0].extends(t[0])
                            item[0] = sorted(item[0], key=lambda encomenda: float(encomenda.getPrazo()))
                            flag = flag + 1

                    if flag == 0:
                        listaEntregas.insert(t[3], t)

                    # listaEntregas.insert(t[3],tuplo)
                    listaEntregas = self.recalculaTempo(listaEntregas,veiculo)
                    listaRemovidas.remove(t)

        return listaEntregas
    
    def existsPesoBicicleta(self,lista):
        for enc in lista:
            if int(enc.getPeso()) <= 5:
                return True
        return False
    
    def existsPesoMota(self,lista):
        for enc in lista:
            if int(enc.getPeso()) <= 20:
                return True
        return False
    
    def existsPesoCarro(self,lista):
        for enc in lista:
            if int(enc.getPeso()) <= 100:
                return True
        return False
    
    def somaLista(self,lista):
        sum = 0
        for enc in lista:
            sum = sum + int(enc.getPeso())
        return sum
    
    def verificaEncomendaSozinho(self,encomenda,veiculo):

        tempo = 0

        freguesia = self.m_Clientes[encomenda.getId_Cliente()].getFreguesia()

        self.g.add_all_heuristica(self.g.verification(freguesia))

        caminho = self.escolheCaminho("Health Planet",freguesia)

        if veiculo == 1:

            tempo = self.bicicletaCusto(caminho[1],int(encomenda.getPeso()))

            # print('Tempo bicicleta: ' + str(tempo))

            if tempo > int(encomenda.getPrazoEntrega()) or encomenda.getVolume() > 50 or encomenda.getPeso() > 5:
                return False
        
        elif veiculo == 2:
            
            tempo = self.motaCusto(caminho[1],int(encomenda.getPeso()))

            # print('Tempo mota: ' + str(tempo))

            if tempo > int(encomenda.getPrazoEntrega()) or encomenda.getVolume() > 100 or encomenda.getPeso() > 20:
                return False
            
        elif veiculo == 3:
            tempo = self.carroCusto(caminho[1],int(encomenda.getPeso()))

            # print('Tempo carro: ' + str(tempo))

            if tempo > int(encomenda.getPrazoEntrega()) or encomenda.getVolume() > 150 or encomenda.getPeso() > 100:
                return False
            
        return True
    
    

   
    def createEntregaEncPend(self,lista,pasta):

        ListaEstafetas = list(self.m_Estafetas.keys())
        ListaVeiculos = list(self.m_Veiculos)

        Veiculos = self.calculaNrVeiculos(ListaVeiculos)
        nrVeiculos = sum(Veiculos)

        while (len(lista) != 0 and nrVeiculos != 0 and (len(ListaEstafetas) != 0)):

            print("tamanho lista: " + str(len(lista)))
            print("nrº veiculos: " + str(nrVeiculos))
            print("nrº estafetas: " + str(len(ListaEstafetas)))

            z = 0

            EncomendasParaEntrega = [] # lista com o máximo possivel num veiculo

            listaAux = [] # lista das encomendas removidas

            aux = [] # lista de tuplos das encomendas possiveis com o seu tempo associado

            peso = 0

            volume = 0

            flagVeiculo = 0

            for encomenda in lista[:]:
                # print(encomenda)
                # print(self.verificaEncomendaSozinho(encomenda,1))
                # print('\n')
                if (Veiculos[0] != 0 and self.existsPesoBicicleta(lista) and self.verificaEncomendaSozinho(encomenda,1)):
                    if len(EncomendasParaEntrega) != 0 and flagVeiculo != 1:
                        pass
                    elif ((peso + float(encomenda.getPeso())) <= 5 and (volume + float(encomenda.getVolume())) <= 50):
                        peso = peso + float(encomenda.getPeso())
                        volume = volume + float(encomenda.getVolume())
                        EncomendasParaEntrega.append(encomenda)
                        flagVeiculo = 1

                elif (Veiculos[1] != 0 and self.existsPesoMota(lista) and self.verificaEncomendaSozinho(encomenda,2)):
                    if len(EncomendasParaEntrega) != 0 and flagVeiculo != 2:
                        pass
                    elif ((peso + float(encomenda.getPeso())) <= 20 and (volume + float(encomenda.getVolume())) <= 100):
                        peso = peso + float(encomenda.getPeso())
                        volume = volume + float(encomenda.getVolume())
                        # print(peso)
                        # print(volume)
                        # print('\n')
                        EncomendasParaEntrega.append(encomenda)
                        flagVeiculo = 2

                elif (Veiculos[2] != 0 and self.existsPesoCarro(lista) and self.verificaEncomendaSozinho(encomenda,3)):
                    if len(EncomendasParaEntrega) != 0 and flagVeiculo != 3:
                        pass
                    elif((peso + float(encomenda.getPeso())) <= 100 and (volume + float(encomenda.getVolume())) <= 150):
                        peso = peso + float(encomenda.getPeso())
                        volume = volume + float(encomenda.getVolume())
                        EncomendasParaEntrega.append(encomenda)
                        flagVeiculo = 3

            EncomendasParaEntrega = sorted(EncomendasParaEntrega, key=lambda encomenda: float(encomenda.getPrazoEntrega()))

            # print(flagVeiculo)

            # for enc in EncomendasParaEntrega:
            #     print(enc)

            # print('\n')

            # Dicionário para armazenar as encomendas de cada cliente
            encomendas_por_cliente = {}

            # Lista resultante
            resultadoClientes = []

            # Iterar sobre a lista original
            for encomenda in EncomendasParaEntrega:
                cliente = encomenda.getId_Cliente()
                # Verificar se já vimos esse cliente antes
                if cliente not in encomendas_por_cliente:
                    # Se é a primeira vez, adicionar à lista resultante
                    resultadoClientes.append(encomenda)
                    # Iniciar uma lista para armazenar as encomendas desse cliente
                    encomendas_por_cliente[cliente] = [encomenda]
                else:
                    # Se já vimos esse cliente, adicionar à lista de encomendas desse cliente
                    encomendas_por_cliente[cliente].append(encomenda)
                    # Adicionar à lista resultante no índice anterior da última encomenda desse cliente
                    resultadoClientes.insert(resultadoClientes.index(encomendas_por_cliente[cliente][-2]) + 1, encomenda)

            # EncomendasParaEntrega = sorted(EncomendasParaEntrega, key=lambda encomenda: encomenda.getId_Cliente())

            # EncomendasParaEntrega = sorted(EncomendasParaEntrega, key=chave_de_ordenacao)

            # for enc in resultadoClientes:
            #     print(enc)

            # print('\n')

            resultado = []
            grupo_atual = []

            for i in range(len(resultadoClientes)):
                if i > 0 and resultadoClientes[i].getId_Cliente() != resultadoClientes[i - 1].getId_Cliente():
                    resultado.append(grupo_atual)
                    grupo_atual = []

                grupo_atual.append(resultadoClientes[i])

            resultado.append(grupo_atual)

            EncomendasParaEntrega = [grupo for grupo in resultado if grupo]

            # for ite in EncomendasParaEntrega:
            #     print('1')
            #     for it in ite:
            #         print(it)
            #     print('\n')

            flag = 1

            i = 0

            estafetaId = random.choice(ListaEstafetas)
            estafeta = self.m_Estafetas[estafetaId]
            entregasEstafeta = []


            if flagVeiculo == 1:

                # print("io")

                for listaCliente in EncomendasParaEntrega:

                    listaEncomendas = []

                    listaRemovidas = []
                    
                    for encomenda in listaCliente:
                        # print(encomenda)

                        x = 0

                        # print("x: " + str(encomenda))
                        # print(flag)

                        pesoEncomendas = 0
                        tempoAux = 0

                        freguesia = self.m_Clientes[(encomenda.getId_Cliente())].getFreguesia()

                        if (flag == 1):
                            # print('fiz aquilo')
                            caminho = self.escolheCaminho("Health Planet", freguesia)
                        else:
                            # print('fiz isto')
                            # tamAux = (len(aux) - 1)
                            # print(len(aux))
                            # print(tamAux)
                            # print(aux)
                            # print(self.m_Clientes[aux[-1][0][0].getId_Cliente()].getFreguesia())
                            caminho = self.escolheCaminho(self.m_Clientes[aux[-1][0][0].getId_Cliente()].getFreguesia(),freguesia)

                        # for cam in caminho[0]:
                        #     print(cam.getName())
                        # print("\n")

                        for l in EncomendasParaEntrega:
                            for encomendas in l:
                                pesoEncomendas += float(encomendas.getPeso())

                        tempo = self.bicicletaCusto(caminho[1],pesoEncomendas)

                        # print(tempo)

                        for entregas in aux:
                            tempoAux += entregas[1]
                            tempoAux += 0.10

                        if ((tempo + tempoAux) <= float(encomenda.getPrazoEntrega())):

                            # print('entreiaq')

                            # print(str(idCliente) + '\n')

                            listaEncomendas.append(encomenda)


                            # print(EncomendasParaEntrega)

                            # for enc in EncomendasParaEntrega[:]:
                            #     # print("y " + str(enc))
                            #     if enc.getId_Cliente() == idCliente:
                            #         # print('entrei \n')
                            #         listaEncomendas.append(enc)
                            #         EncomendasParaEntrega.remove(enc)
                            #         i = i + 1


                            # print(listaEncomendas)
                            # print(EncomendasParaEntrega)

                            # print(aux)

                            x = x + 1
                        else:
                            # print('entreiaqui')
                            listaRemovidas.append(encomenda)
                            # continue
                            # print('entreiaqui2')
                            # EncomendasParaEntrega.remove(encomenda)
                            # i = i + 1
                    # print("filo")

                    if len(listaEncomendas) != 0:

                        aux.append([listaEncomendas,(tempo + tempoAux),caminho])
                        flag = 0
                        i = i + 1

                    if len(listaRemovidas) != 0:

                        listaAux.append([listaRemovidas,0,caminho,i])

                    

            elif flagVeiculo == 2:

                for listaCliente in EncomendasParaEntrega:

                    listaEncomendas = []

                    listaRemovidas = []
                    
                    for encomenda in listaCliente:

                        # print(encomenda)

                        x = 0

                        # print("x: " + str(encomenda))
                        # print(flag)

                        pesoEncomendas = 0
                        tempoAux = 0

                        freguesia = self.m_Clientes[(encomenda.getId_Cliente())].getFreguesia()

                        if (flag == 1):
                            # print('fiz aquilo')
                            caminho = self.escolheCaminho("Health Planet", freguesia)
                        else:
                            # print('fiz isto')
                            # print(self.m_Clientes[aux[-1][0][0].getId_Cliente()].getFreguesia())
                            caminho = self.escolheCaminho(self.m_Clientes[aux[-1][0][0].getId_Cliente()].getFreguesia(),freguesia)

                        for l in EncomendasParaEntrega:
                            for encomendas in l:
                                pesoEncomendas += float(encomendas.getPeso())

                        tempo = self.motaCusto(caminho[1],pesoEncomendas)

                        # print(tempo)

                        for entregas in aux:
                            tempoAux += entregas[1]
                            tempoAux += 0.10

                        if ((tempo + tempoAux) <= float(encomenda.getPrazoEntrega())):

                            # print('entreiaq')

                            # print(str(idCliente) + '\n')

                            listaEncomendas.append(encomenda)


                            # print(EncomendasParaEntrega)

                            # for enc in EncomendasParaEntrega[:]:
                            #     # print("y " + str(enc))
                            #     if enc.getId_Cliente() == idCliente:
                            #         # print('entrei \n')
                            #         listaEncomendas.append(enc)
                            #         EncomendasParaEntrega.remove(enc)
                            #         i = i + 1


                            # print(listaEncomendas)
                            # print(EncomendasParaEntrega)

                            # print(aux)

                            x = x + 1
                        else:
                            # print('entreiaqui')
                            listaRemovidas.append(encomenda)
                            # listaAux.append([encomenda,0,caminho,i])
                            # EncomendasParaEntrega.remove(encomenda)
                            # i = i + 1

                    if len(listaEncomendas) != 0:
                        aux.append([listaEncomendas,(tempo + tempoAux),caminho])
                        flag = 0
                        i = i + 1

                    if len(listaRemovidas) != 0:

                        listaAux.append([listaRemovidas,0,caminho,i])


                    

                # for encomenda in EncomendasParaEntrega[:]:

                #     pesoEncomendas = 0
                #     tempoAux = 0

                #     freguesia = self.m_Clientes[(encomenda.getId_Cliente())].getFreguesia()

                #     if (flag == 1):
                #         caminho = self.escolheCaminho("Health Planet", freguesia)
                #     else:
                #         caminho = self.escolheCaminho(self.m_Clientes[aux[-1][0].getId_Cliente()].getFreguesia(), freguesia)

                #     for encomendas in EncomendasParaEntrega:
                #         pesoEncomendas += float(encomendas.getPeso())

                #     tempo = self.motaCusto(caminho[1],pesoEncomendas)

                #     for entregas in aux:
                #         tempoAux += entregas[1]
                #         tempoAux += 0.10

                #     if ((tempo + tempoAux) <= float(encomenda.getPrazoEntrega())):
                #         aux.append([encomenda,(tempo + tempoAux),caminho])
                #         EncomendasParaEntrega.remove(encomenda)
                #         i = i + 1
                #         flag = 0
                #     else:
                #         listaAux.append([encomenda,0,caminho,i])
                #         EncomendasParaEntrega.remove(encomenda)
                #         i = i + 1

            elif flagVeiculo == 3:

                for listaCliente in EncomendasParaEntrega:

                    listaEncomendas = []

                    listaRemovidas = []
                    
                    for encomenda in listaCliente:

                        x = 0

                        # print("x: " + str(encomenda))
                        # print(flag)

                        pesoEncomendas = 0
                        tempoAux = 0

                        freguesia = self.m_Clientes[(encomenda.getId_Cliente())].getFreguesia()

                        if (flag == 1):
                            # print('fiz aquilo')
                            caminho = self.escolheCaminho("Health Planet", freguesia)
                        else:
                            # print('fiz isto')
                            # print(self.m_Clientes[aux[-1][0][0].getId_Cliente()].getFreguesia())
                            caminho = self.escolheCaminho(self.m_Clientes[aux[-1][0][0].getId_Cliente()].getFreguesia(),freguesia)

                        for l in EncomendasParaEntrega:
                            for encomendas in l:
                                pesoEncomendas += float(encomendas.getPeso())

                        tempo = self.carroCusto(caminho[1],pesoEncomendas)

                        # print(tempo)

                        for entregas in aux:
                            tempoAux += entregas[1]
                            tempoAux += 0.10

                        if ((tempo + tempoAux) <= float(encomenda.getPrazoEntrega())):

                            # print('entreiaq')

                            # print(str(idCliente) + '\n')

                            listaEncomendas.append(encomenda)


                            # print(EncomendasParaEntrega)

                            # for enc in EncomendasParaEntrega[:]:
                            #     # print("y " + str(enc))
                            #     if enc.getId_Cliente() == idCliente:
                            #         # print('entrei \n')
                            #         listaEncomendas.append(enc)
                            #         EncomendasParaEntrega.remove(enc)
                            #         i = i + 1


                            # print(listaEncomendas)
                            # print(EncomendasParaEntrega)

                            # print(aux)

                            x = x + 1
                        else:
                            # print('entreiaqui')
                            listaRemovidas.append(encomenda)
                            
                            EncomendasParaEntrega.remove(encomenda)
                            # i = i + 1

                    if len(listaEncomendas) != 0:
                        aux.append([listaEncomendas,(tempo + tempoAux),caminho])
                        flag = 0
                        i = i + 1

                    if len(listaRemovidas) != 0:

                        listaAux.append([listaRemovidas,0,caminho,i])

                # for encomenda in EncomendasParaEntrega[:]:

                #     pesoEncomendas = 0
                #     tempoAux = 0

                #     freguesia = self.m_Clientes[(encomenda.getId_Cliente())].getFreguesia()

                #     if (flag == 1):
                #         caminho = self.escolheCaminho("Health Planet", freguesia)
                #     else:
                #         caminho = self.escolheCaminho(self.m_Clientes[aux[-1][0].getId_Cliente()].getFreguesia(), freguesia)

                #     for encomendas in EncomendasParaEntrega:
                #         pesoEncomendas += float(encomendas.getPeso())

                #     tempo = self.carroCusto(caminho[1],pesoEncomendas)

                #     for entregas in aux:
                #         tempoAux += entregas[1]
                #         tempoAux += 0.10

                #     if ((tempo + tempoAux) <= float(encomenda.getPrazoEntrega())):
                #         aux.append([encomenda,(tempo + tempoAux),caminho])
                #         EncomendasParaEntrega.remove(encomenda)
                #         i = i + 1
                #         flag = 0
                #     else:
                #         listaAux.append([encomenda,0,caminho,i])
                #         EncomendasParaEntrega.remove(encomenda)
                #         i = i + 1

            # print(aux)
            # print('\n')
                    
            # print("ola \n")


            x = self.recalculaTempo(aux,flagVeiculo)

            listaFinal = self.tentaAdicionar(x,listaAux,flagVeiculo)

            # for it in listaFinal:
            #     for e in it[0]:
            #         print(e)
            #     print('\n')
            # print("hello")

            for tuplo in listaFinal:

                idCliente = tuplo[0][0].getId_Cliente()

                idsEncomendas = []

                pesoFinal = 0

                for enco in tuplo[0]:
                    print(enco)
                    idsEncomendas.append((enco.getId_Encomenda()))
                    pesoFinal += float(enco.getPeso())
                    lista.remove(enco)
                print('\n')

                file = open(pasta, 'a+')
                file.seek(0)
                idEntrega = (len(file.readlines())) + 1

                entrega = Entrega(idEntrega,idCliente,estafetaId,None,self.calculaPrecoServico(pesoFinal,flagVeiculo,tuplo[0][0].getPrazoEntrega(),tuplo[2][1]),flagVeiculo,tuplo[2][0],tuplo[2][1],tuplo[1],idsEncomendas,'A*')
                entregasEstafeta.append(entrega)

                # print(entregasEstafeta)

                ordemExpansao = []

                for nodo in tuplo[2][2]:
                    ordemExpansao.append(nodo.getName())

                # print("Ordem de expansão da entrega " + str(idEntrega) + " : " + str(ordemExpansao))
                # print('\n')

                if idCliente not in self.m_Entregas.keys():
                    self.m_Entregas[idCliente] = []

                self.m_Entregas[idCliente].append(entrega)

                file.write(entrega.__str__() + '\n')

                # lista.remove(tuplo[0])

            estafeta.setEntregas(entregasEstafeta)
            ListaEstafetas.remove(estafetaId)
            Veiculos[flagVeiculo - 1] -= 1
            nrVeiculos -= 1


            print("cheguei ao fim!")   

    def Caminhos_Estafetas(self):
        lista_Estafetas = {}
        lista_entregas = []

        for idEstafeta, estafeta in self.m_Estafetas.items():
            if len(estafeta.getEntregas()) != 0:
                lista_Estafetas[idEstafeta] = []
                for entregas in estafeta.getEntregas():
                    lista_entregas.append(entregas)
                    caminho = entregas.getCaminho()
                    for freg in caminho:
                        lista_Estafetas[idEstafeta].append(freg)
                    lista_Estafetas[idEstafeta].append(';')


        return (lista_Estafetas,lista_entregas)

    def getEncomendas(self):
        return self.m_Encomendas
    
    def getEncPendentes(self):
        return self.m_EncPendentes
    
    def getClientes(self):
        return self.m_Clientes
    
    def getEstafetas(self):
        return self.m_Estafetas
    
    def getEntregas(self):
        return self.m_Entregas
    
    def getCaminhoArquivoClientes(self):
        return self.caminho_arquivo_Clientes
    
    def getCaminhoArquivoEstafetas(self):
        return self.caminho_arquivo_Estafetas
    
    def getCaminhoArquivoEncomendas(self):
        return self.caminho_arquivo_Encomendas
    
    def getCaminhoArquivoEncomendasPendentes(self):
        return self.caminho_arquivo_Encomendas_Pendentes
    
    def getCaminhoArquivoVeiculos(self):
        return self.caminho_arquivo_Veiculos
    
    def getCaminhoArquivoEntregas(self):
        return self.caminho_arquivo_Entregas
    


    def clear_terminal(self):
        os.system('clear')