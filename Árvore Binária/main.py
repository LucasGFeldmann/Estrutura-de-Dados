class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.right = None
        self.left = None
        self.root = None
    
    def __repr__(self):
        return f"{self.value} - {self.value}|{self.right} || {self.value}|{self.left}"

class Tree:
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

    def in_order(self, root):
        if root:
            return self.in_order(root.left) + [root.value] + self.in_order(root.right)
        else:
            return []

    def pre_order(self, root):
        if root:
            return [root.value] + self.pre_order(root.left) + self.pre_order(root.right)
        else:
            return []

    def post_order(self, root):
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
        
            
