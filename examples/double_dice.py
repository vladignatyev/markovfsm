#!coding:utf-8

from random import random
from graphviz import Digraph

from markov import Chain
from markov.plot import transitions_to_graph


def double_dice():
    return int(random() * 6) + int(random() * 6)

chain = Chain(11, double_dice())

# flip coin many times and build Markov chain for this process
# let 0 be heads and 1 tails
for i in range(1000000):
    chain.learn(double_dice())


g = Digraph(format='svg', engine='dot',
            graph_attr={'overlap': 'false', 'pad': '0.1', 'nodesep': '0.35', 'ranksep': '0.35'},
            edge_attr={'fontname':'Helvetica', 'fontsize': '8.0'},
            node_attr={'fontname': 'Helvetica'})

def state_mapping(s):
    scores = {
        2: u'⚀⚀',
        3: u'⚀⚁',
        4: u'⚁⚁',
        5: u'⚁⚂',
        6: u'⚂⚂',
        7: u'⚂⚃',
        8: u'⚃⚃',
        9: u'⚃⚄',
        10: u'⚄⚄',
        11: u'⚄⚅',
        12: u'⚅⚅'
    }
    return scores[s + 2]

transitions_to_graph(g, chain.transition_matrix(), state_mapping)
g.render('./graph')
