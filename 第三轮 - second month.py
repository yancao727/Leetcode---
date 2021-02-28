#!/usr/bin/env python
# coding: utf-8

# # 1428 Leftmost Column with at Least a One

# In[ ]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        #TC: max O(row + col)
        #SC: O(1)

        total_row, total_col = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]

        row = total_row - 1
        col = total_col - 1

        res = total_col

        while(row >= 0 and col >= 0):
            if binaryMatrix.get(row, col) == 1:
                res = min(res, col)
                col -= 1
            else:
                row -= 1

        if res == total_col:
            return -1
        else:
            return res


# # 1152. 用户网站访问行为分析

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


# # 723. Candy Crush

# In[ ]:


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        row,col = len(board),len(board[0])
        todo = False
        
        for r in range(row-2):
            for c in range(col):
                if abs(board[r][c])==abs(board[r+1][c])==abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True
        
        for r in range(row):
            for c in range(col-2):
                if abs(board[r][c])==abs(board[r][c+1])==abs(board[r][c+2]) != 0:
                    board[r][c]=board[r][c+1]=board[r][c+2]=-abs(board[r][c])
                    todo = True
        
        for c in range(col):
            wp = row-1
            for r in range(row-1,-1,-1):
                if board[r][c]>0:
                    board[wp][c] = board[r][c]
                    wp -= 1
            
            for wp in range(wp,-1,-1):
                board[wp][c] = 0
        
        return self.candyCrush(board) if todo else board


# # 1229. 安排会议日程

# In[ ]:


class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1 = sorted(slots1, key = lambda x:x[0])
        slots2 = sorted(slots2, key = lambda x:x[0])
        
        slots = []
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] < slots2[j][0]:
                i += 1
                continue
            elif slots1[i][0] > slots2[j][1]:
                j += 1
                continue
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            slots.append([start, end])
            i += 1
                
        for start, end in slots:
            if end - start >= duration:
                return [start, start + duration]
            
        return []

