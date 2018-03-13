class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, element, path_array):
        # element = data to be inserted

        # path_array an array of 0s and 1s (for left and right respectively) to denote where
        # to store the element. If an empty spot is found before the array is exhausted, the
        # element is simply inserted at that spot and rest of the array is ignored.

        if (self.root is None):
            self.root = Node(element)
            return

        current_node = self.root
        for i in path_array:
            if (i == 0):
                if(current_node.left == None):
                    current_node.left = Node(element)
                    break
                else:
                    current_node = current_node.left
            elif (i == 1):
                if(current_node.right == None):
                    current_node.right = Node(element)
                    break
                else:
                    current_node = current_node.right

    def print_traversal(self, type):
        print('{} TRAVERSAL:'.format(type.upper()))
        if (type == 'pre'):
            self.preorder(self.root)
        elif(type == 'post'):
            self.postorder(self.root)
        elif(type == 'in'):
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

b = BinaryTree()
b.insert(1, [0, 1, 0])
b.insert(2, [0])
b.insert(3, [1])
b.insert(4, [0, 0])
b.insert(5, [0, 1])

b.print_traversal('post')