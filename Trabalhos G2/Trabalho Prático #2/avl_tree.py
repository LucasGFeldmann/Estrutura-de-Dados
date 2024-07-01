class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.root = None
    
    def child(self):
        return f"L{self.left}, R{self.right}"
    
    def __repr__(self):
        return f"{self.value}"

class AVLTree:
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
            
        
        balance = self.get_balance(root)
        print(f"\n=>{value}")
        print("------",balance)

        if balance > 1 and self.get_balance(root.left) >= 0:
            """Desbalancada para a Esquerda"""
            return self.to_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            """Desbalancada para a Direita"""
            return self.to_left(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.to_left(root.left)
            return self.to_right(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.to_right(root.right)

            return self.to_left(root)
        
        return root

    
    def search(self, root, value):
        if value > root.value:
            return self.search(root.right, value)
        elif value < root.value:
            return self.search(root.left, value)
        elif value == root.value:
            return root

    def father(self, root, node):
        if node == root:
            raise Exception("Node não pode ser o root")
        
        if node == root.right:
            return root
        elif node == root.left:
            return root
        
        elif node.value > root.value:
            return self.search(root.right, node)
        elif node.value < root.value:
            return self.search(root.left, node)
        elif node.value == root.value:
            return root
    
    def delete(self, node):
        pai = self.father(self.root, node)
        if pai.right == node:
            pai.right = None
        elif pai.left == node:
            pai.left = None
        
        lista = self.preorder(node)
        lista.pop(0)
        for valor in lista:
            self.insert(self.root, valor)

    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.value] + self.inorder(root.right)
        else:
            return []

    def preorder(self, root):
        if root:
            return [root.value] + self.preorder(root.left) + self.preorder(root.right)
        else:
            return []

    def postorder(self, root):
        if root:
            return self.postorder(root.left) + self.postorder(root.right) + [root.value]
        else:
            return []

    def make_tree(self, arr):
        for item in arr:
            self.insert(self.root,item)

    def inexistente(self, valor):
        if valor == None:
            return f'|{" ".center(5)}'
        else:
            return f'-{str(valor).center(5)}' 
    
    def array_reverse(self, root, nivel = 0):
        if root:
            return self.array_reverse(root.right, nivel + 1) + [(nivel, root.value)] + self.array_reverse(root.left, nivel + 1)
        else:
            return [(nivel, None)]
    
    def array(self, root, nivel = 0):
        if root:
            return self.array(root.left, nivel + 1) + [(nivel, root.value)] + self.array(root.right, nivel + 1)
        else:
            return [(nivel, None)]

    def to_right(self, root):
        left = root.left
        rleft = left.right
        
        root.left = rleft
        left.right = root
        
        return left
    
    def to_left(self, root):
        right = root.right
        rright = right.left
        
        root.right = rright
        right.left = root
        
        return right
        
    def height(self, node) -> int:
        """
        Retorna o valor de filhor que contem. Inclui o proprio node no valor.
        Se o param node não é do tipo Node retorna 0
          A
         / \
        B   C
        
        Isso retorna 3
        """
        def recursivo(node):
            if node.right and node.left:
                return 2 + recursivo(node.right) + recursivo(node.left)
            elif node.right:
                return 1 + recursivo(node.right)
            elif node.left:
                return 1 + recursivo(node.left)
            else:
                return 0
        if type(node) == Node:
            return recursivo(node) + 1
        else:
            return 1
    
    def get_balance(self, node):
        if not node:
            return 0
        elif node.right != None and node.left != None:
            return self.height(node.left) - self.height(node.right)
        elif node.right != None:
            return 0 - self.height(node.right)
        elif node.left  != None:
            return self.height(node.left) - 0
        else:
            return 0
    

    def representacao(self, root):
        arr = self.array_reverse(root, 0)
        for x, y in arr:
            print(x * "|   ",self.inexistente(y))

    def __repr__(self) -> str:
        return f"{self.root}"
        
            
