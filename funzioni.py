def my_func():
    print('spam')
    print('spam')
    print('spam')
    print('spam')

#per chiamare una funzione usiamo il suo nome e la parentesi, una volta definita possiamo chiamarla più volte

my_func()


name = str(input("inserisci il tuo nome: "))
def welcome():
    print(f"buongiorno,{name}")
welcome()


def exclamation(word):
    print(word + '!')

exclamation('word')

def stampa_somma_due_volte(x, y):
    print(x + y)
    print(x + y)

stampa_somma_due_volte(6, 8)


def even(x):
    if x % 2 == 0:
        print("yes")
    else:
        print("no")
even(5)


def lunghezza(lista):
    if len(lista[0]) % 2 == 0:
        print('accettata')
    else:
        print('non accettata')

lista = ["dhbwebbjiw"]
lunghezza(lista)

def comparison(x, y):
    if x >= y:
        return x
    else:
        return y
x = comparison(5, 9)
print(x)


def double(a, b):
    return[a*2, b*2]
x = double(3, 6)
print(x)

def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(sum(4))