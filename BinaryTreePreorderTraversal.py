class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

def preorderTraversal(root):
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    preorder(root)

    return result



print(preorderTraversal(root))

# Pre-Order Traversal a Binary Tree