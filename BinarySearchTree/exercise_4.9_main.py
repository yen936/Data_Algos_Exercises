from BinarySearchTree import BinarySearchTree, Node


# Write find_in_range() function
def range_valid(begin, end):
    ascii_begin = [ord(c) for c in begin]
    ascii_end = [ord(c) for c in end]

    if ascii_begin < ascii_end:
        return True
    else:
        return False


def find_in_range(range_begin, range_end, node):
    if node is None:
        return

    find_in_range(range_begin, range_end, node.left)

    if node.key < range_begin:
        # print("less than the beginning")
        pass
    elif range_begin <= node.key <= range_end:
        keys_in_range.append(node.key)
        # print('within range')
    elif node.key > range_end:
        # print('greater than the end')
        pass

    find_in_range(range_begin, range_end, node.right)


# Main
if __name__ == "__main__":
    tree = BinarySearchTree()
    keys_in_range = []

    # Insert some random-looking integers into the tree.
    user_values = input('Enter values to be inserted separated by spaces: ')
    print()

    for value in user_values.split():
        new_node = Node(value)
        tree.insert(new_node)

    # print('Initial tree:')
    # print(tree)
    # print()

    # Read in range values and starting node's key
    range_begin = input()
    range_end = input()
    s_node = input()

    # Find starting node in tree
    start_node = BinarySearchTree.search(tree, s_node)

    # Find keys in range from starting node
    if range_valid(range_begin, range_end):
        find_in_range(range_begin, range_end, start_node)
    else:
        print("Inout Error: Range not Valid")

    # Output list of keys in range
    print('Keys in range:', keys_in_range)