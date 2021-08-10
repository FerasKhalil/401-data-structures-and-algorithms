from typing import NewType


class Node:
    ### CODE CHALLENGE  5 LINKED LISTS
    def __init__(self,value=""):
        self.value=value
        # self.pointer=pointer
        self.next = None
    def __str__(self):
        return str(self.value)    


class LinkedList():
    def __init__(self):
        self.head = None
        
    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next=self.head
        self.head = node    

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False        
        

    def __str__(self):
        current = self.head
        string = ""
        while current:
            string += str(current) + " -> "
            current = current.next
        string += "NULL"
        return string

    ### CODE CHALLENGE 6

    def append(self,value=''):
        node = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
        else:  
            while current.next != None:
                current = current.next
            current.next = Node(value)

    def insert_before(self,value, new_value):
        node = Node(new_value)
        current = self.head
        previous = self.head
        while current!=None:
            if current.value == value: 
                if current == previous:
                    self.head = node
                    node.next = current
                    break
                else:
                    previous.next = node
                    node.next = current

            previous = current
            current = current.next


    def insert_after(self,value,new_value):
        node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                break
            current = current.next
   
    #### CODE  CHALLENGE 7
    def kth(self,number):
        current = self.head
        list_length=1
        while current.next:
            list_length+=1
            current=current.next
        current=self.head
        if number > list_length:
            return("Input is greater than the length of the linked list")
        elif number < 0:
            return("Input k is not a positive integer")
        target = list_length - number - 1
        print(target)
        for i in range(list_length):
            if i == target:
                print(current.value)
                return(current.value)
            else:
                current=current.next

#### CODE  CHALLENGE 8
    def zip_lists(self,l1,l2):
        lister=LinkedList()
        current1=l1.head
        current2=l2.head
        while current1!=None and current2!=None:
            lister.append(current1)
            lister.append(current2)
            current1 = current1.next
            current2 = current2.next
        while current1!=None:
            lister.append(current1)
            current1=current1.next
        while current2:
            lister.append(current2)
            current2 = current2.next
        return lister        


            # current1.next=current1.next
            



        


#     # 9 9 99 9 99 99 9 9 9 9 9 9 9 9 9  99 9  9
#     def reverse_lister(list):
          
#         previous = None
#         current = list.head     
#         after = current.next   
  
#         while current:
#             current.next = previous 
#             previous = current      
#             current = after        
#             if after:               
#                 after = after.next

#         list.head = previous

if __name__ == "__main__":
    # new = LinkedList()
    # new.append(3)
    # print(new)
    # first_instant = LinkedList('hello')
    # print (str(first_instant))    
    # print(first_instant.next)

    lister = LinkedList()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    lister.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    print(lister) 
    lister.reverse_lister()    
    print(lister)