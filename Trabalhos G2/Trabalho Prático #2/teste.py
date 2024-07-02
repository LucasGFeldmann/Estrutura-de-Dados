from avl_tree import AVLTree
import random

def teste():
    tree = AVLTree()
    tree.make_tree([1,2,3,4,5,6,7,8])
    tree.show(tree.root)
    tree.get_balance(tree.root)
    print(tree.array_reverse(tree.root))



def teste1():
    tree = AVLTree()
    lista = random.sample(range(100),10)
    tree.make_tree(lista)
    print(lista)
    tree.show(tree.root)
    print()
    print(tree.get_balance(tree.root))
    pesq = tree.search(tree.root, lista[2])
    print('\npesquisa:',pesq)
    print(pesq.child())
    print(tree.inorder(tree.root))
    print(tree.preorder(tree.root))
    print(tree.postorder(tree.root))
    
#teste()
teste1()

