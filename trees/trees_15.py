from typing import NoReturn


class Node:
    def __init__(self,value,left=None,right=None):
        self.left=left
        self.right = right
        self.data = value
    def __str__(self):
        return str(self.value)    

class binary_tree:
    def __init__(self,root=None):
        self.root = root
        pre_order_lister=[]
        in_order_lister=[]
        post_order_lister=[]


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
        self.post_order_lister.append(root.value)
        return self.post_order_lister




