from typing import NoReturn


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

    def pre_order(self,root):
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)

    def in_order(self,root):
        if root.left:
             self.in_order(root.left)
        if root.right:
             self.in_order(root.right)

    def post_order(self,root):
        if root.left:
             self.post_order(root.left)
        if root.right:
             self.post_order(root.right)


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
    treeing=BinraySearchTree()
    noder1 = Node(2)
    noder2 = Node(5)
    noder3 = Node(3)
    noder4 = Node(1)

    treeing.root = noder1
    noder1.left=noder4
    noder1.right=noder2
    noder2.left=noder3
    treeing.add(noder1.value)
    print (BinraySearchTree.pre_order(noder1))
    print (BinraySearchTree.in_order(noder1))
    print (BinraySearchTree.post_order(noder1))








