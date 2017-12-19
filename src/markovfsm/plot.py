#!coding:utf-8


def transitions_to_dotlang(matrix):
    dim = len(matrix)
    transitions = []
    for current_state in range(dim):
        for next_state in range(dim):
            t = '   %s -- %s [label = "%.4f"]' % (current_state, next_state, matrix[current_state][next_state])
            transitions.append(t)

    return "digraph G {\n%s\n}" % ('\n'.join(transitions))


def transitions_to_graph(digraph, matrix, state_index_to_name = lambda s: "%s" % s):
    dim = len(matrix)
    for i in range(dim):
        digraph.node(state_index_to_name(i))
    for current_state in range(dim):
        for next_state in range(dim):
            alpha = "{0:x}".format(int(round(matrix[current_state][next_state] * 250 + 6)))
            digraph.edge(state_index_to_name(current_state),
                         state_index_to_name(next_state),
                         label=" %.4f " % matrix[current_state][next_state],
                         color='#ff0000%s' % alpha,
                         fontcolor='#f00000%s' % alpha)

if __name__ == '__main__':
    from graphviz import Digraph

    matrix = [[0.5, 0.5], [0.5, 0.5]]
    print transitions_to_dotlang(matrix)
    g = Digraph(format='svg', engine='dot',
                graph_attr={'overlap': 'true', 'pad': '0.1', 'nodesep': '0.5', 'ranksep': '1.0'},
                edge_attr={'fontname':'HelveticaNeue'})

    transitions_to_graph(g, matrix, lambda s: "heads" if s == 1 else "tails")
    g.render('./graph')
