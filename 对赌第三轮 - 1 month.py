#!/usr/bin/env python
# coding: utf-8

# # 1244. 力扣排行榜

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
                
 
    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.dic[playerId] = 0


# # 253 Meeting Rooms II 

# In[ ]:


def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0]>=heap[0]:
                heapq.heappushpop(heap,interval[1])
            else:
                heapq.heappush(heap,interval[1])
        return len(heap)


# # Employee Free Time

# In[ ]:


def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        # flatten the nested list
        lst = []
        for itvs in schedule:
            for itv in itvs:
                lst.append([itv[S], S])
                lst.append([itv[E], E])

        lst.sort()
        count = 0
        prev = None
        ret = []
        for t, flag in lst:
            if count == 0 and prev:
                ret.append([prev, t])

            if flag == S:
                count += 1
            else:
                prev = t
                count -= 1

        return ret

