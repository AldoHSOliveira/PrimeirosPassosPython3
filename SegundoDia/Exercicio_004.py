#leia algo pelo teclado e mostre o tipo primitivo e todas as informaçoes possiveis sobre ele

dado = input("Digite alguma coisa: ")
print("O tipo primitivo é ", type(dado))
print("Só tem espaço? ", dado.isspace())
print("é um número? ", dado.isnumeric())
print("É alfabetico? ", dado.isalpha())
print("É alfanumérico? ",dado.isalnum())
print("Está em maiuscula? ", dado.isupper())
print("Está em minuscula? ",dado.islower())
print("Está capitalizada, ou seja, maiuscula e minuscula ?", dado.istitle())

