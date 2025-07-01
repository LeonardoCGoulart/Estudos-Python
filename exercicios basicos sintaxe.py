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
