import sys

def is_bst(node, min_value=-sys.maxsize, max_value=sys.maxsize):
    if node.val==None:
        return True
    else:
        if node.left != None and node.left.val >= max_value:
            return False
        if node.right != None and node.right.val <= min_value:
            return False
        return is_bst(node.left, min_value, node.left.val) and is_bst(node.right, node.right.val, max_value)