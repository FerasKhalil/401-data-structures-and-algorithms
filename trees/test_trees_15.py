from stack_and_queues.stack_and_queues import Queue
from trees.trees_15 import *



# def test_add_left_and_right_bst():
#     noder=Node()
#     noder.add(1)
#     noder.add(2)
#     noder.add(8)
#     x = noder()
    
# def test_return_maximum_value():
#     tree=BinaryTree()
#     node1 = Node(1)
#     node2 = Node(20)
#     node3 = Node(1000)
#     node4 = Node(41)
#     node5 = Node(173)
#     node6 = Node(12)
#     node7=Node(92)
#     node8=Node(412)
#     node9=Node(585)
#     tree.root=node1
#     node1.left = node2
#     node1.right = node3
#     node2.left = node4
#     node2.right = node5
#     node3.left = node6
#     node4.left=node7
#     node4.right=node8
#     node5.left=node9
#     assert tree.maximum_tree_value()==1000


## ## # CHALLENGE 17
# def test_breadth_first_func():
#     tree = BinaryTree()
#     node1=Node(1)
#     node2=Node(2)
#     node3=Node(3)
#     node4=Node(4)
#     node5=Node(5)
#     node6=Node(6)
#     node7=Node(7)
#     tree.root=node1
#     node1.left=node2
#     node1.right=node3
#     node2.left=node4
#     node2.right=node5
#     node3.left=node6
#     node3.right=node7
#     assert tree.breadth_first(tree)=='1234567'

def test_fizz_buzz_tree_empty():
    tree = BinaryTree()
    actual = tree.fizz_buzz_tree(tree)
    expected = "Empty Tree"
    assert actual == expected


# def test_fizzer_bizzer():
#     tree = BinaryTree()
#     node1=Node(1)
#     node2=Node(2)
#     node3=Node(3)
#     tree.root=node1
#     node1.left=node2
#     node1.right=node3
#     assert tree.fizz_buzz_tree(tree)==['1','2','Fizz']
    