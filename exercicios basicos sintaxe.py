#EXERCICIO 1:  Manipulação de Strings
#Contar vogais:
frase = "Analise de dados com Python"
# Conte quantas vogais existem na frase
vogais = "aeiouAEIOU"
contador_vogais = sum(1 for letra in frase
                  if
                   letra
                  in
                   vogais
                  )
print(f"Quantidade de vogais na frase: {contador_vogais}")

#EXERICIO 2:
#Inverter uma string

texto = "ciência de dados"
texto_invertido = texto[::-1]
print(f"Texto invertido: {texto_invertido}")

#EXERCICIO 3:
#Nome Formatado
nome = "leonardo goulart"
nome_formatado = nome.title()
print(f"nome formatado: {nome_formatado}")

#EXERCICIO 4:
#substituir palavras 
frase = "Python é dificil"
nova_frase = frase.replace("dificil","fácil")
print(nova_frase)

#EXERCICIO 5:
#manipular listas 
lista_numeros = [10,20,30]
soma = sum(lista_numeros)
print(f"Soma dos números: {soma}")

#EXERCICIO 6:
#filtrar apenas numeros pares
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in lista_numeros if num% 2 == 0]
print(f"Números pares: {numeros_pares}")

#EXERCICIO 7:
#remover duplicatas

dados_duplicados = [1,2,2,3,4,3]
dados_sem_duplicar = list(set(dados_duplicados))
print("dados sem duplicar: ")
print(dados_sem_duplicar)

#EXERCICIO 8:
#Ordenar e inverter a lista
valores = [3, 9, 1, 7, 2]
valores.sort() #ordena
valores.reverse() #inverte
print("lista ordenada e invertida")
print(valores)

#EXERCICIO 9:
#Manipulação de Dicionários - Criar dicionário de notas
alunos = ["joão", "maria", "pedro"]
notas = [7.5, 8.0, 10.0]
alunos_formatados = [alunos.title() for alunos in alunos]
notas_dict = dict(zip(alunos_formatados,notas))
print(notas_dict)

#EXERCICIO 10:
#Atualizar valor do dicionário
estoque ={"banana" : 1, "maça" : 3}
estoque["banana"] += 2
print(f"estoque: {estoque}")

#EXERCICIO 11:
#Remover valor do dicionário

frutas = {"morango" : 1, "laranja" : 3, "abacaxi" : 2}
frutas.pop("laranja")
print(frutas)

#EXERCICIO 12:
#listar todas as chaves e valores
pessoa = {"nome": "Lucas", "idade": 30, "cidade": "São Paulo"}
print("chaves", list(pessoa.keys()))
print("valores", list(pessoa.values()))

#EXERCICIO 12:
#Mini Desafio com Pandas (nível iniciante) -cxPraticar a criação de um DataFrame e algumas operações básicas.
import pandas as pd

# Crie um DataFrame com os dados abaixo
dados = {
    "Nome": ["Ana", "Leo", "Rafael"],
    "Idade": [21, 23, 16],
    "Salario": [2000,50000,3600]
}

df = pd.DataFrame(dados)

# 1. Mostre as 2 primeiras linhas
# 2. Mostre a média de salário
# 3. Filtre pessoas com salário maior que 3000
# 4. Adicione uma nova coluna "Bonificação" com 10% do salário
print(df)

print("Mostre as 2 primeiras linhas:")
print(df.head(2))

print("media salario:")
media_salario = df["Salario"].mean() 
print(media_salario)

print("pessoas com salario > 3000")
maior_3000 = df[df["Salario"]>3000]
print(maior_3000)

print("nova coluna bonificacao com 10% do salario")
df["Bonificacao"] = df["Salario"] * 0.10
print(df)
