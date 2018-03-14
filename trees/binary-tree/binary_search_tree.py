from node import Node
from random import randint

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if (self.root is None):
            self.root = Node(data)
            return

        current = self.root
        while (True):
            if (data <= current.data):
                if (current.left is None):
                    current.left = Node(data)
                    break
                else:
                    current = current.left
            elif (data > current.data):
                if (current.right is None):
                    current.right = Node(data)
                    break
                else:
                    current = current.right

    def search(self, key):
        current = self.root

        while (current is not None and current.data != key):
            if (key < current.data):
                current = current.left
            elif (key > current.data):
                current = current.right

        return current != None

    def print_traversal(self, type):
        print('{} TRAVERSAL:'.format(type.upper()))
        if (type == 'pre'):
            self.preorder(self.root)
        elif (type == 'post'):
            self.postorder(self.root)
        elif (type == 'in'):
            self.inorder(self.root)

    def preorder(self, root):
        if (root != None):
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

bst = BinarySearchTree()

for x in range(0, 20):
    bst.insert(x)

bst.print_traversal('in')
print(bst.search(19))