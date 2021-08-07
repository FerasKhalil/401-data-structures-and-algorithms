
class Node:
    ### CODE CHALLENGE  5
    def __init__(self,value=""):
        self.value=value
        # self.pointer=pointer
        self.next = None
    def __str__(self):
        return str(self.value)    


class LinkedList():
    """
    Put docstring here
    """
    def __init__(self):
        # initialization here
        self.head = None
        # self.next = None
    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next=self.head
        self.head = node    

    def some_method(self):
        # method body here
        pass

    def __str__(self):
        return str(self.head)

    #   #####################################
    ### CODE CHALLENGE 6

    # def append(self,value=''):
    #     print(value)
    #     node = Node(value)
    #     current = self.head

    #     while current.next != None:
    #         current = current.next
    #     current.next = node

    # def insert_before(self,value, new_value):
    #     pass


    # def insert_after():
    #     pass
#   #####################################
    ### END CODE CHALLENGE 6 END ###################
         
   
    #     ##########################################\
    #### CODE  CHALLENGE 7
    # def kth(self,number):
    #     current = self.head
    #     list_length=1
    #     while current.next:
    #         list_length+=1
    #         current=current.next
    #     current=self.head
    #     if number > list_length:
    #         return("Input is greater than the length of the linked list")
    #     elif number < 0:
    #         return("Input k is not a positive integer")
    #     target = list_length - number - 1
    #     print(target)
    #     for i in range(list_length):
    #         if i == target:
    #             print(current.value)
    #             return(current.value)
    #         else:
    #             current=current.next
                 #     ##########################################\
    #### END CODE  CHALLENGE 7 END #################

#####################################################
##### CODE  CHALLENGE 8
    # def zip_lists(l1,l2):
    
    #     lister=LinkedList()
    #     current1=l1.head
    #     current2=l2.head
    #     previous1=current1.next
    #     previous2=current2.next
       
    #     while current1:
    #         # lister.append(current1)
    #         lister.append(current1.value)
    #         current1=previous1.next
    #         # current1.next=current1.next
            
####################  END CHALLENGE 8

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
        




if __name__ == "__main__":
    new = LinkedList()
    new.append(3)
    print(new)
    first_instant = LinkedList('hello')
    print (str(first_instant))    
    print(first_instant.next)
    