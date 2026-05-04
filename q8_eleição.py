# Uma urna eletrônica simplificada recebe votos para até 4 candidatos (identificados pelos números 1 a
# 4), além de voto branco (0) e voto nulo (5). Bote opções para Votar, Ver Resultado, Encerrar. No
# Resultado exiba: total de votos válidos, brancos e nulos; percentual de cada candidato sobre os votos
# válidos; e o(s) vencedor(es) — podendo haver empate. Caso nenhuma candidato atinja mais de 50% dos
# votos mostre que deverá ter segundo-turno. Organize o código em funções.
from ulltils import obter_inteiro
def opções():
 print(f'''
Escolha as opções de acordo com seus respectivos números:\n 
1-Votar\n 
2-Ver resultado\n 
3-Encerrar\n\n''')
 while True:
  try:
   escolha=int(input(' '))
   if escolha<4:
    return escolha
  except:
   print('digite uma escolha válida')



def eleições ():
 print(f'-'*4, 'urna eletrônica', '-'*4)
 validos=0
 resposta='S'
 candidato01=0
 candidato02=0
 candidato03=0
 candidato04=0
 nulo=0
 branco=0
 menu='N'
 
 while True:
    escolha=opções()

    if escolha==1:
            print('''\n Voto em Branco-0\n
                Voto Candidato um-1\n
                Voto Candidato dois-2\n
                Voto Candidato três-3\n
                Voto Candidato quatro-4\n
                Voto Nulo-5''')
            while resposta=='S':
             candidato=int(input('voto candidato: '))
             resposta=input('Você deseja votar mais uma vez ? (S/N)').upper()
             
             if candidato==0:
                 validos+=1
                 branco+=1
             elif candidato==1:
                validos+=1
                candidato01+=1
             elif candidato==2:
                validos+=1
                candidato02+=1
             elif candidato==3:
                validos+=1
                candidato03+=1
             elif candidato==4:
                validos+=1
                candidato04+=1
             elif candidato==5:
                nulo+=1   
             else:
                print('Esse candidato não consta no sistema')
        
             
    elif escolha==2:
     if candidato01> candidato02 and candidato01>candidato03:
        vencedor='vencedor foi o candidato um'
     elif candidato02> candidato01 and candidato02>candidato03:
        vencedor='vencedor foi o candidato dois'
     elif candidato03> candidato01 and candidato03>candidato02:
        vencedor='vencedor foi o candidato três'
     elif candidato01<(validos/2) and candidato02<(validos/2) and candidato03<(validos/2):
        vencedor='nenhum dos candidatos venceu , haverá um segundo turno'
     else:
       vencedor='não houveram votos'
    
     try:
      per01=(candidato01/validos)*100
      per02=(candidato02/validos)*100
      per03=(candidato03/validos)*100
      print(f'porcentagem de votos candidato 01-{per01:.1f}%\n')
      print(f'porcentagem de votos candidato 02-{per02:.1f}%\n')
      print(f'porcentagem de votos candidato 03-{per03:.1f}%')
     except ZeroDivisionError:
       print('não existem votos suficientes')
      
     print(f'''foram {validos} votos validos\nforam {branco} votos em branco e {nulo} votos nulos\n{vencedor}\n ''')
    
    else:
      break
    menu=input('deseja voltar ao menu ? (S/N)').upper()
    if menu=='S':
      continue
    else:
      break
 

 
eleições()