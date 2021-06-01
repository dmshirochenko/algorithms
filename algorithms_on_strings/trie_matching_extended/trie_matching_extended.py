# python3
import sys


class StringTree():
    def __init__(self, node_key, letter_label):
        self.node_key = node_key
        self.letter_label = letter_label
        self.child_list_node = []
        self.child_node_letter_label = []
        self.end_of_the_pattern = False

    def add_child(self, node):
        self.child_list_node.append(node)
        self.child_node_letter_label.append(node.letter_label)

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.letter_label) + "\n"
        for child_node in self.child_list:
            ret += child_node.__str__(level + 1)
        return ret


def build_trie_with_class(patterns):
    tree = {}
    tree[0] = StringTree(0, None)
    next_node_number = 1
    for pattern in patterns:
        # print('pattern = {}'.format(pattern))
        current_node = tree[0]
        for char_index in range(len(pattern)):
            if pattern[char_index] in current_node.child_node_letter_label:
                for child_node in current_node.child_list_node:
                    if pattern[char_index] == child_node.letter_label:
                        current_node = child_node
                        if ((len(pattern) - 1) == char_index):
                            current_node.end_of_the_pattern = True
            else:
                tree[next_node_number] = StringTree(
                    next_node_number, pattern[char_index])
                #print("No Match: Node created key  = {}, label = {}".format(tree[next_node_number].node_key, tree[next_node_number].letter_label))
                current_node.add_child(tree[next_node_number])
                current_node = tree[next_node_number]
                if ((len(pattern) - 1) == char_index):
                    current_node.end_of_the_pattern = True
                next_node_number += 1

    return tree

def prefix_trie_matching(text, tree):
    # print("Text to check = {}".format(text))
    i = 0
    symbol = text[i]
    current_node = tree[0]
    pattern = ""
    text_len = len(text)
    # print("Initial text len = {}".format(text_len))
    while True:
        if (not current_node.child_list_node) or current_node.end_of_the_pattern:
            # print("Returned patertn = {}".format(pattern))
            return pattern
        i += 1
        #print("Current symbol = {}, i = {}".format(symbol, i))
        # print("Current_node = {}, number = {}, letter_label = {}".format(current_node.letter_label, current_node.node_key, current_node.letter_label))
        # text_len -= 1
        if symbol in current_node.child_node_letter_label:
            for child_node in current_node.child_list_node:
                if (symbol == child_node.letter_label):
	                # print("Symbol = {}, child_node.letter_label = {}".format(symbol, child_node.letter_label))
                    pattern += symbol
                    current_node = child_node
                    if (not child_node.child_list_node) or (child_node.end_of_the_pattern):
	                    # print("Find leaf Returned patertn = {}".format(pattern))
	                    return pattern
                    if text_len > i:
                        symbol = text[i]
                    else:
                        return False
                    break

        else:
            return False


def tree_matching(text, tree):
    result = []
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], tree):
            result.append(i)

    return result


"""
class Node:
	def __init__ (self):
		self.next = [NA] * 4

def solve (text, n, patterns):
	result = []

	// write your code here

	return result
"""
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

tree = build_trie_with_class(patterns)
# print(tree[0])
"""
for node in tree:
    print("Node key = {}, node letter = {}, is it last node = {}".format(
        tree[node].node_key, tree[node].letter_label, tree[node].end_of_the_pattern))
"""
ans = tree_matching(text, tree)


sys.stdout.write(' '.join(map(str, ans)) + '\n')
