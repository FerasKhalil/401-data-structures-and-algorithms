# from stack_and_queues.stack_and_queues import Queue
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




# def test_fizz_buzz_tree_empty():
#     tree = BinaryTree()
#     actual = tree.fizz_buzz_tree(tree)
#     expected = "Empty Tree"
#     assert actual == expected


# def test_fizzer_bizzer():
#     tree = BinaryTree()
#     node1=Node(1)
#     node2=Node(2)
#     node3=Node(3)
#     tree.root=node1
#     node1.left=node2
#     node1.right=node3
#     assert tree.fizz_buzz_tree(tree)==['1','2','Fizz']
    

# # # # # Challenge 15

# def test_instantiate_empty_tree():
#     binary_tree = BinaryTree
#     assert binary_tree


# def test_instantiate_tree_with_1_node():
#     binary_tree = BinaryTree
#     node=Node(1)
#     binary_tree.root=node
#     actual = binary_tree.root.value
#     expected = 1
#     assert actual == expected   

# def test_add_left_right_nodes_to_root():
#     binary_tree = BinaryTree
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     binary_tree.root=node1
#     node1.left = node2
#     node1.right = node3
#     actual1=node1.left.value
#     actual2=node1.right.value
#     expected1=2
#     expected2=3
#     assert actual1 == expected1
#     assert actual2 == expected2    



# def test_preorder():
#     binary_tree=BinaryTree()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     binary_tree.root=node1
#     node1.left = node2
#     node1.right = node3
#     node2.left = node4
#     node2.right = node5
#     node3.left = node6
#     actual = binary_tree.pre_order()
#     expected =  [1, 2, 4, 5, 3, 6]
#     assert actual == expected    



# def test_inorder():
#     binary_tree=BinaryTree()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     binary_tree.root=node1
#     node1.left = node2
#     node1.right = node3
#     node2.left = node4
#     node2.right = node5
#     node3.left = node6
#     actual = binary_tree.in_order()
#     expected = [4, 2, 5, 1, 6, 3]
#     assert actual == expected  

# def test_postorder():
#     binary_tree=BinaryTree()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     binary_tree.root=node1
#     node1.left = node2
#     node1.right = node3
#     node2.left = node4
#     node2.right = node5
#     node3.left = node6
    # actual = binary_tree.post_order()
#     expected = [4, 5, 2, 6, 3, 1]
#     assert actual == expected      



## ## # CHALLENGE 17
# def test_breadth_first_func():
    # tree = BinaryTree()
    # node1=Node(1)
    # node2=Node(2)
    # node3=Node(3)
    # node4=Node(4)
    # node5=Node(5)
    # node6=Node(6)
    # node7=Node(7)
    # tree.root=node1
    # node1.left=node2
    # node1.right=node3
    # node2.left=node4
    # node2.right=node5
    # node3.left=node6
    # node3.right=node7
#     assert tree.breadth_first()=='1234567'



# def test_breadth_first():
#     tree = BinaryTree()
#     node1=Node(2)
#     node2=Node(7)
#     node3=Node(5)
#     node4=Node(2)
#     node5=Node(6)
#     node6=Node(9)
#     node7=Node(5)
#     node8=Node(11)
#     node9=Node(4)
#     tree.root=node1
#     node1.left=node2
#     node1.right=node3
#     node2.left=node4
#     node2.right=node5
#     # node3.left=node6
#     node3.right=node6
#     node5.left=node7
#     node5.right=node8
#     node6.left=node9
#     actual = tree.breadth_first()
#     expected = [2,7,5,2,6,9,5,11,4]
#     assert actual==expected




  