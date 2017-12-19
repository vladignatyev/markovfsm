from copy import copy
from random import random


class Chain(object):
    def __init__(self, states_count, initial_state):
        self._states_count = states_count
        self._initial_state = initial_state
        self.clear()

    """
        Build Markov chain from data by feeding new state of the random process
    """
    def learn(self, state):
        self.states[self.current_state][state] = self.states[self.current_state][state] + 1
        self.current_state = state

    """
        Get the transition matrix P of Markov chain
    """
    def transition_matrix(self):
        m = copy(self.states)
        for i in range(self._states_count):
            s = 1.0 / sum([m[i][j] for j in range(self._states_count)])
            m[i] = [m[i][j] * s for j in range(self._states_count)]
        return m

    """
        Get probabilities of transitions to another states from current state
    """
    def get_transitions_probs(self, state):
        s = 1.0 / sum([self.states[state][j] for j in range(self._states_count)])
        c = copy(self.states[state])
        return [c[i] * s for i in range(self._states_count)]

    """
        Clear the model
    """
    def clear(self):
        self.states = [[0 for j in range(self._states_count)] for i in range(self._states_count)]
        self.current_state = self._initial_state



class FSM(object):
    def __init__(self, chain, initial_state, rnd=random):
        self.chain = chain
        self.current_state = initial_state
        self._rnd = rnd

    @property
    def state(self):
        return self.current_state

    def next(self):
        probs = self.chain.get_transitions_probs(self.current_state)
        r = self._rnd()

        p0 = 0.0
        p1 = 0.0

        for i in range(len(probs)):
            p1 = p0 + probs[i]
            if r >= p0 and r < p1:
                self.current_state = i
                return self.current_state
            else:
                p0 = p1



if __name__ == '__main__':
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

    # let's make another chain, build upon random process emulated by FSM
    chain2 = Chain(2, 0)

    # make a chain with states produced by FSM
    for j in range(1000000):
        chain2.learn(fsm.next())

    # get transition matrix. it should be nearly equal
    P2 = chain2.transition_matrix()

    print "%s %s" % (P2[0][0], P2[0][1])
    print "%s %s" % (P2[1][0], P2[1][1])

    print chain2.get_transitions_probs(0)
