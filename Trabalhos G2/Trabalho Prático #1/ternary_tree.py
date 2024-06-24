class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.middle = None
        self.right = None
        self.root = None
    
    def __repr__(self):
        return f"{self.value} - {self.value}|{self.right} || {self.value}|{self.left}"

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
        if value > root.value:
            return self.search(root.right, value)
        elif value < root.value:
            return self.search(root.left, value)
        elif value == root.middle:
            return self.search(root.middle, value)
        elif value == root.value:
            return root.value

    def delete(self, node):
        if type(node) == Node and node.root:
            root = node.root
            if root.right.value:
                if root.right.value == node.value:
                    root.right = None
            elif root.left.value:
                if root.left.value == node.value:
                    root.left = None
            elif root.middle.value:
                if root.middle.value == node.value:
                    root.middle = None
            
            node = Node()

    def inorder(self, root):
        if root:
            return self.in_order(root.left) + [root.value] + self.in_order(root.right)
        else:
            return []

    def preorder(self, root):
        if root:
            return [root.value] + self.pre_order(root.left) + self.pre_order(root.right)
        else:
            return []

    def postorder(self, root):
        if root:
            return self.post_order(root.left) + self.post_order(root.right) + [root.value]
        else:
            return []
    
    def midle(self,arr):
        pass

    def make_tree(self, arr):
        for item in arr:
            self.insert(self.root,item)

    def __repr__(self) -> str:
        return f"{self.root}"
        
            
