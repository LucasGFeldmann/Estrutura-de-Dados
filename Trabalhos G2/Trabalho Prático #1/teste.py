from ternary_tree import TernaryTree

def test_delete():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5, 6]
    #values = [10, 5, 20, 5, 15, 25, 5, 6,10,10,30]
    for value in values:
        tree.insert(tree.root, value)
    
    tree.show
    print("\n")
    node_ = tree.search(tree.root, 20)
    tree.delete(node_)
    
    tree.show

    
test_delete()