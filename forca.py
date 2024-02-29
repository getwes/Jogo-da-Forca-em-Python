palavra = "python"
letras_usuarios = [""]
chances = 7
ganhou = False

while True:
    # criando a logica
    for letra in palavra:
        if letra.lower() in letras_usuarios:
            print(letra, end="")
        else:
            print("_", end="")
    print("")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuarios.append(tentativa.lower())
    break 



if ganhou:
    print(f"parabens, voce ganhou. A palavra era: {palavra}")

else:
    print(f"voce perdeu!. A palavra era: {palavra}")