from stack_and_queues.stack_and_queues_12 import *
# # # # # CHALLENGE 10 # # # # # # # ## # # 
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

# def test_dequeue_out_of_queue():
#     queue=Queue()
#     node1 = Node(1)
#     node2 = Node(2)
#     queue.front=node1
#     node1.next=node2
#     queue.dequeue()
#     expected = 2
#     actual = queue.front.value
#     assert expected == actual

# def test_empty_a_equeue_after_multiple_dequeues():
#     queue=Queue()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     queue.front=node1
#     node1.next=node2
#     node2.next=node3
#     node3.next=node4
#     queue.dequeue()
#     queue.dequeue()
#     queue.dequeue()
#     queue.dequeue()
#     assert queue.is_empty

# def test_multiple_value_enqueue():
#     queue = Queue()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     expected = 1
#     actual = queue.front.value
#     assert expected == actual

# def test_instantiate_an_empty_queue():
#     queue=Queue()
#     assert queue

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
#     # expected="empty queue amigo"
#     with pytest.raises(EmptyStackOrQueueException, match = "Queue is Empty"):
#         queue=Queue.dequeue()
#     queue=dequeue()



 # # ## CHALLENGE 13 # # # # # 
 
def test_validate_bracket():
    actual=validate_brackets('()')
    expected=True
    assert actual==expected

def test_weird_validate_bracket():
    actual=validate_brackets('{](})}))}}')
    expected=False
    assert actual==expected

