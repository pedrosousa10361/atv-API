# Uma empresa precisa calcular a folha de pagamento de N funcionários (N informado pelo usuário). Para
# cada funcionário, leia nome, salário bruto e quantidade de horas extras trabalhadas no mês. Calcule o
# salário líquido seguindo as regras abaixo e exiba um extrato individual. Ao final, mostre o maior e o menor
# salário líquido recebido e o total gasto com a folha. Organize o código em funções. Trate entradas
# inválidas com try/except.
def nome():
     try:
      nome=input('nome do funcionário: ').upper()
      return nome
     except ValueError:
        print('digite um nome adequado')

def salario_liquido():
    name=nome()

    while True:
        try:
            h_trabalho=int(input(f'quantas horas extras o funcionário {name} trabalhou por mês? '))
            bruto=int(input(f'salario bruto do {name}: '))
            break
        except ValueError:
          print('digite um valor adequado')
    h_normal=bruto/220
    h_extra=(h_normal*1.5)*h_trabalho
    vale=0
    if bruto>2000:
             vale=150
    inss=bruto*0.11
    sal_liqui=(bruto+h_extra)-inss-vale
    return sal_liqui, name, bruto, h_extra, inss, vale, h_trabalho
    
    

def folha():
    while True:
     try:
      n=int(input('Quantidade de funcionários: '))
      break
     except:
       print('digite um numero inteiro')
    maior=0
    menor=0
    salario_total=0

    for i in range(n):
      salario, preencher_nome, sal_bruto, horas_extras, aposentadoria, vale_refeiçao, total_horas=salario_liquido()
      salario_total+=salario
      if salario>maior:
         maior=salario
      elif salario<maior:
         salario=menor 
      print(f'{'-'*4}Extrato : {preencher_nome}{'-'*4}' )
      print(f'''Salario Bruto    R$ {sal_bruto:.2f}\nHoras Extras     R$ {horas_extras:.2f} ({total_horas})\nINSS        R$ {aposentadoria:.2f}\nVale refeição     R$  {vale_refeiçao:.2f}\n 
Salario Liquido     R$ {salario:.2f}''')
    print(f'maior salario                R$ {maior:.2f}')
    print(f'menor salario                R$ {menor:.2f}')
    print(f'totall gasto com a folha     R$ {salario_total:.2f}')
      
        
folha()


