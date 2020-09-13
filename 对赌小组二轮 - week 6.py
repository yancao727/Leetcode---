#!/usr/bin/env python
# coding: utf-8

# # Leetcode 1197：进击的骑士
# 一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。
# 
# 骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格。
# 
# 每次移动，他都可以按图示八个方向之一前进。
# 
# 现在，骑士需要前去征服坐标为 [x, y] 的部落，请你为他规划路线。
# 
# 最后返回所需的最小移动次数即可。本题确保答案是一定存在的。

# In[ ]:


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        d = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        x, y = abs(x), abs(y)
        
        seen = set()
        see.add((0,0))
        q = [[0,0]]
        steps = 0
        while q:
            for _ in range(len(q)):   
                i, j = q.pop(0)
                if i == x and j == y:
                    return steps

                for d1, d2 in d:
                    nx, ny = i + d1, j + d2
                    if -2 <= nx < x + 2 and -2 <= ny < y + 2 and (nx,ny) not in seen:
                        seen.add((nx,ny))
                        q.append([nx,ny])
            steps += 1

    
# 数学方法？？https://blog.csdn.net/qq_17550379/article/details/101195668
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x + y == 1:
            return 3
        res = max(max((x + 1)//2, (y + 1)//2), (x + y + 2)//3)
        res += (res ^ x ^ y) & 1
        return res


# # 1490. Clone N-ary Tree
# Given a root of an N-ary tree, return a deep copy (clone) of the tree.
# 
# Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.
# 
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# In[ ]:


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def coloneNode(node):
            newNode = Node()
            newNode.val = node.val
            if node.children is not None:
                newNode.children = []
                for c in node.children:
                    cc = colonNode(c)
                    newNode.children.append(cc)
            else:
                newNode.children = None 
            return newNode
            
        return colonNode(root) if root else None

