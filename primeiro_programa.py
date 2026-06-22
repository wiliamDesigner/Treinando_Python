import random

Nome=(input("Digite o seu nome:"))
ataque=int(input("Digite o valor do seu ataque:"))
inimigo=(input("digite o nome do seu inimigo:"))
ataqueinimigo=random.randint(0,100)
if(ataque>ataqueinimigo):
    print("você derrotou  seu inimigo com uma força de:",ataque)
else:
    print("você foi derrotado com uma força de:",ataqueinimigo)