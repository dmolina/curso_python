opciones = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']
gana = {
    'piedra': ['tijeras', 'lagarto'],
    'papel': ['piedra', 'spock'],
    'papel': ['piedra', 'spock'],
    'lagarto': ['spock', 'papel'],
    'spock': ['tijeras', 'piedra']
}
valid = False

while not valid:
    opcion1 = input()
    valid = (opcion1 in opciones)

valid = False

while not valid:
    opcion2 = input()
    valid = (opcion2 in opciones)

if opcion1 == opcion2:
    print("Empate con", opcion1)
else:
    if opcion1 in gana[opcion2]:
        print(opcion2, "gana a", opcion1)
    elif opcion2 in gana[opcion1]:
        print(opcion1, "gana a", opcion2)
