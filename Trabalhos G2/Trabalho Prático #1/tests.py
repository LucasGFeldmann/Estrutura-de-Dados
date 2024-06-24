from ternary_tree import *


def test_classes():
    errors = []

    # Teste da classe Node
    try:
        node = Node(10)
        assert node.value == 10
        assert node.left == None
        assert node.middle == None
        assert node.right == None
        assert repr(node) == "10 - 10|None || 10|None"
    except Exception as e:
        errors.append(f"Erro na classe Node: {e}")

    # Teste da classe TernaryTree

    tree = TernaryTree()
    assert tree.root == None

    tree = TernaryTree(5)
    assert tree.root.value == 5

    node_root = Node(7)
    tree = TernaryTree(node_root)
    assert tree.root.value == 7

    try:
        tree = TernaryTree("not_allowed")
    except TypeError:
        pass  # Exceção esperada

    tree = TernaryTree()
    tree.insert(tree.root, 5)
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 7)
    tree.insert(tree.root, 5)  # valor duplicado

    assert tree.root.value == 5
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7
    assert tree.root.middle.value == 5

    result = tree.search(tree.root, 7)
    assert result == 7

    result = tree.search(tree.root, 3)
    assert result == 3

    result = tree.search(tree.root, 5)
    assert result == 5

    node_to_delete = tree.root.left
    tree.delete(node_to_delete)
    assert tree.root.left == None

    node_to_delete = tree.root.middle
    tree.delete(node_to_delete)
    assert tree.root.middle == None

    # Testando as ordens de travessia
    tree = TernaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    tree.make_tree(values)

    inorder_result = tree.inorder(tree.root)
    assert inorder_result == [2, 3, 4, 5, 6, 7, 8]

    preorder_result = tree.preorder(tree.root)
    assert preorder_result == [5, 3, 2, 4, 7, 6, 8]

    postorder_result = tree.postorder(tree.root)
    assert postorder_result == [2, 4, 3, 6, 8, 7, 5]

    # except Exception as e:
    #     errors.append(f"Erro na classe TernaryTree: {e}")

    # Verificar e reportar erros
    if errors:
        for error in errors:
            print(error)
    else:
        print("Todos os testes passaram sem erros.")

test_classes()
