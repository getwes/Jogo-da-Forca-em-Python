palavra = "python"
letras_usuarios = []
chances = 7
ganhou = False

while True:
    # criando a logica
    for letra in palavra:
        if letra in letras_usuarios:
 if ganhou:
    print(f"parabens, voce ganhou. A palavra era: {palavra}")

else:
    print(f"voce perdeu!. A palavra era: {palavra}")