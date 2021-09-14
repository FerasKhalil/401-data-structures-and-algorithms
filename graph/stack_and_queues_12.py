from typing import NewType


class Node:
    def __init__(self,value=""):
        self.value=value
        # self.pointer=pointer
        self.next = None
    def __str__(self):
        return str(self.value)    

class EmptyStackOrQueueException(Exception):
    	pass
 
#######CODE CHALLENGE 10 # # # # ## # ## #### # ## # ######  ## ####

class Stack:
    def __init__(self,node=None):
        self.top=node

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node      
    
    def pop(self):
        if self.top == None:
            return "this is an empty stack amigo"
        else:    
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.top == None:
            return "this is an empty stack amigo"
        else:
            return self.top.value
                          
    def is_empty (self):
        if self.top == None:
            return False
        else:
            return True    

  
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self , value):
        node=Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node    
            self.rear = node    

    def peek(self):
        if self.front==None:
            raise Exception("empty queue amigo")
        else:
            return self.front.value    
    
    def is_empty(self):
        return self.front == None


    def dequeue(self):

        if self.front:
            current = self.front
            self.front = current.next
            current.next=None
            return current.value
        else:
            raise Exception('Queue is Empty')    
        




    # 9 9 99 9 99 99 9 9 9 9 9 9 9 9 9  99 9  9

# CHALLENGE 12
class AnimalShelter:
    def __init__(self):
        # self.dog_front = None
        # self.dog_rear = None
        # self.cat_front = None
        # self.cat_rear = None
        self.dog_queue=Queue()
        self.cat_queue=Queue()
        
    def enqueue_animal(self,animal):
        user_animal = AnimalShelter(animal)
        if user_animal.type=='dog':
            if self.dog_front == None:
                self.dog_front = user_animal
                self.dog_rear = user_animal
            else:
                self.dog_rear.next = user_animal
                self.dog_rear = user_animal
        elif user_animal.type == 'cat':
            if self.cat_front == None:
                self.cat_front = user_animal
                self.cat_rear = user_animal
            else:
                self.cat_rear.next = user_animal
                self.cat_rear = user_animal
        else:
            return 'type should only be dog or cat'
    def dequeue_animal(self,pref):
        pass


# # # CHALLENGE 13 # # # # # # #
def validate_brackets(user_input):
    stack_list = []
    valid_brackets={")":"(","}":"{","]":"["}
    for i in user_input:
        if i in valid_brackets.values():
            stack_list.append(i)
        elif stack_list and valid_brackets[i] == stack_list[-1]:
            stack_list.pop()     
        else:
            return False
    if stack_list==[]:
        return True
    else:
        return False            

# if __name__ == "__main__":
#     # new = LinkedList()
#     # new.append(3)
#     # print(new)
#     # first_instant = LinkedList('hello')
#     # print (str(first_instant))    
#     # print(first_instant.next)

#     lister = LinkedList()
#     node1 = Node(4)
#     node2 = Node(3)
#     node3 = Node(2)
#     node4 = Node(1)
#     lister.head=node1
#     node1.next=node2
#     node2.next=node3
#     node3.next=node4
#     print(lister) 
#     lister.reverse_lister()    
#     print(lister)


