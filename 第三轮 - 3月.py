#!/usr/bin/env python
# coding: utf-8

# # LeetCode-Python-1152. 用户网站访问行为分析

# In[ ]:


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        record = defaultdict(list)
        for i, un in enumerate(username):
            record[un].append([timestamp[i], website[i]]) #对每个人建立档案
 
        row = defaultdict(int)
        for key in record.keys():
            record[key].sort() #把每个人的记录按照时间排序
            used = set()
            for i in range(len(record[key])):
                for j in range(i + 1, len(record[key])):
                    for k in range(j + 1, len(record[key])):
                        sequence = record[key][i][1] + "+" + record[key][j][1]+ "+" + record[key][k][1] #找到新的顺序组合
                        if sequence not in used: #避免同一个人的顺序发生重复
                            row[sequence] += 1
                            used.add(sequence)
        # print row
        possible_sol = []
        max_freq = max(row.values())
        for key, val in row.items():
            if val == max_freq: #找到所有可能的解
                possible_sol.append(key.split("+"))
        possible_sol = possible_sol[::-1]
        # print possible_sol
        if len(possible_sol) > 1:
            possible_sol.sort() #找到最终解，也就是字典序最小的那个解
        return possible_sol[0]


# # 359. Logger Rate Limiter

# In[ ]:


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        

    def shouldPrintMessage(self, timestamp: 'int', message: 'str') -> 'bool':
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.data or timestamp - self.data[message] >= 10:
            self.data[message] = timestamp
            return True
        else:
            return False


# # 356. Line Reflection 直线对称

# In[ ]:


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
        if not points or not points[0]: return True
        rgxVal = [x for x,y in points]
        minxVal = min(rgxVal)
        maxxVal = max(rgxVal)
        pairxVal = minxVal + maxxVal
        pairSet = {}

        for pair in points:
            xVal, yVal = pair
            if xVal == pairxVal/2.0: continue
            curPair = (xVal, yVal)
            pairRef = (pairxVal-xVal, yVal)

            if pairRef in pairSet:
                pairSet[pairRef] -= 1
            else:
                pairSet[curPair] = 1
        for val in pairSet.values():
            if val == 1: return False
        return True


# # 1057. Campus Bikes

# In[ ]:


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pairs = []
        for i,bike in enumerate(bikes):
            for j,worker in enumerate(workers):
                dis = abs(bike[0]-worker[0])+abs(bike[1]-worker[1])
                pairs.append((dis,j,i))
        
        pairs.sort(key = lambda x:(x[0],x[1],x[2]))
        assigned_bikes = set()
        assigned_workers = set()
        
        ans = [0]*len(workers)
        #print(pairs)
        for pair in pairs:
            worker_id = pair[1]
            bike_id = pair[2]
            if worker_id not in assigned_workers and bike_id not in assigned_bikes:
                ans[worker_id] = bike_id
                assigned_workers.add(worker_id)
                assigned_bikes.add(bike_id)
        return ans

