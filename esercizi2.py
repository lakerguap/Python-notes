#il linguaggio dei furfanti


def rovarspraket():
    vowels = "aåäeioöu"
    specials = [" ", ",", ".", "?", "!", '"', "'"]
    while True:
        parole = input("inserisci una parola: ")
        traduzione = ""
        for x in parole:
            if x in vowels or x in specials:
                 traduzione += x
            else:
                 traduzione += x + 'o' + x

        print(f"ecco la traduzione: {traduzione}")

        if input("\n Desideri inserire un'altra frase? ").lower() == "no":
            break

rovarspraket()


#reverser

def reverser():
    parola = input("inserisci il termine da invertire: ")
    for x in parola[::-1]:
        print(x)

reverser()


def reverser_alt(stringa):
    indice = (len(stringa)-1)
    new_string = ""

    while indice >= 0:
        new_string += stringa[indice]
        indice -= 1
    print(f"il termine invertito è: {new_string}")

stringa = input("inserire stringa: ")
reverser_alt(stringa)
