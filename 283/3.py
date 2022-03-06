from typing import *

# 这个属于二叉树的表示方式之间的转换
# 二叉树里面的各节点值互不相同 也就是说一个数字可以唯一表示一个节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        from collections import defaultdict
        # 键是id 值是TreeNode
        nodetable = defaultdict(None)
        isroot = defaultdict(bool)
        for node in descriptions:
            parent, child, isLeft = node
            # 如果父节点不存在
            if parent not in nodetable:
                nodetable[parent] = TreeNode(parent)
                isroot[parent] = True
            # 如果子节点不存在
            if child not in nodetable:
                nodetable[child] = TreeNode(child)
            if isLeft:
                nodetable[parent].left = nodetable[child]
            else:
                nodetable[parent].right = nodetable[child]
            isroot[child] = False
        for key,value in isroot.items():
            if value:
                return nodetable[key]

def main():
    sol = Solution()
    _input = ([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]], )
    _output = sol.createBinaryTree(*_input)
    print(_output)
    print(_output.val)

if __name__ == '__main__':
    main()
