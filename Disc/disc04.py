# Tree Constructor
def tree(label, branches=[]):
    # for branch in branches:
    # assert is_tree(branch)
    return [label] + list(branches)

# Tree Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

# 2.1 Write a function that returns the largest number in a tree
def tree_max(t):
    """Return the maximum label in a tree.

    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    largest_label = label(t)
    for branch in branches(t):
        if label(branch) > largest_label:
            largest_label = label(branch)
    return largest_label

# 2.2 Write a function that returns the height of a tree. Recall that the height of a tree ins the length of the longest path from the root to a leaf
def height(t):
    """Return the height of a tree.
    
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if branches(t):
