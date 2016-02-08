class Node():
    def __init__(self, cargo=0, nextNode=None):
        self.cargo = cargo
        self.nextNode = nextNode
        
    def __str__(self):
        return str(self.cargo)
        
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)

node0.nextNode = node1
node1.nextNode = node2

node = node0

while node:
    print node
    node = node.nextNode
    
def print_b(items):
    if items == None:
        return
    head = items
    tail = items.nextNode
    print_b(tail)
    print head

print_b(node0)