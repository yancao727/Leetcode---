#!/usr/bin/env python
# coding: utf-8

# # 1231 分享巧克力
# 你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。
# 
# 你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。
# 
# 为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。
# 
# 请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。
# 
# 输入：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
# 输出：6
# 解释：你可以把巧克力分成 [1,2,3], [4,5], [6], [7], [8], [9]。

# In[ ]:


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = 1, sum(nums) // (k + 1)
        while l < r:
            cur = 0
            cnt = 0
            mid = (l + r) // 2
            for s in sweentness:
                cur += s
                if cur >= mid:
                    cnt += 1
                    cur = 0
            if cnt >= k + 1: #分多了，自己得到的sweetness可以更大
                l = mid
            else:
                r = mid - 1
        return l


# # 1485 Clone Binary Tree With Random Pointer

# In[ ]:


# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        self.map = {}
        def dfs(node):
            if not node:
                return None
            if node in self.map:
                return self.map[node]
            copyNode = NodeCopy(node.val)
            self.map[node] = copyNode
            copyNode.left = dfs(node.left)
            copyNode.right = dfs(node.right)
            copyNode.random = dfs(node.random)
            return copyNode
        return dfs(root)

