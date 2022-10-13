caixa= list()
caixap = list()
preresult = list()
resultado = list()
for dados in open('gabarito.txt','r'):
        caixa.append(dados)
for dados in open('provas.txt','r'):
        caixap.append(dados)                    #!!!--          comentario apenas para registrar dúvidas e soluções de problemas                ---!!!

#print(str(caixa)[2:-2])                #não consigo selecionar por caracter: exemplo caixa[2] tive que converter a str.
                                        #print(len(str(caixa)))#23 caracteres        print(len((caixa)))#1 caracteres
for u in caixap:                        #10 caract para os  alunos
        nota = 0
        y = u[11:]                      # u[11:]quero so o gabarito
        #print(u)                       # perdi horas porque o gabarito estava com apenas um itêm e tive que converter a str para o for considerar cada elemento no for
        cont = 0
        for o in y:
                if o == (str(caixa))[2+cont] and not o in "[]';" and not(str(caixa))[2+cont] in "[]';"  :
                        nota += 1       #print('acertou,{}{}{}'.format(cont,o,nota))            apenas para teste de funcionamento
                cont += 1
        result = u[:-1]+' nota:'+str(nota)       #'u' esta dando um pulo e eliminei a ultima caract que provavelmente deve ser \n e... resolveu!
        preresult.append(result)

for b in range(10,-1,-1):                     #criei a logica para ordenar :)
        for a in preresult:
                if b == int((str(a))[-1]):    #int((str(a))[-1]) vai pegar o ultimo dado que é o de acertos  
                        #print(a)                       - so para teste
                        #print(b,((str(a))[-1]))        - so para teste
                        resultado.append(a)
                                        #print(len(resultado)) para confirmar se passou todos alunos
                        #!!!--          a biblioteca os é para trazer funcos de tratamento de arquivo
arquivo = open('resultado.txt','w')
for i in resultado:
        arquivo.write(i+'\n')
arquivo.close()

        
                
        

