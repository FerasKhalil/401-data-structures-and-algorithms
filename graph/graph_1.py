from typing import Deque
from stack_and_queues_12 import * 
class Node:
    def __init__(self,value=""):
        self.value=value
        # self.pointer=pointer
        self.next = None
    def __str__(self):
        return str(self.value)    

class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
   

class Graph:
    def __init__(self):
        self._adjacency_list={}

    def add_node(self,value):
        node=Node(value)
        self._adjacency_list[node]=[]
        return node

    def add_edge(self,vertex1,vertex2,weight=1):
        if vertex1 not in self._adjacency_list or vertex2 not in self._adjacency_list:
            raise KeyError("not found")
        self._adjacency_list[vertex1].append(Edge(vertex2,weight))    

    def get_nodes(self):
        return self._adjacency_list.keys()


    def get_neighbors(self,vertex):
        return self._adjacency_list.get(vertex,[])

    def size(self):
        return len(self._adjacency_list)


    def breadth_first(self,vertex):
        nodes=[]
        breadth=Queue()
        visited=[]
        breadth.enqueue(vertex)
        visited.append(vertex)
        while breadth:
            front=breadth.dequeue()
            nodes.append(front)
            for i in nodes:
                if i not in visited:
                    visited.append(i)
                    breadth.enqueue(i)
        return nodes                



def business_trip(graph_1,city_names):
    pass


def depth_first_graph():
    pass



