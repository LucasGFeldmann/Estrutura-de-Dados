class Node:
    """
    Classe que representa um nó em uma árvore ternária.

    Atributos:
    -----------
    value : int, float, optional
        O valor armazenado no nó. O padrão é None.
    left : Node, optional
        O nó filho à esquerda. O padrão é None.
    middle : Node, optional
        O nó filho do meio. O padrão é None.
    right : Node, optional
        O nó filho à direita. O padrão é None.
    root : Node, optional
        O nó pai. O padrão é None.
    """

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.middle = None
        self.right = None
        self.root = None

    def child(self):
        """
        Retorna uma string representando os filhos do nó.

        Returns:
        --------
        str
            String com os filhos do nó.
        """
        return f"L{self.left}, M{self.middle}, R{self.right}"
    
    def __repr__(self):
        """
        Retorna uma representação em string do valor do nó.

        Returns:
        --------
        str
            O valor do nó como string.
        """
        return f"{self.value}"


class TernaryTree:
    """
    Classe que representa uma árvore ternária.

    Atributos:
    -----------
    root : Node, optional
        A raiz da árvore. O padrão é None.

    Métodos:
    --------
    insert(root, value):
        Insere um novo valor na árvore.
    search(root, value):
        Busca um valor na árvore.
    father(root, node):
        Encontra o pai de um nó.
    delete(node):
        Remove um nó da árvore.
    inorder(root):
        Retorna uma lista de valores na ordem infixa.
    preorder(root):
        Retorna uma lista de valores na ordem prefixa.
    postorder(root):
        Retorna uma lista de valores na ordem posfixa.
    make_tree(arr):
        Cria uma árvore a partir de uma lista de valores.
    middle_count(node):
        Conta o número de nós filhos do meio a partir de um nó dado.
    formarter(valor):
        Formata um valor para impressão.
    array_reverse(root, nivel):
        Gera uma lista de nós em ordem reversa.
    array(root, nivel):
        Gera uma lista de nós.
    show:
        Exibe a árvore de forma formatada.
    """

    def __init__(self, root=None):
        """
        Inicializa a árvore ternária.

        Parameters:
        -----------
        root : Node, int, float, optional
            A raiz da árvore. Pode ser um objeto Node, um inteiro ou um float. O padrão é None.
        """
        if type(root) == Node: 
            self.root = root
        elif type(root) == int or type(root) == float:
            self.root = Node(root)
        elif root == None:
            self.root = root
        else:
            raise TypeError("type not allowed")

    def insert(self, root, value):
        """
        Insere um novo valor na árvore.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde o valor será inserido.
        value : int, float
            O valor a ser inserido.
        """
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
        """
        Busca um valor na árvore.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a busca será realizada.
        value : int, float
            O valor a ser buscado.

        Returns:
        --------
        Node
            O nó contendo o valor buscado, ou None se não for encontrado.
        """
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
        """
        Encontra o pai de um nó.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a busca será realizada.
        node : Node
            O nó cujo pai será encontrado.

        Returns:
        --------
        Node
            O nó pai do nó fornecido.

        Raises:
        -------
        Exception
            Se o nó fornecido for a raiz da árvore.
        """
        if node == root:
            raise Exception("Node não pode ser o root")
        elif node == None:
            raise Exception("Valor nao encontrado")
        
        # Retorna o pai
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
        """
        Remove um nó da árvore.

        Parameters:
        -----------
        node : Node
            O nó a ser removido.
        """
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
        """
        Retorna uma lista de valores na ordem infixa.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a ordenação será realizada.

        Returns:
        --------
        list
            Lista de valores na ordem infixa.
        """
        if root:
            return self.inorder(root.left) + [root.value] + self.inorder(root.middle) + self.inorder(root.right)
        else:
            return []

    def preorder(self, root):
        """
        Retorna uma lista de valores na ordem prefixa.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a ordenação será realizada.

        Returns:
        --------
        list
            Lista de valores na ordem prefixa.
        """
        if root:
            return [root.value] + self.preorder(root.left) + self.preorder(root.middle) + self.preorder(root.right)
        else:
            return []

    def postorder(self, root):
        """
        Retorna uma lista de valores na ordem posfixa.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a ordenação será realizada.

        Returns:
        --------
        list
            Lista de valores na ordem posfixa.
        """
        if root:
            return self.postorder(root.left) + self.postorder(root.right) + self.postorder(root.middle) + [root.value]
        else:
            return []

    def make_tree(self, arr):
        """
        Cria uma árvore a partir de uma lista de valores.

        Parameters:
        -----------
        arr : list
            Lista de valores a serem inseridos na árvore.
        """
        for item in arr:
            self.insert(self.root, item)

    def middle_count(self, node):
        """
        Conta o número de nós filhos do meio a partir de um nó dado.

        Parameters:
        -----------
        node : Node
            O nó a partir do qual a contagem será realizada.

        Returns:
        --------
        int
            O número de nós filhos do meio.
        """
        if node.middle:
            return 1 + self.middle_count(node.middle)
        else:
            return 1

    def formarter(self, valor):
        """
        Formata um valor para impressão.

        Parameters:
        -----------
        valor : int, float, None
            O valor a ser formatado.

        Returns:
        --------
        str
            O valor formatado como string.
        """
        if valor == None:
            return f'|{" ".center(5)}'
        else:
            return f'-{str(valor).center(5)}' 
    
    def array_reverse(self, root, nivel=0):
        """
        Gera uma lista de nós em ordem reversa.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a listagem será realizada.
        nivel : int, optional
            O nível inicial de profundidade. O padrão é 0.

        Returns:
        --------
        list
            Lista de nós em ordem reversa.
        """
        if root:
            return self.array_reverse(root.right, nivel + 1) + [(nivel, root.value, self.middle_count(root))] + self.array_reverse(root.left, nivel + 1)
        else:
            return []
    
    def array(self, root, nivel=0):
        """
        Gera uma lista de nós.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a listagem será realizada.
        nivel : int, optional
            O nível inicial de profundidade. O padrão é 0.

        Returns:
        --------
        list
            Lista de nós.
        """
        if root:
            return self.array(root.left, nivel + 1) + [(nivel, root.value, self.middle_count(root))] + self.array(root.right, nivel + 1)
        else:
            return []

    @property
    def show(self):
        """
        Exibe a árvore de forma formatada.
        """
        arr = self.array_reverse(self.root, 0)
        for x, y, z in arr:
            print(x * "|   ", self.formarter(f"{(str(y) + ' ') * z}"))

    def __repr__(self) -> str:
        """
        Retorna uma representação em string da raiz da árvore.

        Returns:
        --------
        str
            A raiz da árvore como string.
        """
        return f"{self.root}"
