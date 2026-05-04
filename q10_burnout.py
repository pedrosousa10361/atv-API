def obter_respostas():
    while True:
     try:
        n=int(input('quantidade de entrevistados: '))
        break
     except ValueError:
        print('valor invalido, tente novamente')
    
    for i in range(n):
       print(f'''Responda as perguntas abaixo para responder à dimensão exaustão emocionalde acordo com a escala\n
       0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n
       4 = Frequentemente 5 = Quase sempre 6 = Sempre\n
       ''')
       while True:
          try:
             q1=int(input('1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho.'))
             q2=int(input('2. Sinto-me esgotado(a) ao final de um dia de estudos/trabalho.'))
             q3=int(input('3. Acordar de manhã e ter que enfrentar mais um dia me causa cansaço.'))
             q4=int(input( '4. Sinto que me tornei mais indiferente com as pessoas ao meu redor.'))
             q5=int(input('5. Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas.'))
             q6=int(input('6. Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas.'))
             q7=int(input('7. Consigo lidar eficazmente com os problemas que surgem no meu dia a dia.'))
             q8=int(input('8. Sinto que estou tendo uma influência positiva na vida das pessoas.'))
             q9=int(input('9. Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas.'))
             if 0 <= q1 <= 6 and 0 <= q2 <= 6 and 0 <= q3 <= 6 and 0 <= q4 <= 6 and 0 <= q5 <= 6 and 0 <= q6 <= 6 and 0 <= q7 <= 6 and 0 <= q8 <= 6 and 0 <= q9 <= 6:
               calcular_scores(q1, q2, q3, q4, q5, q6, q7, q8, q9, i)
               break
             else:
                print('opção invalida')
          except:
             print('digite um numero')
def calcular_scores( q1, q2, q3, q4, q5, q6, q7, q8, q9, i):

   dimensao01=(q1+q2+q3)/3
   dimensao02=(q4+q5+q6)/3
   dimensao03=(q7+q8+q9)/3

   classificar_dimensao( dimensao01, dimensao02, dimensao03, i)

def classificar_dimensao(dimensao01, dimensao02, dimensao03, i):
 if 0<=dimensao01<=2:
    classificaçao1='Baixo ✅'
 elif 2.1<=dimensao01<=3.9:
    classificaçao1='Moderado'
 else:
    classificaçao1='alto 🔴'
   
 if 0<=dimensao02<=2:
    classificaçao2='Baixo✅'
 elif 2.1<=dimensao02<=3.9:
    classificaçao2='Moderado'
 else:
    classificaçao2='alto🔴'

 if 0<=dimensao03<=2:
    classificaçao3='Alto ✅'
 elif 2.1<=dimensao03<=3.9:
    classificaçao3='Moderado'
 else:
    classificaçao3='Baixo🔴'
 exibir_laudo(i, dimensao01, dimensao02, dimensao03, classificaçao1, classificaçao2, classificaçao3, )


def exibir_laudo(i, dimensao01, dimensao02, dimensao03, classificaçao1, classificaçao2, classificaçao3):
   print(f'''
   ========== LAUDO:{i+1}PACIENTE ==========
    Exaustão Emocional : {dimensao01:.2f} → {classificaçao1}
    Despersonalização : {dimensao02:.2f} → {classificaçao2}
    Realização Pessoal : {dimensao03:.2f} → {classificaçao3}''')

obter_respostas()
   
