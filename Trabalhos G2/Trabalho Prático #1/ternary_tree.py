class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.middle = None
        self.right = None
        self.root = None
    
    def child(self):
        return f"L{self.left}, M{self.middle}, R{self.right}"
    
    def __repr__(self):
        return f"{self.value}"

class TernaryTree:
    def __init__(self, root=None):
        if type(root) == Node: 
            self.root = root
        elif type(root) == int or type(root) == float:
            self.root = Node(root)
        elif root == None:
            self.root = root
        else:
            raise TypeError("type not allowed")

    def insert(self, root, value):
        if not root:
            self.root = Node(value)
        else:
            if value > root.value:
                if not root.right:
                    node = Node(value)
                    node.root = root
                    root.right = node
                else:
                    self.insert(root.right, value)
            elif value < root.value:
                if not root.left:
                    node = Node(value)
                    node.root = root
                    root.left = node
                else:
                    self.insert(root.left, value)
            elif value == root.value:
                if not root.middle:
                    node = Node(value)
                    node.root = root
                    root.middle = node
                else:
                    self.insert(root.middle, value)

    def search(self, root, value):
        if not root:
            return None
        if value > root.value:
            return self.search(root.right, value)
        elif value < root.value:
            return self.search(root.left, value)
        elif value == root.middle:
            return self.search(root.middle, value)
        elif value == root.value:
            return root
        return None

    def father(self, root, node):
        if node == root:
            raise Exception("Node não pode ser o root")
        
        if node == root.right or node == root.left or node == root.middle:
            return root

        if node.value > root.value:
            return self.father(root.right, node)
        elif node.value < root.value:
            return self.father(root.left, node)
        elif node.value == root.value:
            return self.father(root.middle, node)
        
        return None
    
    def delete(self, node):
        pai = self.father(self.root, node)
        if pai.right == node:
            pai.right = None
        elif pai.middle == node:
            pai.middle = None
        elif pai.left == node:
            pai.left = None
        
        lista = self.preorder(node)
        lista.pop(0)
        for valor in lista:
            self.insert(self.root, valor)

    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.value] + self.inorder(root.middle) + self.inorder(root.right)
        else:
            return []

    def preorder(self, root):
        if root:
            return [root.value] + self.preorder(root.left) + self.preorder(root.middle) + self.preorder(root.right)
        else:
            return []

    def postorder(self, root):
        if root:
            return self.postorder(root.left) + self.postorder(root.right) + self.postorder(root.middle) + [root.value]
        else:
            return []

    def make_tree(self, arr):
        for item in arr:
            self.insert(self.root, item)

    def middle_count(self, node):
        if node.middle:
            return 1 + self.middle_count(node.middle)
        else:
            return 1

    def formarter(self, valor):
        if valor == None:
            return f'|{" ".center(5)}'
        else:
            return f'-{str(valor).center(5)}' 
    
    def array_reverse(self, root, nivel=0):
        if root:
            return self.array_reverse(root.right, nivel + 1) + [(nivel, root.value, self.middle_count(root))] + self.array_reverse(root.left, nivel + 1)
        else:
            return []
    
    def array(self, root, nivel=0):
        if root:
            return self.array(root.left, nivel + 1) + [(nivel, root.value, self.middle_count(root))] + self.array(root.right, nivel + 1)
        else:
            return []

    @property
    def show(self):
        arr = self.array_reverse(self.root, 0)
        for x, y, z in arr:
            print(x * "|   ", self.formarter(f"{(str(y) + ' ') * z}"))

    def __repr__(self) -> str:
        return f"{self.root}"
