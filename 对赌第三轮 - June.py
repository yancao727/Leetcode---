#!/usr/bin/env python
# coding: utf-8

# # 353. Design Snake Game

# In[ ]:


from collections import deque

class SnakeGame(object):
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food = food + [ [-1,-1] ]
        self.foodInx = 0

        self.bodyQueue = deque( [ (0,0) ] ) # snake head on the right, tail on the left
        self.bodySet = { (0,0) }

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """

        oldHead = self.bodyQueue[-1]
        newHead = ( oldHead[0] + int(direction=='D') - int(direction=='U'),
                    oldHead[1] + int(direction=='R') - int(direction=='L') )

        # hit wall?
        if not ( 0<=newHead[0]<self.height and 0<=newHead[1]<self.width ):
            return -1

        # eat foot?
        eatFood = ( newHead == tuple( self.food[ self.foodInx ] ) )
        if eatFood:
            self.foodInx += 1

        # shrink tail
        if not eatFood:
            oldTail = self.bodyQueue.popleft()
            self.bodySet.remove( oldTail )

        # hit self?
        if newHead in self.bodySet:
            return -1

        # grow head
        self.bodyQueue.append( newHead )
        self.bodySet.add( newHead )

        # score is body length - 1
        return len(self.bodySet) - 1


# # 253. Meeting Rooms II 

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


# # 1152 Analyze User Website Visit Pattern

# In[ ]:


import collections
import itertools


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        lookup = collections.defaultdict(list)
        A = zip(timestamp, username, website)
        A.sort()
        for t, u, w in A:
            lookup[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(lookup[u], 3))) for u in lookup], collections.Counter())
        return list(min(count, key=lambda x: (-count[x], x)))

