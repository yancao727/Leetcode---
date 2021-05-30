#!/usr/bin/env python
# coding: utf-8

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


# # 296. Best Meeting Point

# In[ ]:


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        locs = []

        m = len(grid)
        n = len(grid[0]) if m else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    locs.append([i,j])


        locs.sort(key = lambda point: point[0])
        x = locs[len(locs)/2][0]
        for point in locs:
        	res += abs(point[0] - x)

        locs.sort(key = lambda point: point[1])
        y = locs[len(locs)/2][1]
        for point in locs:
        	res += abs(point[1] - y)

        return res


# # 1060 Missing Element in Sorted Array

# In[ ]:


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
        return nums[left] + k # k should be between left and right index in the end

