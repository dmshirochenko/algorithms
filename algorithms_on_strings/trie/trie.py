#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


class StringTree():
    def __init__(self, node_key, letter_label):
        self.node_key = node_key
        self.letter_label = letter_label
        self.child_list = []


    def add_child(self, node):
        self.child_list.append(node)

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.letter_label)+"\n"
        #print(ret)
        for i in range(len(self.child_list)):
            #print(self.child_list[i])
            ret += self.child_list[i].__str__(level+1)
        return ret


def build_trie_with_class(patterns):
    tree = {}
    tree[0] = StringTree(0, None)
    next_node_number = 1
    for pattern in patterns:
        #print('pattern = {}'.format(pattern))
        current_node = tree[0]
        for char_index in range(len(pattern)):
            match = False
            for child_node in current_node.child_list:
                if pattern[char_index] == child_node.letter_label:
                    current_node = child_node
                    match = True
            if not match:
                tree[next_node_number] = StringTree(next_node_number, pattern[char_index])
                #print("No Match: Node created key  = {}, label = {}".format(tree[next_node_number].node_key, tree[next_node_number].letter_label))
                current_node.add_child(tree[next_node_number])
                current_node = tree[next_node_number]
                next_node_number += 1

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    print("Initial data = {}".format(patterns))
    tree = build_trie_with_class(patterns)
    #print("Edge end root = {}".format(tree[0].edge_end.letter_label))
    #print(tree[0])

    for item in tree:
        #print("item node =  {}, item letter label = {}, item adj_list  = {}".format(tree[item].node_key, tree[item].letter_label, tree[item].child_list))
        if tree[item].child_list:
            for c in tree[item].child_list:
                print("{}->{}:{}".format(tree[item].node_key,  c.node_key, c.letter_label))
