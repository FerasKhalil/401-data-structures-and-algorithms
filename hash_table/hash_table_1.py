from collections import Counter
from trees.trees_15 import *
from linked_list.linked_list import *


class HashTable :

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None] *self.size

    def hash(self,key:str)->int:
        value=0
        for x in key:
            value += ord(x)
        index = (value * 7) % self.size   
        return index

    def add(self,key,value):
        index = self.hash(key) 
        if not self._buckets[index]:
            self._buckets[index] = LinkedList()
        self._buckets[index].append([key,value])

    def find(self,key):
        index = self.hash[key]
        return index

    def contains(self,key):    
        index = self.hash(key)
        if self._buckets[index]:
            linked_list = self._buckets[index]
            current = linked_list.head

            while current!=None:
                if current.value[0] == key:
                    return True

                current = current.next
        return False

 
def repeated_word(user_input)->str: 
    if not user_input:
        return None
    else:
        hash_table=HashTable()
        user_input = user_input.replace('.', '')
        user_input = user_input.replace(',', '')
        user_input = user_input.replace('-', '')
        all_words=user_input.split()

        for word in all_words:
            word=word.lower()
            if hash_table.contains(word):
                return word
            hash_table.add(word,word)    


def tree_intersection(first_b_tree,second_b_tree):
    lister_1=first_b_tree.pre_order()
    lister_2=second_b_tree.pre_order()
    output_list=[]
    for i in lister_1:
        if i in lister_2:
            output_list.append(i)
    if output_list:
        return output_list
    else:
        return 


if __name__ == "__main__":
    stringer = "Once upon a time, there was a brave princess who..."
    print(repeated_word(stringer))