from typing import NewType


class Node:
    def __init__(self,value=""):
        self.value=value
        # self.pointer=pointer
        self.next = None
    def __str__(self):
        return str(self.value)    

 
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
            return "empty queue amigo"
        else:
            return self.front.value    
     
##### END CHALLENGE 10  # # #  # # # ## ## # # ## # # # # # # # ## # ## 
        


    # 9 9 99 9 99 99 9 9 9 9 9 9 9 9 9  99 9  9


class AnimalShelter:
    def __init__(self):
        self.dog_front = None
        self.dog_rear = None
        self.cat_front = None
        self.cat_rear = None

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


