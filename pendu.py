dico = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

mot = dico[3]
mot_len = len(mot)

mystere = ""
test = True

for i in range(mot_len):
    if i%2 == 0:
        mystere += mot[i]
    else:
        mystere += "*"


while test:

    print(mystere)
    mot_utilisateur = input("Quel est le mot mystere: ")

    if not len(mot_utilisateur) == mot_len:
        print(f"Desole vous devez entre un mot contenant {mot_len} caractere!")
    else:
        if not mot_utilisateur == mot:
            mystere_backup = mystere
            mystere = ""
            for i in range(mot_len):
                if mot_utilisateur[i] == mot[i]:
                    if i > 0:
                        if mot[i-1] == mot_utilisateur[i-1]:
                            mystere += mot[i]
                    else:
                        mystere += mystere_backup[i]
                else:
                    mystere += mystere_backup[i]
            print(f"Desole le mot mystere entre ne correspond pas!")
        else:
            print(f"Felicitation vous avez trouvez le mot cache : {mot}")
            test = False