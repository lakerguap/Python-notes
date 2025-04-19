class Node:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


    #insert
    def Insert(self, data):
        if data < self.data:
            if self.leftchild:
                #se abbiamo ancora bisogno di scorrere sul ramo sinistro
                self.leftchild.Insert(data)
            else:
                self.leftchild = Node(data)
                return
        else:
            if self.rightchild:
                self.rightchild.Insert(data)
            else:
                self.rightchild = Node(data)
                return

    def PrintTree(self):
        if self.leftchild:
            self.leftchild.PrintTree()
        print (self.data)
        if self.rightchild:
            self.rightchild.PrintTree()

root = Node(27)

root.Insert(15)
root.Insert(86)
root.Insert(65)
root.Insert(12)
root.Insert(9)

root.PrintTree()




