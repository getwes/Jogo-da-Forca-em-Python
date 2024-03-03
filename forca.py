##importando palavra de um outro aquivo palavraforca.py
from palavraforca import palavra
#palavra = "python"
letras_usuarios = [""]
chances = 4
ganhou = False

while True:
    # criando a logica
    for letra in palavra:
        if letra.lower() in letras_usuarios:
            print(letra, end="")
        else:
            print("_", end="")
    print(f"voce tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuarios.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1


    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuarios:
            ganhou = False



    if chances == 0 or ganhou:
    
     break 



if ganhou:
    print(f"parabens, voce ganhou. A palavra era: {palavra}")

else:
    print(f"voce perdeu!. A palavra era: {palavra}")