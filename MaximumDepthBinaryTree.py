class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

def maxDepth(root):
    if root:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        print(max(left_depth, right_depth))
        return max(left_depth, right_depth) + 1
    else:
        return 0


print(maxDepth(node))