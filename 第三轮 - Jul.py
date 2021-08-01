#!/usr/bin/env python
# coding: utf-8

# # 1570 Dot Product of Two Sparse Vectors

# In[ ]:


class SparseVector:
    def __init__(self, nums: List[int]):
        self.Dict = {}
        for idx, val in enumerate(nums):
            if val != 0:
                self.Dict[idx] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key in self.Dict:
            if key in vec.Dict:
                res = res + self.Dict[key]*vec.Dict[key]
        return res


# # 1244 Design A Leaderboard

# In[ ]:


from collections import defaultdict
from heapq import *
class Leaderboard(object):
    def __init__(self):
        self.dic = defaultdict(int)
 
    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.dic[playerId] += score
        
    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        self.l = []
        heapify(self.l)
        for pid, score in self.dic.items():
            if len(self.l) >= K:
                if score > self.l[0]:
                    heappush(self.l, score)
                    heappop(self.l)       
            else:
                heappush(self.l, score)
                
        return sum(self.l)


# # 1086 High five 

# In[ ]:


import heapq
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        record = dict()
        
        for item in items:
            sd, sc = item[0], item[1] #student, score
            
            if sd not in record:
                record[sd] = [sc]
                heapq.heapify(record[sd]) #初始化
            else:
                heapq.heappush(record[sd], sc) #新分入堆
                if len(record[sd]) > 5:
                    heapq.heappop(record[sd]) #六个分里最小的出堆
                    #print record[sd]
        res = []
        for key, val in record.items():
            res.append([key, sum(val) // 5])
        # print record
        return res

