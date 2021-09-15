from graph.graph_1 import *
# import pytest

# def test_add_node_to_graph():
#     grapher=Graph()
#     grapher=grapher.add_node('Firas')
#     actual=grapher.value
#     expected='Firas'
#     assert actual==expected


# def test_add_edge_raise_error():
#     graph=Graph()
#     node1=Node(33)
#     node2=graph.add_node(5)
#     with pytest.raises(KeyError):
#         graph.add_edge(node1,node2)

# def test_get_nodes():
#     graph=Graph()
#     node1=graph.add_node(1)
#     node2=graph.add_node(123)
#     node3=graph.add_node(55)
#     actual=len(graph.get_nodes())
#     expected=3
#     assert actual==expected

# def test_graph_size():
#     graph=Graph()
#     graph.add_node(43)
#     actual=graph.size()
#     expected=1
#     assert actual==expected

# def test_empty_graph():
#     graph=Graph()
#     actual=graph.size()
#     expected=0
#     assert actual==expected
