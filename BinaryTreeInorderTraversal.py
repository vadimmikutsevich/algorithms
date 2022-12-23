class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

def inorderTraversal(root):
    result = []

    def inorder(n):
        if n:
            inorder(n.left)
            result.append(n.val)
            inorder(n.right)
    inorder(root)
    return result

print(inorderTraversal(root))