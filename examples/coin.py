#!coding:utf-8

from random import random
from graphviz import Digraph

from markov import Chain
from markov.plot import transitions_to_graph


def coin():               # random process: the perfect coin flipping
  return 1 if random() > 0.5 else 0

chain = Chain(2, coin())  # create an empty Markov chain with 2 states

for i in range(1000000):  # let the Markov chain build state transition matrix
  chain.learn(coin())   # based on 1000000 of coin flips

# let's plot a graph of state transitions
g = Digraph(format='svg', engine='dot',
          graph_attr={'pad': '0.1', 'nodesep': '0.4', 'ranksep': '1.0'},
          node_attr={'fontname': 'Helvetica'},
          edge_attr={'fontsize': '8.0', 'fontname': 'Helvetica'})

# the lambda here is a simple mapping function to show beautiful name
# instead of weird '0' or '1'

transitions_to_graph(g, chain.transition_matrix(),
                   lambda s: "tails" if s == 0 else "heads")

g.render('./graph')       # this will output ``graph.svg`` (SVG graphics)
                        # and ``graph`` (DOT language) files
