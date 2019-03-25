# Markov Chain and Finite-State Stochastic Machine

This package implements functionality for analyzing stochastic (or random)
finite state (Markov) processes.

It can build a Markov chain from the states of the process.

Also the package provides non-deterministic FSM (finite-state machine)
functionality for evaluating Markov chains. You can easily build a probabilistic
automaton from the Markov chain.

One more feature is an integration with amazing `Graphviz <http://www.graphviz.org/>`_ tool.
``markovfsm`` plots a state transitions graph of Markov model for you.

# Installation
As usual, ``pip install markovfsm``

No special prerequisites required, expect the Graphviz, if you want to use plotting features.
In such case, you have to install Graphviz and ``graphviz`` PyPI package.

# Usage examples
## Coin flipping
Let's start with the simplest Markov process - a flipping of perfect coin.
Let '0' state correspond to 'tails' and '1' state to 'heads' correspondingly.

We define a random function (`coin()`), once being evaluated, returns a next state of the process.

Let's create a `Chain` object and perform big enough count of experiments:
```python
from random import random
from graphviz import Digraph

from markovfsm import Chain
from markovfsm.plot import transitions_to_graph


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
```

## Rigged dice
Another illustrative example is the process of rolling rigged dice.
We use beta distribution to emulate non-perfect dice.
The remaining part of the code almost the same.
```python
#!coding:utf-8

from random import betavariate
from graphviz import Digraph

from markovfsm import Chain
from markovfsm.plot import transitions_to_graph


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
```

# Probabilistic finite-state machine
Finite-state machine (FSM, or state machine) is a model of computation.
The machine can be in exactly one of finite number of states.
Probabilistic automaton is a FSM where transitions between states are probabilistic.
Unlike normal FSM, requiring only a graph of possible transitions between states,
probabilistic automaton adds probability of every transition.
```python
from random import random

# build Markov chain with 2 states, init with random state
chain = Chain(2, 0 if random() > 0.5 else 1)

# flip coin many times and build Markov chain for this process
# let 0 be heads and 1 tails
for i in range(1000000):
    chain.learn(0 if random() > 0.5 else 1)

# get transition matrix
#   It should look like:
#
#    P = | 0.5 0.5 |
#        | 0.5 0.5 |
#
P = chain.transition_matrix()

print "%s %s" % (P[0][0], P[0][1])
print "%s %s" % (P[1][0], P[1][1])

# get probabilities of transition from state 0 to other states (0 and 1)
# actually, the line in the transition matrix
print chain.get_transitions_probs(0)

# let's make a FSM with stochastic properties equal to described by Markov chain
# use rnd() as a random numbers generator, and 0 (heads) as initial state
fsm = FSM(chain, 0)

fsm.next()  # will change the state of automaton randomly in a such way that
            # the statistics of such transition will be equal to Markov process
            # statistics
```

# API
`chain.transition_matrix()` will return transition matrix: a matrix N x N,
where N is the number of states, where each i-row correspond to the state of the process
and each j-element in the row contains the probability of transition to state ``j``
from the state ``i``.

`FSM(chain, initial_state)` - object, representing probabilistic automaton,
built from


# License
MIT License. Creative Commons CC0.
