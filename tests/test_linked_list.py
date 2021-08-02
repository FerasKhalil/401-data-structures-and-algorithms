###### TEST CODE CHALLENGE 5
import pytest
from linked_list_insertions.linked_list_insertions import LinkedList, Node


# def test_import():
#     assert LinkedList


# def test_insert():
#     linked_list = LinkedList()
#     with pytest.raises(AttributeError):
#         linked_list.head.value
#     linked_list.insert("first")
#     actual = linked_list.head.value
#     assert actual == "first"    




# def test_add__node_to_the_end_of_the_linked_list():
#     assert LinkedList.append()

# def add_multiple_nodes_to_the_end_of_linked_list():
#     value1 = 5
#     value2 = 10
#     assert LinkedList.append(value1) == 5
#     assert LinkedList.append(value2) == 10

# # def insert_node_before_node_located_i_the_middle_of_linked_list():
# #     value = 5
# #     new_value = 10
# #     assert LinkedList.insert_before(value,new_value) ==






def test_kth_greater_than_the_length_of_the_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    list = LinkedList()
    list.insert(node4)
    list.insert(node3)
    list.insert(node2)
    list.insert(node1)

    actual = LinkedList.kth(7)
    expected = "the argument is greater than the length of the list"
    assert actual == expected



#Where k and the length of the list are the same
def test_k_same_length_as_list():
    pass

def test_k_is_not_postive_integer():
    pass

def test_linked_list_size_1():
    pass

def test_k_is_at_the_end():
    pass