import random

def generate_mystey_word(dictionnaire):
    mot = random.choice(dictionnaire)
    mot_len = len(mot)
    mystere = ""
    
    for i in range(mot_len):
        if i%2 == 0:
            mystere += mot[i]
        else:
            mystere += "*"
            
    return mot, mystere 


def check_it(mystere, mot, user_try):
    status = False
    msg = None
    if not len(user_try) == len(mot):
        msg = f"Desole vous devez entre un mot contenant {len(mot)} caractere!"
        return status, msg, mystere
    
    if not user_try == mot:
        mystere_backup = mystere
        mystere = ""
        for i in range(len(mot)):
            if user_try[i] == mot[i]:
                if i > 0:
                    if mot[i-1] == user_try[i-1]:
                        mystere += mot[i]
                    else:
                        mystere += mystere_backup[i]
                else:
                    mystere += mystere_backup[i]
            msg = f"Desole le mot mystere entre ne correspond pas!"
            return status, msg, mystere
    
    msg = f"Felicitation vous avez trouvez le mot cache : {mot}"
    status = True
    return status, msg, mystere


def play(dictionnaire = ["test", "mystere"]):
    mot, mystere = generate_mystey_word(dictionnaire)
    test = False
    
    while not test:
        print(mystere)
        user_try = input("Quel est le mot mystere ? ")
        test, msg, mystere = check_it(mystere, mot, user_try)
        print(msg)
  
        
dico = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mystere",
    "cacher"
]

play(dico)