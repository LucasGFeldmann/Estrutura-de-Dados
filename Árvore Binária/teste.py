from main import *
import random

def teste1():
    lista = []
    for x in range(5):
        lista.append(random.randint(0,101))
    print(lista)
    

    tree = Tree()

    for x in lista:
        tree.insert(tree.root,x)

    li = tree.in_order(tree.root)
    print("",li)
    li = tree.pre_order(tree.root)
    print("",li)
    li = tree.post_order(tree.root)
    print("",li)
    print(tree)


teste1()