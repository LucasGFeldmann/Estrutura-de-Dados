from avl_tree import AVLTree
import unittest

# Define a classe Node e AVLTree aqui antes de rodar os testes
# Copie e cole a implementação completa das classes Node e AVLTree aqui

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        """Configuração do ambiente de teste antes de cada método de teste."""
        self.avl = AVLTree()

    def test_insert_single_value(self):
        """Teste para a inserção de um único valor."""
        self.avl.root = self.avl.insert(self.avl.root, 10)
        self.assertEqual(self.avl.root.value, 10)

    def test_insert_multiple_values(self):
        """Teste para a inserção de múltiplos valores."""
        values = [10, 20, 5, 6, 15, 30, 25, 40]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        inorder_result = self.avl.inorder(self.avl.root)
        self.assertEqual(inorder_result, [5, 6, 10, 15, 20, 25, 30, 40])

    def test_balance(self):
        """Teste para garantir que a árvore está balanceada após inserções."""
        values = [1,2,3,4,5]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        self.assertEqual(self.avl.get_balance(self.avl.root), 0)

    def test_delete_leaf_node(self):
        """Teste para deletar um nó folha."""
        values = [10, 20, 5, 6]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        self.avl.root = self.avl.delete(self.avl.root, 6)
        inorder_result = self.avl.inorder(self.avl.root)
        self.assertEqual(inorder_result, [5, 10, 20])

    def test_delete_node_with_one_child(self):
        """Teste para deletar um nó com um filho."""
        values = [10, 20, 5, 6]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        self.avl.root = self.avl.delete(self.avl.root, 5)
        inorder_result = self.avl.inorder(self.avl.root)
        self.assertEqual(inorder_result, [6, 10, 20])

    def test_delete_node_with_two_children(self):
        """Teste para deletar um nó com dois filhos."""
        values = [10, 20, 5, 6, 15]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        self.avl.root = self.avl.delete(self.avl.root, 10)
        inorder_result = self.avl.inorder(self.avl.root)
        self.assertEqual(inorder_result, [5, 6, 15, 20])

    def test_search(self):
        """Teste para a busca de um valor."""
        values = [10, 20, 5, 6, 15]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        result = self.avl.search(self.avl.root, 15)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 15)

    def test_min_value_node(self):
        """Teste para encontrar o nó com o menor valor."""
        values = [10, 20, 5, 6, 15]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        min_node = self.avl.min_value_node(self.avl.root)
        self.assertEqual(min_node.value, 5)

    def test_height(self):
        """Teste para calcular a altura de um nó."""
        values = [10, 20, 5, 6, 15]
        for value in values:
            self.avl.root = self.avl.insert(self.avl.root, value)
        
        height = self.avl.height(self.avl.root)
        self.assertEqual(height, 5)

if __name__ == '__main__':
    unittest.main()
