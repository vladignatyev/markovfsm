#!coding:utf-8

from random import betavariate
from graphviz import Digraph

from markov import Chain
from markov.plot import transitions_to_graph


def rigged_dice():
    return int((betavariate(0.5, 0.7) * 6))

chain = Chain(6, rigged_dice())

# roll dice many times and build Markov chain for this process
for i in range(100000):
    chain.learn(rigged_dice())


def state_mapping(state):
    if state == 0: return u'⚀'
    if state == 1: return u'⚁'
    if state == 2: return u'⚂'
    if state == 3: return u'⚃'
    if state == 4: return u'⚄'
    if state == 5: return u'⚅'



g = Digraph(format='svg', engine='dot',
            graph_attr={'pad': '0.1', 'nodesep': '0.15', 'ranksep': '0.5'},
            edge_attr={'fontsize': '6.0', 'fontname':'Helvetica'})

transitions_to_graph(g, chain.transition_matrix(), state_mapping)
g.render('./graph')
