class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def reverse_itertive(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            print(nxt.data)
        self.head = prev
        
if __name__ == '__main__':
    llist = LinkedList()  #llist is object

    llist.head = Node(1) #Inserting value in node1
    second = Node(2)     # Inserting value in node2
    third = Node(3)      #Inserting value in node3 

    llist.head.next = second  #linking node1 to node2
    second.next = third       # linking node2 to node3

    #note = no need to link node 3 because no nodes after node 3

    llist.printlist()