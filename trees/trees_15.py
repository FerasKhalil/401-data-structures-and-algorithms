# from stack_and_queues.stack_and_queues import Queue
from typing import NoReturn

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


class Node:
    def __init__(self,value=None,left=None,right=None):
        self.left=left
        self.right = right
        self.value = value
    def __str__(self):
        return str(self.value)    

class BinaryTree:
    def __init__(self,root=None):
        self.root = root
        self.pre_order_lister=[]
        self.in_order_lister=[]
        self.post_order_lister=[]
# 
    def pre_order(self,root):
        self.pre_order_lister.append(root.value)
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)
        return self.pre_order_lister

    def in_order(self,root):
        self.in_order_lister.append(root.value)
        if root.left:
             self.in_order(root.left)
        if root.right:
             self.in_order(root.right)
        return self.in_order_lister

    def post_order(self,root):
        if root.left:
             self.post_order(root.left)
        if root.right:
             self.post_order(root.right)

    def maximum_tree_value(self):
        all_tree_values = self.in_order(self.root)
        max_val = self.root.value
        for i in all_tree_values:
            if i > max_val:
                 max_val = i
        return max_val

        # def breadth_first(self,tree):
    #     lister=[]
    #     if tree.root == None:
    #         return 'Empty tree'
    #     else:
    #         if tree.root:
    #             lister.append(tree.root)
    #         if tree.root.left:
    #             lister.append(tree.root.left)
    #         if tree.root.right:
    #             lister.append(tree.root.right)
    def breadth_first(self,tree=None):
        lister=[]
        breadth_queue = Queue()
        front = Node()
        breadth_queue.enqueue(tree)
        while breadth_queue.peek():
            front = breadth_queue.dequeue()
            lister.append(front)
            if front.left:
                breadth_queue.enqueue(front.left)
            if front.right:
                breadth_queue.enqueue(front.right)
        return lister        

    def fizz_buzz_tree(k_ary_tree):
        pass    
         
## # # # # # # # ###############################################

class BinraySearchTree(BinaryTree):
    def __init__(self,node=None):
        self.root=None
    
    def add(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value,self.root)    
# _add() is private function of add. Made it for recursion.
# Knowing the root of the tree exists we will check if the new node was greater than or bigger than it. Then add the node where it belongs with recursion (in the private function)

    def _add(self,value,rooter):
        if value < rooter.value: #if it was smaller than root
            if rooter.left == None:
                rooter = Node(value)
            else:
                self._add(value,rooter.left)
        elif value > rooter.value: #if it was bigger than root
            if rooter.right == None:
                rooter.right = Node(value)
            else:

                self._add(value,rooter.right)    
        else:
            print("value is already in the tree")        




if  __name__ == "__main__":
    # treeing = BinraySearchTree()
    # noder1 = Node(2)
    # noder2 = Node(5)
    # noder3 = Node(3)
    # noder4 = Node(1)

    # treeing.root = noder1
    # noder1.left=noder4
    # noder1.right=noder2
    # noder2.left=noder3
    # treeing.add(noder1.value)
    # print (BinraySearchTree.pre_order(noder1))
    # print (BinraySearchTree.in_order(noder1))
    # print (BinraySearchTree.post_order(noder1))

## CHAllenge 17 
    tree = BinaryTree()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    node5=Node(5)
    node6=Node(6)
    node7=Node(7)
    tree.root=node1
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.left=node6
    node3.right=node7
    print(BinaryTree.breadth_first(tree))






