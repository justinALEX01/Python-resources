import random

print("Care este numele tau?")
name = input()
nr_de_incercari = 0

generated = random.randint(0,100)
print("Numerele la care ma gandesc sunt intre 1 si 100", name)

while nr_de_incercari < generated:
    print("Alege un numar:")
    numar = input()
    numar = int(numar)

    nr_de_incercari = nr_de_incercari + 1

    print("Caut un numar mai mare") if numar <  generated else print("Caut un numar mai mic")
    if numar ==  generated:
        break

if numar == generated:
    nr_de_incercari = str(nr_de_incercari)
    print("Corect!", name, "Ai nimerit din incercarea nr:", nr_de_incercari)
if numar != generated:
    generated = str(generated)
    print("Gresit!:", generated)
