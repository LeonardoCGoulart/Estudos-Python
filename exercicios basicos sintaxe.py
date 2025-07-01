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