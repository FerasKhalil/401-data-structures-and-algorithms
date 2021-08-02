
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

    def append(self,value=''):
        print(value)
        node = Node(value)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = node

    def insert_before(self,value, new_value):
        pass


    def insert_after():
        pass

         
   
    #     ##########################################\
    #### CODE  CHALLENGE 7
    def kth(self,number):
        current = self.head
        list_length=0
        while current.next:
            list_length+=1
            current=current.next
        current=self.head
        print(list_length)
        target = list_length - number
        print(target)
        for i in range(list_length):
            if i == target:
                print(i)
                return current.value
            else:
                current=current.next



if __name__ == "__main__":
    new = LinkedList()
    new.append(3)
    print(new)
    first_instant = LinkedList('hello')
    print (str(first_instant))    
    print(first_instant.next)
    