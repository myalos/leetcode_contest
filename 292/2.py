from typing import *

# 一个二叉树节点root 找出并返回满足要求的个数，要求节点的值等于其子树中值的平均值

# root的子树由root和它的所有后代组成
# n个元素的平均值可以由n个元素求和然后再除以n，并向下舍入到最近整数

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            value, cnt = node.val, 1
            if node.left:
                _value, _cnt = dfs(node.left)
                value += _value
                cnt += _cnt
            if node.right:
                _value, _cnt = dfs(node.right)
                value += _value
                cnt += _cnt
            if node.val == value // cnt:
                ans += 1
            return value, cnt
        dfs(root)
        return ans

def main():
    sol = Solution()
    root = TreeNode(4)
    layer11 = TreeNode(8)
    layer12 = TreeNode(5)
    layer21 = TreeNode(0)
    layer22 = TreeNode(1)
    layer24 = TreeNode(6)
    root.left = layer11
    root.right = layer12
    layer11.left = layer21
    layer11.right = layer22
    layer12.right = layer24
    _input = (root, )
    _output = sol.averageOfSubtree(*_input)
    print(_output)

if __name__ == '__main__':
    main()
