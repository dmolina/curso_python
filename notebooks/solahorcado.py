referencia = input()

while len(referencia) == 0:
    referencia = input()

size = len(referencia)
actual = list("_" * size)
intentos = 5

while "_" in actual and intentos > 0:
    print("Actual:", "".join(actual))
    print("Intentos:", intentos)
    letra = input()

    if letra not in referencia:
        intentos -= 1
    else:
        for i, c in enumerate(referencia):
            if c == letra:
                actual[i] = letra

if intentos:
    print("Has acertado, felicidades")
else:
    print("Lo siento, has fallado, la palabra era '" + referencia + "'")
