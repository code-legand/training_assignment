class Node:
    def __init__(self, data = 0, link = None):
        self.data = data
        self.link = link

    def add(self, data):
        node = self
        temp = Node()
        temp.data = data
        temp.link = None
        while node.link!=None:
            node = node.link
        node.link = temp

    def displayElem(self, n):
        temp = self
        count = 0
        while count<n:
            temp = temp.link
            count+=1
            if temp == None:
                print("No Element")
                break
        else:
            print(temp.data)

LinkedList = Node()
elements = map(int, input().split())
for i in elements:
    LinkedList.add(i)
n = int(input("N = "))
LinkedList.displayElem(n)











    
