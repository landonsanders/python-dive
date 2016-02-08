class Node:
    def __init__(self, data=None, leftTree=None, rightTree=None):
        self.data = data
        self.leftTree = leftTree
        self.rightTree = rightTree
        
    def __str__(self):
        return str(self.data)
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def remove(node):
        if node.left and node.right:
            successor = node.right:
                while successor.left:
                    successor = successor.left
                node.key = successor.key
                node.value = successor.value
                self.remove(successor)
        elif node.left:
            self.replace(node.left, node)
        elif node.right:
            self.replace(node.right, node)
        else:
            self.replace(node, None)
            
print_tree(tree):
    if tree == None:
        return
    print tree
    print_t(tree.left)
    print_t(tree.right)
        
        
