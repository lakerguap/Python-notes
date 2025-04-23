city = "chicago"
print("the city where you live in is", city) #la newline di print è inclusa nell'output che fornisce


#variabili

price = 50 #50 è un int

tax_rate = 1.15 #in questo caso, 1.15 è un floating point

#in python, una variabile può contenere diversi valori

total = price + tax_rate

print(total)

total = price * tax_rate

print(total)

#in questo caso, total può contenere due valori diversi

#una variabile può contenere stringhe

customer_name = "Idris Elba"

#può anche contenere un valore booleano

discount = True

#funzione print

first_name = "Ali"
age = 20

print("Name:", first_name, "Age:", age)

#nel caso in cui volessi che i valori vengano separati da , posso usare un parametro
#integrato nella funzione print, sep
#posso usare un altro parametro, end, per separare due frasi da uno spazio

print(1,2,3,4,5,sep=",")
print("On the", end=" ")
print("same line")

#apertura di un file

text_file = open("file.txt", "w") #open aprirà file.txt per la scrittura

#text_file è un oggetto che ci permette di scrivere su file
#posso passare text_file a print e print lo aprirà

print("Test 1 2 3", file=text_file)  #file contiene Test 1 2 3

text_file.close()



#operatori aritmetici

a = 5
b = 2

print("a =", a)
print("b =", b)
print("")

print(" a + b =", a + b)
print(" a - b =", a - b)
print(" a * b =", a * b)
print(" a ** b =", a**b) #a elevato a b
print(" a / b =", a / b)
print(" a % b =", a % b)
print(" a // b =", a // b) #divisione fra floating numbers arrotondata al numero vicino più piccolo
print(" a // -b =", a // -b)

c = 4
d = 5
print("")
print("c before =", c)
print("d before =", d)

#entrambi gli statement fanno la stessa cosa
c += d
c = c + d

print("c after =", c)



#user input
#qualsiasi valore inserito in input viene convertito in una stringa
#se inserisci un valore int, viene convertito in una stringa
#devi convertirlo esplicitamente in un int usando typecasting

val = input("Enter your value: ")
print("your value is:", val)

#esistono funzioni che prendono il valore desiderato

num = int(input("Enter a number:"))
print(num, " ", type(num))

floatNum = float(input("Enter a decimal number:"))
print(floatNum, " ", type(floatNum))

#operatori di comparazione

a = 5

print(1 < a < 10)
print(10 > a <= 9)
print(5 != a > 4)
print(a < 10 < a*10 == 50)

#operatori logici

#oepratori logici AND,OR,NOT con variabili generiche

a, b, c = True, False, True

if a and c:
    print("Both a and c are True (AND condition).")
if b or c:
    print("Either b or c is True (OR condition).")
if not b:
    print("b is False (NOT condition).")

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("At least one number is not greater than 0")


#un blocco è tale quando ogni istruzione è separata dagli stessi spazi


#condizioni if

i = 10
if i == 10:  # Livello 1 (nessun rientro)
    print("i is smaller than 15")  # Livello 2 (4 spazi)

    if i < 12:  # Livello 2 (4 spazi, perché annidato dentro il primo if)
        print("i is smaller than 12 too")  # Livello 3 (8 spazi, perché annidato nel secondo if)
    else:
        print("i is greater than 15")  # Livello 3 (8 spazi, perché allineato all'if annidato)
else:
    print("i is not equal to 10")  # Livello 2 (4 spazi, perché dentro l'else del primo if)


#cicli while

i = int(input("insert value:"))
while i < 5: #non sono richieste parentesi attorno alla condizione
    print(i)
    i += 1 #incremento

#statement continue permette il passaggio al blocco successivo

i = 1

while i <= 10:
    print(i)
    if (i == 3):
        i += 3
        continue #se la condizione è soddisfatta, incremento di 3 e passo al blocco successivo
    i += 1

#nel caso di stringhe
i = 0
a = "stringofcharacters"

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue    #nel caso in cui la condizione fosse rispettata, il contatore scorre di 1

    print(a[i])
    i += 1

#tipi su python

name = "Barbara Liskov"
age = 24 #valore di tipo int
average = 94.5
is_student = True
grades = [92.56, 93.45, 97.78]

#la funzione type permette di ritormare il tipo di valore contenuto nella variabile

print(type(age))
print(type(name))
print(type(average))
print(type(is_student))
print(type(grades))

#conversione di un tipo
#posso convertire una somma di stringhe in una somma di int

number1 = "41"
number2 = "50"

sum = int(number1) + int(number2)

print(sum)

#conversione di tipi

x = int(input("Enter a number:"))
y = float(input("Enter a decimal number:"))

print("x:", x)
print("type(x):", type(x))

print("y:", y)
print("type(y):", type(y))

z = x + y

print("type(z):", type(z))

xf = 5.25

print("xf:", xf)
print("type(xf):", type(xf))

xi2 = int(xf)

print("xi2:", xi2)
print("type(xi2):", type(xi2))


yi = 7

print("yi:", yi)
print("type(yi):", type(yi))

ys1 = str(yi)

print("ys1:", ys1)
print("type(ys1)", type(ys1))




#stringhe

programmer = "Grace Hopper"

print(programmer)

print(type(programmer))

#         0123456789
school = "Yale University"

#possiamo accedere ad ogni carattere della stringa usando un operatore index

print(school[0])

print(school[5])

print(school[0:4])

print(school[5:])

print(len(school))

#possiamo verificare l'uguaglianza fra due stringhe diverse

other_string = "Vassar College"

if (school == other_string):
    print("Schools are the same")
else:
    print("Schools are NOT the same")

#possiamo creare un loop con a

text = "invented one of the 1st Linkers"

for character in text:
    print(character)


#possiamo incrementare un contatore ogni volta che un carattere di una stringa è uguale all'altro

count = 0
for character in text:
    if(character == "e"):
        count +=  1
print("e count:", count)

if("one" in text):
    print("one IS in text")

if("two" not in text):
    print("two is NOT in text")


#modificare una stringa

birth = " Born in New York City "

print(birth.upper())

print(birth.lower())

#posso ritagliare gli spazi

print(birth.strip())

print(birth.replace("York", "Fork"))

print(birth.split())

first_name = "Grace"

last_name = "Hopper"

full_name = first_name + " " + last_name

#se voglio aggiungere elementi mentre il programma è in esecuzione

birthday = "{} in the year {} "

year = int(input("Enter a number: "))
print(birthday.format("Born", year))


#sequenze di escape

#\n - newLine
print("Line1\nline2")

#\t - tab
print("Before Tab\tAfter")

#\b - backspace
print("Some text in a string")


#metodi per le stringhe

#mettere la prima lettera di una stringa in maiuscolo

string = "portfolio COURSES"

new_string = string.capitalize()    #non modifica la vecchia stringa ma ne crea una nuova

print(new_string)


#aumentare la lunghezza di una stringa, aggiungendo spazi per centrarla

string = "text"

new_string = string.center(6)

#con dash
#new_string = string.center(10, "-")

print(new_string)

#numero di occorrenze di una stringa in una stringa
         #0123456789   12
string = "To be or not not to be"

be_count = string.count("be")
print(be_count)

to_count = string.count("to")
print(to_count)

o_range_count = string.count("o",2,12)
print(o_range_count)

#controllare se una stringa termina con un'altra stringa, restituisce true o false

string = "Carol Shaw"

print(string.endswith("Shaw"))

#funzione range e list

numbers = list(range(0,10))
print(numbers)

#append

lista = ['mele', 'pere', 'banane']
lista.append ('angurie')

print(lista)

#insert

lista = ['carne', 'uova', 'patate']
lista.insert (2, 'riso')

print(lista)

#max(list)/min(list)

lista = [2, 3, 4, 5]
print(max(lista))

#remove

lista = ['s', 'f', 'g', 4, 7]
lista.remove('f')
print(lista)


#format

name = "Gianni"
age = 30
message = ("My name is {0} and i am {1} years old. {1} is my favorite number.".format(name, age))

#join

stringa = ['s', 'f', 'g', 'h']

print(' '.join(stringa))

#split

stringa = "mi chiamo gianluca"

x = stringa.split()

print(x)


#reversed

numeri = [1, 2, 3, 4, 5]

for i in reversed(numeri):
    print(numeri)

#slicing

numeri = [1, 2, 3, 4, 5]

for i in numeri[::-1]:
    print(i)



