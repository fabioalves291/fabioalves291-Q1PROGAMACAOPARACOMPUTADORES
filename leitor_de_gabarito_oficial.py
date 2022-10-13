caixa= list()
caixap = list()
preresult = list()
resultado = list()
for dados in open('gabarito.txt','r'):
        caixa.append(dados)
for dados in open('provas.txt','r'):
        caixap.append(dados)                
                                                       
for gabdalunos in caixap:                       
        y = gabdalunos[11:] 
        nota = 0                                           
        cont = 0
        for gab in y: 
                if gab == (str(caixa))[2+cont] and not gab in "[]';" and not(str(caixa))[2+cont] in "[]';"  :
                        nota += 1       
                cont += 1
        result = gabdalunos[:-1]+' nota:'+str(nota)  #aqui tem horas que o a nota desce uma linha    
        preresult.append(result)

for nota in range(10,-1,-1):                     
        for a in preresult:
                if nota == int((str(a))[-1]):   
                        resultado.append(a)
                        
arquivo = open('resultado.txt','w')
for i in resultado:
        arquivo.write(i+'\n')
arquivo.close()

        
                
        

