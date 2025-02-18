from Sistema import Sistema

def main():

    sistema = Sistema()
    
    saida = -1
    while saida != 0:
        sistema.clear_terminal()
        print("*--      HEALTH PLANET       --*")
        print("1 - Criar Conta")
        print("2 - Autenticar")
        # print("3 - Teste")
        print("0 - Saír")

        try:
            saida = int(input("\nIntroduza a sua opção: "))

            if saida == 0:
                print("saindo.......")

            elif saida == 1:
                sistema.clear_terminal()

                id = input("Id: ")

                while True:
                    try:

                        freguesia = input("Freguesia: ")

                        if not freguesia.isalpha():
                            raise ValueError("Entrada inválida. Por favor, digite apenas caracteres.")

                        verifica = sistema.g.verification(freguesia)

                        if verifica == None:
                            raise ValueError("Não fazemos entregas para a sua freguesia ou a freguesia não existe!")
                        else:
                            break

                    except ValueError as e:
                        print(e)
                        print('\n')

                while True:
                    try:

                        nome = input("Nome: ")

                        if not nome.isalpha():
                            raise ValueError("Entrada inválida. Por favor, digite apenas caracteres!")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        print('\n')

                password = input("Password: ")

                if not(sistema.create_Account(id,freguesia,nome,password)):
                    print("Cliente já existe!")
                    saida = 7

                l = input("prima enter para continuar")

            elif saida == 2:
                sistema.clear_terminal()

                id = input("Id: ")

                password = input("Password: ")

                if id == "rafa" and password == "123":
                     menuAdmin(sistema)
                     saida = -1

                elif(sistema.autentication(id, password)):
                    print("Ok!")
                    menuCliente(sistema, id)
                    saida = -1

                else: print("Erro!")

            else:
                print("Digite um dos nº mostrados na tela!")
                l = input("prima enter para continuar")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            l = input("prima enter para continuar")

def menuAlgoritmos(sistema):
    saida = -1
    while saida != 0:
        sistema.clear_terminal()
        print("*--      HEALTH PLANET       --*")
        print("1 - DFS")
        print("2 - BFS")
        print("3 - Uniforme")
        print("4 - A*")
        print("5 - Gulosa")
        print("0 - Voltar Atras")

        try:

            saida = int(input("introduza a sua opcao-> "))

            if saida == 0: break

            elif saida == 1:
                n1 = input("Nodo inicial-> ")
                n2 = input("Nodo final-> ")
                inicio = sistema.g.verification(n1)
                fim = sistema.g.verification(n2)
                print('\n')
                print("1 - Ordem de expansão")
                print("2 - Resultado")
                opcao = int(input("Introduza opçao: "))
                if opcao == 1:
                    lista = []
                    result = sistema.g.procura_DFS(inicio,fim, path=[], visited=set())
                    for info in result[2]:
                        lista.append(info.getName())
                    print(lista)
                else:
                    result = sistema.g.procura_DFS(inicio,fim, path=[], visited=set())
                    sistema.g.printPath(result[0])
                l = input("prima enter para continuar")

            elif saida == 2:
                n1 = input("Nodo inicial->")
                n2 = input("Nodo final->")
                inicio = sistema.g.verification(n1)
                fim = sistema.g.verification(n2)
                print('\n')
                print("1 - Ordem de expansão")
                print("2 - Resultado")
                opcao = int(input("Introduza opçao: "))
                if opcao == 1:
                    lista = []
                    result = sistema.g.procura_BFS(inicio,fim)
                    for info in result[2]:
                        lista.append(info.getName())
                    print(lista)
                else:
                    result = sistema.g.procura_BFS(inicio,fim)
                    sistema.g.printPath(result[0])
                l = input("prima enter para continuar")
                
            elif saida == 3:
                n1 = input("Nodo inicial->")
                n2 = input("Nodo final->")
                inicio = sistema.g.verification(n1)
                fim = sistema.g.verification(n2)
                print('\n')
                print("1 - Ordem de expansão")
                print("2 - Resultado")
                opcao = int(input("Introduza opçao: "))
                if opcao == 1:
                    lista = []
                    result = sistema.g.uniform_cost(inicio,fim)
                    for info in result[2]:
                        lista.append(info.getName())
                    print(lista)
                else:
                    result = sistema.g.uniform_cost(inicio,fim)
                    sistema.g.printPath(result[0])
                l = input("prima enter para continuar")

            elif saida == 4:
                n1 = input("Nodo inicial->")
                n2 = input("Nodo final->")
                inicio = sistema.g.verification(n1)
                fim = sistema.g.verification(n2)
                print('\n')
                print("1 - Ordem de expansão")
                print("2 - Resultado")
                opcao = int(input("Introduza opçao: "))
                if opcao == 1:
                    lista = []
                    sistema.g.add_all_heuristica(fim)
                    result = sistema.g.procura_aStar(inicio, fim)
                    for info in result[2]:
                        lista.append(info.getName())
                    print(lista)
                else:
                    sistema.g.add_all_heuristica(fim)
                    result = sistema.g.procura_aStar(inicio, fim)
                    sistema.g.printPath(result[0])
                l = input("prima enter para continuar")

            elif saida == 5:
                n1 = input("Nodo inicial->")
                n2 = input("Nodo final->")
                inicio = sistema.g.verification(n1)
                fim = sistema.g.verification(n2)
                print('\n')
                print("1 - Ordem de expansão")
                print("2 - Resultado")
                opcao = int(input("Introduza opçao: "))
                if opcao == 1:
                    lista = []
                    sistema.g.add_all_heuristica(fim)
                    result = sistema.g.greedy(inicio,fim)
                    for info in result[2]:
                        lista.append(info.getName())
                    print(lista)
                else:
                    sistema.g.add_all_heuristica(fim)
                    result = sistema.g.greedy(inicio,fim)
                    sistema.g.printPath(result[0])
                l = input("prima enter para continuar")

            else:
                print("Digite um dos nº mostrados na tela!")
                l = input("prima enter para continuar")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            l = input("prima enter para continuar")


def menuAuxiliar(sistema):
    saida = -1
    while saida != 0:
     sistema.clear_terminal()
     print("*--      HEALTH PLANET       --*")
     print("1 - Desenhar Grafo")
     print("2 - Algoritmos")
     print("3 - Heuristica")
     print("0 - Voltar Atras")

     try:

        saida = int(input("introduza a sua opcao-> "))

        if saida == 0: break

        elif saida == 1:
            sistema.g.desenha()

        elif saida == 2:
               menuAlgoritmos(sistema)
               saida = -1

        elif saida == 3:
               n1 = input("Nodo final->")
               fim = sistema.g.verification(n1)
               sistema.g.desenhaComHeuristica(fim)
               l = input("prima enter para continuar")

        else:
            print("Digite um dos nº mostrados na tela!")
            l = input("prima enter para continuar")

     except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        l = input("prima enter para continuar")
         

def menuCliente(sistema, id_cliente):
    saida = -1
    while saida != 0:
     sistema.clear_terminal()
     print("*--      HEALTH PLANET       --*")
     print("1 - Ver Perfil")
     print("2 - Criar Encomenda")
     print("3 - Lista de Encomendas")
     print("4 - Lista de Entregas")
     print("0 - Voltar Atras")

     try:
 
        saida = int(input("\nIntroduza a sua opção-> "))

        if saida == 0: break

        elif saida == 1:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")
                sistema.viewProfile(id_cliente)
                l = input("Prima enter para continuar")

        elif saida == 2:
               
               sistema.clear_terminal()
               sistema.createEncomenda(id_cliente)
               l = input("prima enter para continuar")

        elif saida == 3:
               
               sistema.clear_terminal()
               print("*--      HEALTH PLANET       --*\n")
               
               sistema.lista_Encomendas_Cliente(id_cliente)

               # lista = sistema.listarEncomendasSemEntrega(id_cliente)
               # for encomenda in lista:
               #      print('\n')
               #      print(encomenda)

               print("Deseja escolher alguma encomenda para entrega?\n")

               print("1 - SIM")
               print("2 - NÃO\n")

               while True:
                   try:

                        opcao = input("Introduza a sua opção: ")

                        if int(opcao) == 1:
                        
                             print("1 - IMEDIATO")
                             print("2 - NÃO IMEDIATO\n")

                             while True:
                                 try:

                                    escolha = input("Introduza a sua opção de urgência da sua entrega: ")

                                    if int(escolha) == 1:
                                         
                                         while True:
                                             try:
                                    
                                                id = input("Introduza o id da sua encomenda (Ou ids se quiser mais do que uma encomenda, nesse caso separe os ids por vírgulas): ")

                                                teste = id.split(',')

                                                ids = []

                                                for enc in sistema.m_Encomendas[id_cliente]:
                                                    ids.append(enc.getId_Encomenda())

                                                for i in teste:
                                                    if i.isdigit():
                                                        if int(i) not in ids:
                                                            raise ValueError("Introduza ids de encomendas que existam na sua lista!")
                                                    else:
                                                        raise ValueError("Introduza digitos!")
                                                    
                                                break
                                             
                                             except ValueError as e:
                                                 print(e)
                                                 print('\n')
                                             
                                         result = sistema.createEntregaEncomendas(id_cliente,id)

                                         if result != None:
                                              
                                              entrega = result[0]

                                              caminho = entrega.getCaminho()

                                              sistema.g.desenhaCaminhoAnimacao(caminho,entrega.getEstafeta(),entrega.getPreco(),entrega.getVeiculo(),entrega.getTempoPrevisto(),entrega.getAlgoritmo())

                                              print("Ordem de Expansão: " + str(result[1]) + '\n')

                                              sistema.entregaRealizada(entrega,id_cliente)

                                              entrega.strFormat()

                                              l = input("prima enter para continuar")
                                              break

                                         else:
                                              l = input("prima enter para continuar")
                                              break

                                    elif int(escolha) == 2:
                                    
                                         while True:
                                             try:
                                    
                                                id = input("Introduza o id da sua encomenda (Ou ids se quiser mais do que uma encomenda, nesse caso separe os ids por vírgulas): ")

                                                teste = id.split(',')

                                                ids = []

                                                for enc in sistema.m_Encomendas[id_cliente]:
                                                    ids.append(enc.getId_Encomenda())

                                                for i in teste:
                                                    if i.isdigit():
                                                        if int(i) not in ids:
                                                            raise ValueError("Introduza ids de encomendas que existam na sua lista!")
                                                    else:
                                                        raise ValueError("Introduza digitos!")
                                                    
                                                break
                                             
                                             except ValueError as e:
                                                 print(e)
                                                 print('\n')

                                         result = sistema.guardaEncomendas(id_cliente,id)

                                         if result == True:
                                           print("Encomendas guardadas na lista de pendentes.")

                                           l = input("prima enter para continuar")
                                           break
                                         
                                         else:
                                           print("Não foi guardado nenhuma encomenda!")

                                           l = input("prima enter para continuar")
                                           break
                                         
                                    else:
                                        print("Digite um dos nº mostrados na tela!")
                                        print('\n')

                                 except ValueError:
                                     print("Entrada inválida. Por favor, digite um número válido.")
                                     print('\n')
                        
                        elif int(opcao) == 2:
                            break

                        else:
                            print("Digite um dos nº mostrados na tela!")
                            print('\n')

                   except ValueError:
                       print("Entrada inválida. Por favor, digite um número válido.")
                       print('\n')

                   break
                       
                
        elif saida == 4:
             sistema.clear_terminal()
             print("*--      HEALTH PLANET       --*\n")


             lista = sistema.lista_Entregas_Cliente(id_cliente)

             if len(lista) == 0:
                  print("Não possui entregas!")
                  l = input("prima enter para continuar")

             else:

               for entrega in lista:
                    entrega.strFormat()
                    print('\n')

               print("Deseja classificar alguma Entrega?\n")

               print("1 - SIM")
               print("2 - NÃO")

               while True:
                   try:

                        opcao = input("Introduza a sua opção: ")

                        if int(opcao) == 1:
                          
                          while True:
                              try:
                        
                                escolha = int(input("Introduza o nrº da entrega que deseja classificar: "))

                                ids = []

                                for entreg in sistema.m_Entregas[id_cliente]:
                                    ids.append(entreg.getId())

                                if escolha not in ids:
                                    raise SystemError("Introduza um nrº da entrega da sua lista!")
                                
                                else:
                                    break

                              except SyntaxError as e:
                                  print(e)
                                  print('\n')

                              except ValueError:
                                print("Entrada inválida. Por favor, digite um número válido.")
                                print('\n')


                          sistema.classificaEntrega(lista,escolha)
                          l = input("prima enter para continuar")
                          break

                        elif int(opcao) == 2:
                            break

                        else:
                            print("Digite um dos nº mostrados na tela!")
                            print('\n')

                   except ValueError:
                       print("1")
                       print("Entrada inválida. Por favor, digite um número válido.")
                       print('\n')
                       
        else:
            print("Digite um dos nº mostrados na tela!")
            print('\n')

     except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        print('\n')

def menuAdmin(sistema):
    saida = -1
    while saida != 0:
        sistema.clear_terminal()
        print("*--      HEALTH PLANET       --*\n")
        print("1 - Ver Clientes registados no Sistema")
        print("2 - Ver Estafetas registados no Sistema")
        print("3 - Ver Veiculos registados no Sistema")
        print("4 - Adicionar Estafeta")
        print("5 - Adicionar Veículo")
        print("6 - Ver Encomendas do Sistema")
        print("7 - Ver Entregas Concluídas do Sistema")
        print("8 - Lançar Encomendas Pendentes")
        print("9 - Ranking dos Estafetas Classificação")
        print("10 - Ranking dos Estafetas Ecológicos")
        print("11 - Menu Auxiliar")
        print("0 - Voltar Atrás")

        try:

            saida = int(input("\nIntroduza a sua opção-> "))

            if saida == 0: break

            elif saida == 1:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")
                file = open(sistema.getCaminhoArquivoClientes(), 'r')
                listaClientes = file.readlines()
                i = 1
                for linha in listaClientes:
                     print(i,"-",linha)
                     i = i+1

                l = input("Prima enter para continuar") 
                saida = -1

            elif saida == 2:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")
                file = open(sistema.getCaminhoArquivoEstafetas(), 'r')
                listaEstafetas = file.readlines()
                i = 1
                for linha in listaEstafetas:
                     print(i,"-",linha)
                     i = i+1

                l = input("Prima enter para continuar") 
                saida = -1

            elif saida == 3:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")

                v1 = 0
                v2 = 0
                v3 = 0

                listaVeiculos = sistema.m_Veiculos

                for c in listaVeiculos:
                    if c == 1:
                        v1 = v1 + 1
                    elif c == 2:
                        v2 = v2 + 1
                    else: v3 = v3 +1

                print("VEÍCULOS DISPONÍVEIS:")
                print("Bicicleta -> ", v1)
                print("Mota -> ", v2)
                print("Carro -> ", v3)

                l = input("\nPrima enter para continuar") 
                saida = -1
    
            elif saida == 4:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")
                print("ADICIONAR ESTAFETA:")
                id = input("Id: ")

                while True:
                    try:

                        nome = input("Nome: ")

                        if not nome.isalpha():
                            raise SystemError("Entrada inválida. Por favor, digite apenas caracteres!")
                        
                        else:
                            break

                    except SystemError as e:
                        print(e)
                        print('\n')

                if not(sistema.create_Estafeta(id,nome)):
                    print("Estafeta já existe!")

                l = input("prima enter para continuar")
                saida = -1

            elif saida == 5:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")
                print("ADICIONAR VEÍCULO:")
                print("1 -> Bicicleta")
                print("2 -> Mota")
                print("3 -> Carro")

                while True:
                    try:

                        n = int(input("\nIntroduza o dígito correspondente ao veículo -> "))

                        if (n == 1) or (n == 2) or (n == 3):
                            break

                        else:
                            print("Digite um dos nº mostrados na tela!")
                            print('\n')
                            
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número válido.")
                        print('\n')

                sistema.create_Veiculo(n)

                l = input("prima enter para continuar")
                saida = -1

            elif saida == 6:
                i = 1
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")

                print("1 - Visualizar Encomendas de um Cliente")
                print("0 - Voltar Atrás")

                while True:
                    try:
                
                        saida = int(input("\nIntroduza a sua opção -> "))

                        if (saida == 0):
                             saida = -1
                             break
                         
                        elif saida == 1:
                        
                            sistema.clear_terminal()

                            print("UTILIZADORES:")
                            for id in sistema.m_Clientes.keys():
                                print("->", id)
                                i = i+1

                            while True:
                                try:

                                    id = input("\nIntroduza o id do cliente que pretende visualizar -> ")

                                    if id not in sistema.m_Clientes.keys():
                                        raise SystemError("Introduza um dos ids dos clientes mostrados na tela!")
                                    
                                    else:
                                        break

                                except SystemError as e:
                                    print(e)
                                    print('\n')

                            sistema.clear_terminal()
                            print("*--      HEALTH PLANET       --*\n")

                            if id in sistema.m_Encomendas.keys():
                                lista_encomendas_cliente = sistema.m_Encomendas[id]
                                for enc in lista_encomendas_cliente:
                                    # if int(enc.getEstado()) == 1:
                                    print(str(enc) + '\n')

                                l = input("prima enter para continuar")
                                saida = -1

                            else:
                                print('ERRO!!')
                                l = input("prima enter para continuar")
                                saida = -1

                        else:
                            print("Digite um dos nº mostrados na tela!")
                            print('\n')

                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número válido.")
                        print('\n')

                    break

            elif saida == 7:
                i = 1
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")
                '''
                for id in sistema.m_Clientes.keys():
                    print(i," - ", id)
                '''

                print("1 - Visualizar Entregas de um Cliente")
                print("2 - Visualizar Entregas de um Estafeta")
                print("0 - Voltar Atrás")

                while True:
                    try:

                        saida = int(input("\nIntroduza a sua opção -> "))

                        if (saida == 0):
                             saida = -1
                             break
                         
                        elif saida == 1:
                            sistema.clear_terminal()

                            print("UTILIZADORES:")
                            for id in sistema.m_Clientes.keys():
                                print("->", id)

                            while True:
                                try:

                                    id = input("\nIntroduza o id do cliente que pretende visualizar -> ")

                                    if id not in sistema.m_Clientes.keys():
                                        raise SystemError("Introduza um dos ids dos clientes mostrados na tela!")
                                    
                                    else:
                                        break

                                except SystemError as e:
                                    print(e)
                                    print('\n')

                            sistema.clear_terminal()
                            print("*--      HEALTH PLANET       --*\n")

                            if id in sistema.m_Entregas.keys():
                                lista_entregas_cliente = sistema.m_Entregas[id]
                                for ent in lista_entregas_cliente:
                                    ent.strFormat()
                                    print('\n')

                                l = input("prima enter para continuar")
                                break
                                # saida = -1

                            else:
                                print('ERRO!!')
                                l = input("prima enter para continuar")
                                saida = -1
                                break
                            
                        elif saida == 2:
                            sistema.clear_terminal()

                            print("ESTAFETAS:")
                            for id in sistema.m_Estafetas.keys():
                                print("->", id)

                            while True:
                                try:

                                    id = input("\nIntroduza o id do estafeta que pretende visualizar -> ")

                                    if id not in sistema.m_Estafetas.keys():
                                        raise SystemError("Introduza um dos ids dos estafetas mostrados na tela!")
                                    
                                    else:
                                        break

                                except SystemError as e:
                                    print(e)
                                    print('\n')

                            sistema.clear_terminal()
                            print("*--      HEALTH PLANET       --*\n")

                            if id in sistema.m_Estafetas:
                                for ent in sistema.m_Entregas.values():
                                     for e in ent:
                                          if id == e.getEstafeta():
                                               e.strFormat()
                                               print('\n')
                                l = input("prima enter para continuar")
                                break
                                # saida = -1

                            else:
                                print('ERRO!!')
                                l = input("prima enter para continuar")
                                saida = -1
                                break
                            
                        else:
                            print("Digite um dos nº mostrados na tela!")
                            print('\n')
                    
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número válido.")
                        print('\n')


            elif saida == 8:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")

                lista = sistema.organizaListaHeuristica()

                # print('fiz')

                if (len(lista) == 0):
                    print("Vazio!")
                    l = input("prima enter para continuar")

                else:
                    # print('fiz')
                    sistema.createEntregaEncPend(lista,sistema.getCaminhoArquivoEntregas())

                    # print('fiz')

                    teste = sistema.Caminhos_Estafetas()

                    sistema.g.desenhaVariosCaminhosAnimacao(teste[0])

                    for entrega in teste[1]:
                        print('*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*')
                        entrega.strFormat()
                        print('\n')
                        sistema.entregaRealizada(entrega,entrega.getCliente())
                        

                    l = input("prima enter para continuar")

            elif saida == 9:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")

                lista = sistema.lista_Estafetas_Classificacao()

                lisa_ordenada = sorted(lista.items(), key=lambda x: x[1], reverse=True)

                i = 0

                print("RANKING:")
                print('\n')
                for estafeta, media in lisa_ordenada:
                    i = i + 1
                    print(str(i) + " -> " + str(estafeta) + ", " + str(media) + "⭐️")
                print('\n')
                l = input("prima enter para continuar")

            elif saida == 10:
                sistema.clear_terminal()
                print("*--      HEALTH PLANET       --*\n")

                sistema.ranking_Estafetas_Ecológicos()
                l = input("prima enter para continuar")

            elif saida == 11:
                menuAuxiliar(sistema)

            else:
                print("Digite um dos nº mostrados na tela!")
                l = input("prima enter para continuar")

        except ValueError:
            print('aqui')
            print("Entrada inválida. Por favor, digite um número válido.")
            l = input("prima enter para continuar")



if __name__ == "__main__":
    main()