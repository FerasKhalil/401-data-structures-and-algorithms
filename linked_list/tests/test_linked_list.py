###### TEST CODE CHALLENGE 5
import pytest
from linked_list.linked_list import LinkedList, Node, Queue, Stack


def test_import():
    assert LinkedList

def test_instantiate():
    lister = LinkedList()
    actual = lister.head
    expected = None
    assert actual == expected

def test_insert():
    linked_list = LinkedList()
    linked_list.insert("tester")
    actual = linked_list.head.value
    assert actual == "tester"    

def test_head_point_to_first_node():
    lister = LinkedList()
    lister.insert(4)
    expected = 4
    assert lister.head.value == expected

def test_linked_list_multiple_nodes_insertion():
    lister=LinkedList()
    lister.insert(1)
    lister.insert(2)
    lister.insert(3)
    actual = lister.head.value
    expected = 3
    assert expected == actual

def test_linked_list_find_value():
    lister = LinkedList()
    lister.insert(1)
    lister.insert(2)
    actual = lister.includes(2)
    expected = True
    assert expected == actual

def test_linked_list_doesnt_find_value():
    lister = LinkedList()
    lister.insert(1)
    lister.insert(2)
    actual = lister.includes(4)
    expected = False
    assert expected == actual


def test_linked_list_return_all_nodes_values():
    lister=LinkedList()
    lister.insert(3)
    lister.insert(2)
    lister.insert(1)
    actual = lister.__str__()
    expected = '1 -> 2 -> 3 -> NULL' 
    assert expected == actual

# def test_add__node_to_the_end_of_the_linked_list():
#     assert LinkedList.append()

# def add_multiple_nodes_to_the_end_of_linked_list():
#     value1 = 5
#     value2 = 10
#     assert LinkedList.append(value1) == 5
#     assert LinkedList.append(value2) == 10

# def insert_node_before_node_located_i_the_middle_of_linked_list():
#     value = 5
#     new_value = 10
#     assert LinkedList.insert_before(value,new_value) ==

def test_add__node_to_the_end_of_the_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.append(5)
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> None"

def test_add_multiple_nodes_to_the_end_of_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None"

def test_insert_node_before_node_located_in_the_middle_of_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_before(3,5)
    assert linked_list.__str__() == "1 -> 2 -> 5 -> 3 -> 4 -> None"

def test_insert_node_before_the_first_node():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_before(1,5)
    assert linked_list.__str__() == "5 -> 1 -> 2 -> 3 -> 4 -> None"

def test_insert_after_node_located_in_the_middle_of_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_after(2,5)
    assert linked_list.__str__() == "1 -> 2 -> 5 -> 3 -> 4 -> None"

def test_insert_node_after_the_last_node():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_after(4,5)
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> None"




#### # # # # # #      CODE CHALLEGEN 7           # # # # # # # # 
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(6)
# node4 = Node(4)
# node5 = Node(9)
# node6 = Node(25)
# node7 = Node(14)
# node8 = Node(3)
# list = LinkedList()
# list.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7
# node7.next = node8

# def test_kth_greater_than_the_length_of_the_linked_list():
#     actual = list.kth(10)
#     expected = "Input is greater than the length of the linked list"
#     assert actual == expected

# #Where k and the length of the list are the same
# def test_k_same_length_as_list():
#     actual = list.kth(7)
#     expected = 1
#     assert actual == expected

# def test_k_is_not_postive_integer():
#     actual = list.kth(-3)
#     expected = "Input k is not a positive integer"
#     assert actual == expected

# def test_linked_list_size_1():
#     alone_node = Node(5)
#     linked_list=LinkedList()
#     linked_list.head = alone_node

#     actual = linked_list.kth(0)
#     expected = 5
    # assert actual == expected
    #### # # # # # #   END   CODE CHALLEGEN 7         END  # # # # # # # # 
#
#### # # # # # # # # #  CHALLENGE 8 # # # # # # # # # # # # # ## #
# def test_zip_lists():
#     l1=LinkedList()
#     l2=LinkedList()
#     l1.append(1)
#     l1.append(3)
#     l1.append(5)
#     l2.append(2)
#     l2.append(4)
#     actual=list.zip_lists(l1,l2)
#     expected='head-> {1} -> {2} -> {3} -> {4} -> {5} -> NULL'
#     assert expected==actual


# # # # # # CHALLENGE 10 # # # # # # # ## # # 
# def test_push():
#     stack = Stack()
#     stack.push(1)
#     expected = stack.top.value
#     assert expected == 1

# def test_push_multiple():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     expected = stack.top.value
#     assert expected == 3    

# def test_pop():
#     stack = Stack()
#     stack.push(2)
#     stack.push(4)
#     actual = stack.pop()
#     expected = 4
#     assert actual == expected

# def test_pop_multiple():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.pop()
#     stack.pop()
#     stack.pop()
#     actual = stack.top
#     expected = None
#     assert actual == expected

# def test_peek_stack():
#     stack=Stack()
#     stack.push(10)
#     stack.push(12)
#     expected = 12
#     actual=stack.peek() 
#     assert actual == expected   


# def test_instantiate_empty_stack():
#     stack=Stack()
#     expected=None
#     actual = stack.top
#     assert actual == expected    


# def test_raise_stack():
#     stack=Stack()
#     expected="this is an empty stack amigo"
#     assert expected==stack.peek()


# def test_enqueue():
#     queue = Queue()
#     queue.enqueue(7)
#     expected = 7
#     actual = queue.front.value
#     assert expected == actual

# def test_multiple_value_enqueue():
#     queue = Queue()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     expected = 1
#     actual = queue.front.value
#     assert expected == actual


# def test_peek_queue():
#     queue=Queue()
#     queue.enqueue(4)
#     queue.enqueue(444)
#     expected =4
#     actual=queue.peek() 
#     assert actual == expected


# def test_instantiate_empty_queue():
#     queue=Queue()
#     expected=None
#     actual = queue.front
#     assert expected == actual


# def test_exception_peek_empty_queue():
#     queue= Queue()
#     expected="empty queue amigo"
#     assert expected==queue.peek()
 # # # # #  END CHALLENGE 10 # # ##  # # # # # 