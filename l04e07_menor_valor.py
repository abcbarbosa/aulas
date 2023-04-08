"""            Comentários de várias linhas.
   CEUB   -   FATECS   -   BCC   -   ADS   -   Programação   -   Prof. Barbosa
Atalhos: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

Monitoria (dúvidas, de segunda a sexta). Asa Norte: lab. 8202, das 17h30 às 19h
                                         Taguatinga: lab. 174, das 11h às 12h30

- Construa o programa que encontre o menor valor de um conjunto de valores
inteiros digitados pelo usuário. Use o valor 0 (zero) na condição de saída
que não será considerado na pesquisa.

- Ideia (lógica) pra resolver o problema:
Preciso de quantas variáveis?

(variáveis)     Tempo1          Tempo2      Tempo3      Tempo4      Tempo5
valor (input)                   2           3           1           0
menor_valor     9999999999      2           -           1

- Dicas (algoritmo):
variável menor_valor        (inicia a variável)
estrutura de repetição
    lê numero
    testa condição saída
    compara o valor lido (numero) com o menor valor
    atualiza ou não o menor valor
Tela de saída               (fim do algoritmo)
Teste 1: Entrada: valor: 2, 3, 1, 0   Saída: Menor = 1
Teste 2: Entrada: valor: 1, 3, 2, 0   Saída: Menor = 1
Teste 3: Entrada: valor: 3, 2, 1, 0   Saída: Menor = 1
Teste 4: Entrada: valor: 0            Saída: Não foi digitado nenhum número. """
menor_valor = 99999999                  # Valor inicial da variável menor_valor
# menor_valor = float('inf')            # O maior valor possível no Python
print('Digite [0] para sair')           # Executa uma vez
while True:                             # Passa várias vezes
    valor = int(input("Digite um valor: "))     # Recebe um valor
    if valor == 0:                      # Se o valor for igual a zero
        break                           # O laço encerra, saí do while.
    if valor < menor_valor:
        menor_valor = valor             # Atualiza a variável menor_valor.
    # Fim da estrutura de repetição (while).
print("O menor valor é", menor_valor)   # Executa uma vez
''' ----- ALTERAÇÕES:
a. Mostre também a quantidade de valores foram digitado, no final.
b. Mostre a soma dos valoes digitados.         
c. Digite a codição de saída de primeira. Mostre a msg: 
   "Não foi digitado nenhum valor."
    ----- DICA ABAIXO:
ct = 0                                           # Antes do while            # a.
ct = ct + 1                                      # Dentro do while, no final
print ('Quantidade de valores digitados: ', ct)  # Depois do while               
soma = 0                                         # Antes do while            # b.
soma = soma + valor                              # Dentro do while
print ('Soma dos valores digitados: ', soma)     # Depois do while      
...                                      # No final, depois do fim do while  # c.
if ct == 0:                                 
    print("Não foi digitado nenhum valor.")
else:
    print("O menor valor é: ", menor_valor)                                    
    print ('Quantidade de valores digitados: ', ct)      
    print ('Soma dos valores digitados: ', soma)   

-----

- Solução 2:

menor, cont = 0, 0
while True:
    num = int(input('insira um número ou [0] para sair]: '))
    if num == 0:
        break
    cont += 1
    if cont == 1:
        menor = num
    else:
        if num < menor:
            menor = num
print(f'{cont} valores foram digitados')
if cont == 1:
    print('nenhuma valor digitado')
else:
    print(f'o menor valor digitado foi {menor}')

'''
