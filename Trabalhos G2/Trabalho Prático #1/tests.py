from ternary_tree import TernaryTree

def test_insert():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    for value in values:
        tree.insert(tree.root, value)
    
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.left.middle.value == 5
    assert tree.root.left.middle.middle.value == 5
    assert tree.root.right.value == 20
    assert tree.root.right.left.value == 15
    assert tree.root.right.right.value == 25

def test_search():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    for value in values:
        tree.insert(tree.root, value)
    
    assert tree.search(tree.root, 10).value == 10
    assert tree.search(tree.root, 5).value == 5
    assert tree.search(tree.root, 20).value == 20
    assert tree.search(tree.root, 15).value == 15
    assert tree.search(tree.root, 25).value == 25

def test_father():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    for value in values:
        tree.insert(tree.root, value)
    
    node_5 = tree.search(tree.root, 5)
    assert tree.father(tree.root, node_5) == tree.root

    node_15 = tree.search(tree.root, 15)
    assert tree.father(tree.root, node_15) == tree.root.right

def test_delete():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    for value in values:
        tree.insert(tree.root, value)
    
    #tree.show
    
    node_5 = tree.search(tree.root, 20)
    tree.delete(node_5)
    
    #tree.show

    assert tree.search(tree.root, 20) is None

def test_traversals():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    for value in values:
        tree.insert(tree.root, value)

    assert tree.inorder(tree.root) == [5, 5, 5, 10, 15, 20, 25]
    assert tree.preorder(tree.root) == [10, 5, 5, 5, 20, 15, 25]
    assert tree.postorder(tree.root) == [5, 5, 5, 15, 25, 20, 10]

def test_make_tree():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    tree.make_tree(values)
    
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.left.middle.value == 5
    assert tree.root.left.middle.middle.value == 5
    assert tree.root.right.value == 20
    assert tree.root.right.left.value == 15
    assert tree.root.right.right.value == 25

def test_show():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    tree.make_tree(values)
    tree.show

def test_formarter():
    tree = TernaryTree()
    assert tree.formarter(None) == "|     "
    assert tree.formarter(10) == "-  10 "

def test_array_reverse():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    tree.make_tree(values)
    
    arr_rev = tree.array_reverse(tree.root)
    
    expected = [(2, 25, 1), (1, 20, 1), (2, 15, 1), (0, 10, 1), (1, 5, 3)]

    assert arr_rev == expected

def test_array():
    tree = TernaryTree()
    values = [10, 5, 20, 5, 15, 25, 5]
    tree.make_tree(values)
    
    arr = tree.array(tree.root)

    
    expected = [(1, 5, 3), (0, 10, 1), (2, 15, 1), (1, 20, 1), (2, 25, 1)]
    
    assert arr == expected


test_insert()
test_search()
test_father()
test_delete()
test_traversals()
test_make_tree()
test_show()
test_formarter()
test_array_reverse()
test_array()

print("Todos os testes passaram!")
