#max tra due numeri
from operator import truediv
from os import urandom

num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un numero: "))

if num1 > num2:
    print(num1)
else:
    print(num2)

#max tra tre numeri

a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un numero: "))
c = int(input("Inserisci un numero: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

#il maggiore tra tutti

lista_numeri = [3,25,67,89,12]

numero_maggiore = lista_numeri[0]

for numero in lista_numeri:
    if numero > numero_maggiore:
        numero_maggiore = numero
print(numero_maggiore)

#sei una vocale?

string = [b]

vowel = "aeiou"
letter = str(input("Inserisci un carattere: "))

if letter in vowel:
       print(f"il carattere '{letter}' è una vocale")
else:
       print(f"il carattere '{letter}' non è una vocale")

#somma inarrestabile

lista = [3,4,5,7,8,9]
risultato = 0

for contatore in lista:
    risultato += contatore
print("il risultato della somma è ..." + str(risultato))


#moltiplicatore inarrestabile

lista = [1, 2, 5, 8 , 9, 22, 0]
risultato = 1

for contatore in lista:
    if contatore != 0:
       risultato *= contatore
print("il risultato del prodotto è..." + str(risultato))


#solamente per soci

lista = ['James', 'Lewis', 'Calvin', 'Lukas']
el = input('Inserisci un nome da cercare: ')
trovato = False

for carattere in lista:
    if carattere == el:
        trovato = True
        break
if trovato:
    print(f"{el} è presente nella lista all'indice {lista.index(el)}")
else:
    print(f"{el} non è presente nella lista.")


#generatore di istogrammi

lista = [3, 5, 6, 9]
for i in lista:
    print('*' * i)

#scriviamo la nostra versione di len()

def mia_len(mia_lista):
    lunghezza = 0
    for i in mia_lista:
        lunghezza += 1
    return lunghezza

lista = ['s', 3, 5, 'g']
print(mia_len(lista))

#a ciascuno il suo


def comprensione(mia_lista):
    lista_b = []
    for parola in mia_lista:
        lista_b.append(len(parola))
    return lista_b

lista = ['fwhwduh', 'sdhjd', 'msjdi', 'p']
print(comprensione(lista))


#il frequenzimetro

def frequenzimetro(mia_lista):

    dizionario = {}

    for i in mia_lista:
        if i in dizionario:
            dizionario[i] += 1
        else:
            dizionario[i] = 1

lista = ['a', 'b', 's', 'c', 'a']
print(frequenzimetro(lista))


#l'americana

def americana(metri):
    conversions = dict()
    conversions["miglia"] = metri * 0.000621371
    conversions["feet"] = metri * 3.28084
    conversions["pollici"] = metri * 39.3701
    conversions["yarde"] = metri * 1.09361

    print(f"{metri} metri corrispondo a:")

    #key è la chiave corrente, value è il valore associato a quella chiave
    #items restituisce i valori in coppia key,value
    for key, value in conversions.items():
        print(f"{key}: {value}")


valore = float(input("valore in metri: "))
print(americana(valore))

#il signore del tempo

def calcola_secondi():
    print("Questa funzione converte un dato numero di Giorni, ore e minuti in secondi")
    da_giorni = int(input("inserisci il numero di giorni: ")) * 24 * 3600
    da_ore = int(input("inserisci il numero di ore: ")) * 3600
    da_minuti = int(input("inserisci il numero di minuti: ")) * 60
    totale = da_giorni + da_ore + da_minuti
    print(totale)

calcola_secondi()


#il geometra

def calcolo_area():
    print("""In fase di selezioneì
          a ciascun valore numerico
          corrisponde un'area da calcolare
          -Area del triangolo 1
          -Area del rettangolo 2
          -Area del triangolo 3
          -Area del cerchio 4
          """)
    print("Di quale figura geometrica desideri calcolare l'area?")
    scelta = int(input("<<<"))

    if scelta == 1:
        print("Hai scelto il quadrato: ")
        lato = float(input("inserisci il lato: "))
        print(f"l'area del quadrato avente lato {lato} è: {lato * lato}")
    elif scelta == 2:
        print("Hai scelto area del rettangolo")
        base = float(input("inserisci il valore della base: "))
        altezza = float(input("inserisci il valore dell'altezza: "))
        print(f"l'area del rettangolo è: {base * altezza}")
    elif scelta == 3:
        print("Hai scelto il triangolo")
        base = float(input("inserisci il valore della base: "))
        altezza = float(input("inserisci il valore dell'altezza: "))
        print(f"l'area del triangolo è: {(base * altezza) / 2}")
    elif scelta == 4:
        print("Hai scelto il cerchio")
        r = float(input("Inserisci il valore del raggio: "))
        print(f"l'area del cerchio è. {(r * r) * 3.14}")
    else:
        print("nessun calcolo disponibile per il valore scelto")

calcolo_area()

#funzione genera MAC

import random

def genera_mac():
    char_set = "ABCDEF0123456789"
    mac_addr = ""
    due_punti = 0

    for _ in range(6): #il codice MAC è composto da 6 coppie
        for _ in range(2): #il codice MAC è composto da coppie
            mac_addr += random.choice(char_set)

        if due_punti < 5:
            mac_addr += ":"
            due_punti += 1

    return mac_addr

print(genera_mac())


#info di sistema

import platform

def sys_info():
    print(f"Il Sistema Operativo attualmente in uso è {platform.system()}")
    print(f"info release: {platform.release()}")

sys_info()

#trova ASCII

def trova_ascii():

    carattere = input("inserisci i caratteri da convertire: ")
    valore = ord(carattere)

    return print(f"il valore associato a {carattere} è {valore}")

trova_ascii()


#Il numero perfetto

def numero_perfetto(n):
    somma_divisori = 0

    for i in range(1, n//2 + 1):
        if n % i == 0:
            somma_divisori += i

    if somma_divisori == n:
        return True
    else:
        return False

n = int(input("inserisci un numero intero positivo: "))
if numero_perfetto(n):
    print(f"il numero {n} è un numero perfetto")
else:
    print(f"il numero {n} non è un numero perfetto")


#lista di colori

def lista_colori():
    lista = input("inserisci una lista di 10 colori separata da spazi: ")
    colori = lista.split()

    if len(colori) != 10:
        print("errore, devi inserire esattamente 10 colori")

    lettera = input("inserisci una lettera: ")
    colori_iniziano_con_lettera = []

    for colore in colori: #colore scorre fra ogni elemento della lista colori
        if colore.startswith(lettera):
            colori_iniziano_con_lettera.append(colore)

    if colori_iniziano_con_lettera:
        print(f"i colori che iniziano con la lettera {lettera} sono {','.join(colori_iniziano_con_lettera)}")
    else:
        print(f"non ci sono colori che iniziano con la lettera {lettera}")

lista_colori()


#print senza andare a capo

def print_senza_andare_a_capo():
    input_utente = input("inserisci input: ")

    while len(input_utente) is not 0:
        print(input_utente, end=" ")  #il comando end= specifica cosa deve essere al posto di \n
        input_utente = input("inserisci input: ")

print_senza_andare_a_capo()


#la segreteria

def segreteria(studenteA, studenteB, studenteC):
    # Stampa le informazioni degli studenti
    for studente in (studenteA, studenteB, studenteC):  #uso un dizionario per iterare sui dizionari
        print(studente["Nome"], studente["Cognome"], f"Classe: {studente['Classe']}")

    # Calcola e stampa la media per ogni studente
    for studente in (studenteA, studenteB, studenteC):
        media = sum(studente["Voti"]) / (float(len(studente["Voti"])))
        print(f"Media di {studente['Nome']}: {media:.2f}")

# Dizionari degli studenti
studenteA = {
    'Nome': 'Mario',
    'Cognome': 'Rossi',
    'Classe': "5B",
    'Voti': [8, 7, 6, 5, 4, 6, 8]
}

studenteB = {
    'Nome': 'Francesco',
    'Cognome': 'Bianchi',
    'Classe': "4A",
    'Voti': [8, 6, 7, 5, 8, 7, 8]
}

studenteC = {
    'Nome': 'Giulia',
    'Cognome': 'Ferrari',
    'Classe': "5A",
    'Voti': [7, 6, 4, 8, 5, 6, 7]
}

# Chiamata alla funzione
segreteria(studenteA, studenteB, studenteC)



#Gestione login

import csv

def crea_file(dizionario, nome_file):
    with open(nome_file, 'w', newline="") as file_csv: #apertura del file per la scrittura
        writer = csv.writer(file_csv)

        #intestazione del CSV
        writer.writerow(['Username', 'Password', 'Email', 'Data_di_registrazione'])

        #scriviamo i dati degli utenti
        for utente in dizionario:
            writer.writerow([utente['Username'], utente['Password'], utente['Email'], utente['Data_di_registrazione']])

def leggi_file(nome_file):
    with open(nome_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            print(row)


dati_login = {
    'Username' : input("inserisci username: "),
    'Password' : input("inserisci password: "),
    'Email' : input("inserisci email:"),
    'Data_di_registrazione' : input("inserisci data di registrazione: ")
}

crea_file(dati_login,'utenti.csv')
leggi_file('utenti.csv')


#testi di canzoni

def salva_testo_canzone(titolo, testo):
   nome_file = titolo + '.txt'
   with open(nome_file, 'w') as file_testo:
       file_testo.write(testo)
   print(f"testo della canzone {titolo} salvato in {nome_file}.")

titolo_canzone = input("inserisci il titolo della canzone: ")
testo_canzone = input("inserisci il testo della canzone: ")

salva_testo_canzone(titolo_canzone, testo_canzone)


#il sistema solare

pianeti = (
    ('mercurio', 'roccioso', 0),
    ('venere', 'roccioso', 0),
    ('terra', 'roccioso',1),
    ('marte','roccioso',2),
    ('giove', 'gassoso', 95),
    ('saturno', 'gassoso', 83),
    ('urano','gassoso', 27),
    ('plutone','gassoso', 14)
)

def sistema_solare():
    print("i pianeti del sistema solare sono:")
    for oggetto in pianeti:
        print(f"{oggetto[0]}: {oggetto[1]} contiene {oggetto[2]} satelliti.")

    num_satelliti = sum(oggetto[2] for oggetto in pianeti)

    print(f"il numero totale di satelliti nel sistema soalre è di {num_satelliti} satelliti.")

sistema_solare()



#sport di squadra e individuali

def valuta_sport(sport_selezionato):

    sport_di_squadra = {"calcio", "basket", "volley", "hockey su ghiaccio", "rugby", "football", "curling"}
    sport_individuale = {"tennis", "golf", "pugilato", "atletica", "surf", "nuoto", "ciclismo", "judo"}

    if sport_selezionato.lower() in sport_di_squadra:
        print(f"{sport_selezionato} è uno sport di squadra.")

    elif sport_selezionato.lower() in sport_individuale:
            print(f"{sport_selezionato} è uno sport individuale.")

    else:
        print("Mi dispiace, non conosco questo sport.")


sport_selezionato = input("inserisci uno sport: ")

valuta_sport(sport_selezionato)