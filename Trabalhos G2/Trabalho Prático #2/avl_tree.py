
class Node:
    """
    Classe que representa um nó em uma árvore AVL.

    Atributos:
    -----------
    value : int, float, optional
        O valor armazenado no nó. O padrão é None.
    left : Node, optional
        O nó filho à esquerda. O padrão é None.
    right : Node, optional
        O nó filho à direita. O padrão é None.
    """

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

    def child(self):
        """
        Retorna uma string representando os filhos do nó.

        Returns:
        --------
        str
            String com os filhos do nó.
        """
        return f"L{self.left}, R{self.right}"
    
    def __repr__(self):
        """
        Retorna uma representação em string do valor do nó.

        Returns:
        --------
        str
            O valor do nó como string.
        """
        return f"{self.value}"


class AVLTree:
    """
    Classe que representa uma árvore AVL.

    Atributos:
    -----------
    root : Node, optional
        A raiz da árvore. O padrão é None.

    Métodos:
    --------
    insert(root, value):
        Insere um novo valor na árvore.
    balance(root):
        Balanceia a árvore a partir de um nó dado.
    to_right(root):
        Rotaciona a árvore à direita.
    to_left(root):
        Rotaciona a árvore à esquerda.
    height(node):
        Calcula a altura de um nó.
    get_balance(node):
        Obtém o fator de balanceamento de um nó.
    inorder(root):
        Retorna uma lista de valores na ordem infixa.
    preorder(root):
        Retorna uma lista de valores na ordem prefixa.
    postorder(root):
        Retorna uma lista de valores na ordem posfixa.
    make_tree(arr):
        Cria uma árvore a partir de uma lista de valores.
    formarter(valor):
        Formata um valor para impressão.
    array_reverse(root, nivel):
        Gera uma lista de nós em ordem reversa.
    show(root):
        Exibe a árvore de forma formatada.
    search(root, value):
        Busca um valor na árvore.
    min_value_node(node):
        Encontra o nó com o menor valor a partir de um nó dado.
    delete(root, value):
        Remove um nó da árvore.
    """

    def __init__(self, root=None):
        """
        Inicializa a árvore AVL.

        Parameters:
        -----------
        root : Node, int, float, optional
            A raiz da árvore. Pode ser um objeto Node, um inteiro ou um float. O padrão é None.
        """
        self.root = root if isinstance(root, Node) else Node(root) if root is not None else None

    def insert(self, root, value):
        """
        Insere um novo valor na árvore.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde o valor será inserido.
        value : int, float
            O valor a ser inserido.

        Returns:
        --------
        Node
            A nova raiz ou sub-raiz após a inserção e balanceamento.
        """
        if not root:
            return Node(value)
        
        if value > root.value:
            root.right = self.insert(root.right, value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            return root
        
        return self.balance(root)

    def balance(self, root):
        """
        Balanceia a árvore a partir de um nó dado.

        Parameters:
        -----------
        root : Node
            O nó a partir do qual o balanceamento será realizado.

        Returns:
        --------
        Node
            A nova raiz ou sub-raiz após o balanceamento.
        """
        balance_factor = self.get_balance(root)
        
        if balance_factor > 1:
            if self.get_balance(root.left) > 0:
                return self.to_right(root)
            else:
                root.left = self.to_left(root.left)
                return self.to_right(root)
        if balance_factor < -1:
            if self.get_balance(root.right) < 0:
                return self.to_left(root)
            else:
                root.right = self.to_right(root.right)
                return self.to_left(root)
        
        return root

    def to_right(self, root):
        """
        Rotaciona a árvore à direita.

        Parameters:
        -----------
        root : Node
            O nó a partir do qual a rotação será realizada.

        Returns:
        --------
        Node
            A nova raiz ou sub-raiz após a rotação.
        """
        left = root.left
        rleft = left.right
        
        left.right = root
        root.left = rleft
        
        return left

    def to_left(self, root):
        """
        Rotaciona a árvore à esquerda.

        Parameters:
        -----------
        root : Node
            O nó a partir do qual a rotação será realizada.

        Returns:
        --------
        Node
            A nova raiz ou sub-raiz após a rotação.
        """
        right = root.right
        rright = right.left
        
        right.left = root
        root.right = rright
        
        return right

    def height(self, node):
        """
        Calcula a altura de um nó.

        Parameters:
        -----------
        node : Node
            O nó cuja altura será calculada.

        Returns:
        --------
        int
            A altura do nó.
        """
        if not node:
            return 0
        return self.height(node.left) + self.height(node.right) + 1

    def get_balance(self, node):
        """
        Obtém o fator de balanceamento de um nó.

        Parameters:
        -----------
        node : Node
            O nó cujo fator de balanceamento será calculado.

        Returns:
        --------
        int
            O fator de balanceamento do nó.
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

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
            return self.inorder(root.left) + [root.value] + self.inorder(root.right)
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
            return [root.value] + self.preorder(root.left) + self.preorder(root.right)
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
            return self.postorder(root.left) + self.postorder(root.right) + [root.value]
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
            self.root = self.insert(self.root, item)
    
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
            return self.array_reverse(root.right, nivel + 1) + [(nivel, root.value)] + self.array_reverse(root.left, nivel + 1)
        else:
            return []
    
    def show(self, root):
        """
        Exibe a árvore de forma formatada.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz que será exibida.
        """
        arr = self.array_reverse(root, 0)
        for x, y in arr:
            print(x * "|   ", self.formarter(y))
            
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
            O nó

 que contém o valor buscado ou None se não encontrado.
        """
        if not root or root.value == value:
            return root
        
        if value < root.value:
            return self.search(root.left, value)
        
        return self.search(root.right, value)

    def min_value_node(self, node):
        """
        Encontra o nó com o menor valor a partir de um nó dado.

        Parameters:
        -----------
        node : Node
            O nó a partir do qual a busca será realizada.

        Returns:
        --------
        Node
            O nó com o menor valor.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, value):
        """
        Remove um nó da árvore.

        Parameters:
        -----------
        root : Node
            A raiz ou sub-raiz onde a remoção será realizada.
        value : int, float
            O valor do nó a ser removido.

        Returns:
        --------
        Node
            A nova raiz ou sub-raiz após a remoção e balanceamento.
        """
        if not root:
            return root
        
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        
        return self.balance(root)

    def __repr__(self) -> str:
        """
        Retorna uma representação em string da raiz da árvore.

        Returns:
        --------
        str
            A raiz da árvore como string.
        """
        return f"{self.root}"
