class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

def postorderTraversal(root):
    result = []

    def postorder(n):
        if n:
            postorder(n.left)
            postorder(n.right)
            result.append(n.val)
    postorder(root)
    return result

print(postorderTraversal(root))