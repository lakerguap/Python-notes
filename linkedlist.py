class Node: #definizione di un nodo
    def __init__ (self, initdata): #definizione di un oggetto, init, self indica che si riferisce a sé stesso e init data è il suo valore
        self.data = initdata #memorizza il valore passato, in questo caso 93
        self.next = None #il riferimento in questo caso è nessuno


    def getData(self):
        return self.data #restituisce un valore

    def getNext(self):
        return self.next #restituisce il riferimento al nodo successivo


    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


temp = Node(93)  #crea un nodo con 93
print(temp.getData())  #restituisce 93
print(temp.getNext())

#in questo caso il Nodo è una foglia perché next non punta ad alcun altro nodo


#creazione di una mini lista

n1 = Node(93)
n2 = Node(42)

n1.setNext(n2)
print(n1.getData())
print(n2.getData())
print(n1.getNext())
print(n2.getNext())


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None #restituisce True se la lista è vuota

    def add(self, item):
        temp = Node(item) #crea un nuovo nodo
        temp.setNext(self.head) #collega il nodo alla testa
        self.head = temp #aggiorna la testa con il nuovo nodo

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.getData(), end=" -> ")
            current = current.getNext()
        print("None")


myList = LinkedList()
myList.add(10)
myList.add(20)
myList.add(30)

myList.display()
print("La lista è vuota?", myList.isEmpty())
print(f"La dimensione della lista è: {myList.size()}")
print("contiene 20?", myList.search(20)) #restituisce True
print("contiene 99?", myList.search(99)) #restituisce False


#append

def append(self, item):
    nuovo_nodo = Node(item)
    if self.head is None:
        self.head = nuovo_nodo
    else:
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(nuovo_nodo)

def index(self):
    current = self.head
    count = 0
    while current is not None:
        count += 1
        current = current.getNext()
    return count

def insert(self, index, item):
    new_node = Node(item)

    list_length = self.index()

    if index >= list_length:

        current = self.head
        while current.getNext() is not None: #scorro fino al penultimo elemento
            current = current.getNext()
        current.setNext(new_node)

    elif index == 0:
        new_node.setNext(self.head)
        self.head = new_node

    else:
        current = self.head
        count = 0
        while current.getNext() is not None and count < index - 1:
            current = current.getNext()
            count += 1

        if current is not None:  #inserire il nodo alla posizione richiesta
            new_node.setNext(current.getNext()) #punto al nodo a cui current puntava
            current.setNext(new_node)  #il nodo corrente punta al nuovo nodo



def pophead(self):  #rimozione dalla testa
    if self.head is None:
        return None
    popped_node = self.head
    self.head = self.head.getNext()
    return popped_node.getData()

def poptail(self): #rimozione dalla coda
    if self.head is None:
        return None

    if self.head.getNext() is None:
        data = self.head.getData()
        self.head = None
        return data

    current = self.head
    while current.getNext().getNext() is not None:  #scorro fino al penultimo nodo
        current = current.getNext()

    data = current.getNext().getData()  #rimozione dell'ultimo nodo
    current.setNext(None)
    return data








