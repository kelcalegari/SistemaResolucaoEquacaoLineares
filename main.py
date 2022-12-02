def GaussJacob (A, b, vetorSolution, nInteracoes):
    print("GaussJacob")
    interacao = 0 

    #Criando vetores temporário e para salvar os deltas e erros de cada variável
    vetorTemp=[]
    vetorDelta = []
    vetorErro = []

    # Iniciando vetores com 0 de acordo com o tamanho do vetor
    for i in range(len(vetorSolution)):
        vetorTemp.append(0)
        vetorDelta.append(0)
        vetorErro.append(0)

    #Laço para repetir conforme o numero de repetições desejado
    while interacao<nInteracoes:

        #Salva o resultado anterior
        for k in range(len(vetorSolution)):
                vetorTemp[k] = vetorSolution[k]
        
        #For das linhas da matriz
        for i in range(len(A)):
            #Pega o valor 'depois do igual'
            vetorSolution[i]=b[i]
            #For das colunas da matriz
            for j in range(len(A)):
                #Se não for a diagonal principal, troca o sinal e soma 
                if i!=j:
                    vetorSolution[i] -=A[i][j]*(vetorTemp[j])
            #Divide a soma da linha com o valor da diagonal
            vetorSolution[i] = vetorSolution[i]/A[i][i]
        
            
        # Calculando o erro e o delta para cada variavel
        for e in range(len(vetorSolution)):
            vetorDelta[e] = abs(vetorSolution[e]-vetorTemp[e])
            if(vetorSolution[e]!=0):
                vetorErro[e] = abs(vetorDelta[e]/vetorSolution[e])*100
            else:
                vetorErro[e] = 100
        
        print(" ", interacao, " - Vetor Solução = ", vetorSolution, " - Delta = ", vetorDelta, " - Erro ", vetorErro)
        interacao+=1

    print("Final com ", interacao, " interações - Vetor Solução = ", vetorSolution, " - Delta = ", vetorDelta, " - Erro ", vetorErro)

def GaussSeidel (A, b, vetorSolution, nInteracoes):
    print("GaussSeidel")
    interacao = 0

    #Criando vetores temporário e para salvar os deltas e erros de cada variável
    vetorTemp=[]
    vetorDelta = []
    vetorErro = []

    # Iniciando vetores com 0 de acordo com o tamanho do vetor
    for i in range(len(vetorSolution)):
        vetorTemp.append(0)
        vetorDelta.append(0)
        vetorErro.append(0)

    #Laço para repetir conforme o numero de repetições desejado
    while interacao<nInteracoes:

        #Salva o resultado anterior
        for k in range(len(vetorSolution)):
                vetorTemp[k] = vetorSolution[k]
        
        #For das linhas da matriz
        for i in range(len(A)):
            #Pega o valor 'depois do igual'
            vetorSolution[i]=b[i]
            #For das colunas da matriz
            for j in range(len(A)):
                #Se não for a diagonal principal, troca o sinal e soma 
                if i!=j:
                    #GaussSeidel utiliza as variáveis atualizadas
                    vetorSolution[i] -=A[i][j]*(vetorSolution[j])
            #Divide a soma da linha com o valor da diagonal
            vetorSolution[i] = vetorSolution[i]/A[i][i]
        
        # Calculando o erro e o delta para cada variavel
        for e in range(len(vetorSolution)):
            vetorDelta[e] = abs(vetorSolution[e]-vetorTemp[e])
            if(vetorSolution[e]!=0):
                vetorErro[e] = abs(vetorDelta[e]/vetorSolution[e])*100
            else:
                vetorErro[e] = 100
        print(" ", interacao, " - Vetor Solução = ", vetorSolution, " - Delta = ", vetorDelta, " - Erro ", vetorErro)
        interacao+=1
    print("Final com ", interacao, " interações - Vetor Solução = ", vetorSolution, " - Delta = ", vetorDelta, " - Erro ", vetorErro)

def criterioDasLinhas (A):
    print("criterioDasLinhas")
    coeficiente = []
    # For das linhas da matriz
    for i in range(len(A)):
        #Inicia a soma com 0
        b = 0
        # For das colunas
        for j in range(len(A)):
            # Se não for a diagonal soma-se
            if i!=j:
                b +=A[i][j]
        # Divide a soma com a diagonal da linha
        b/= A[i][i]
        #Salva o resultado da linha no vetor
        coeficiente.append(b)    
    
    print(coeficiente)

    # Pega o maior coeficiente do vetor e verifica se é menor que 1 e imprime o resultado
    if (max(coeficiente)<1):
        print("Com coeficiente de", max(coeficiente), "sendo menor que 1, gera uma sequencia convergente no GaussJacob")
    else:
        print("Com coeficiente de", max(coeficiente), "sendo maior que 1, não gera uma sequencia convergente no GaussJacob")

def Sassenfeld (A):
    coeficiente = []
    # For das linhas da matriz
    for i in range(len(A)):
        #Inicia a soma com 0
        b = 0
        # For das colunas
        for j in range(len(A)):
            
            # Se for os números a cima da diagonal principal soma-se
            if (i!=j and i ==0) or i<j:
                b +=A[i][j]
            
            # Se for os números a baixo da diagonal principal soma-se e multiplica com o coeficiente da coluna respectiva 
            elif i != j and i!=0:
                b +=A[i][j]*coeficiente[j]
        
        #Divide a soma com a diagonal
        b/= A[i][i]
        coeficiente.append(b) 
    print(coeficiente)  
        
    # Pega o maior coeficiente do vetor e verifica se é menor que 1 e imprime o resultado
    if (max(coeficiente)<1):
        print("Com coeficiente de", max(coeficiente), "sendo menor que 1, gera uma sequencia convergente no Gauss-Seidel")
    else:
        print("Com coeficiente de", max(coeficiente), "sendo maior que 1, não gera uma sequencia convergente no Gauss-Seidel")

   

matrix = [[-4,1,1,0],[1,-4,0,1],[1,0,-4,1],[0,1,1,-4]]
b = [-175,-75,-125,-25]
Ninteracao = 55
criterioDasLinhas(matrix)
GaussJacob(matrix,b,[0,0,0,0],Ninteracao)
Sassenfeld(matrix)
GaussSeidel(matrix,b,[0,0,0,0],Ninteracao)

