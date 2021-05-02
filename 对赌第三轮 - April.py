#!/usr/bin/env python
# coding: utf-8

# LeetCode 1570 Dot Product of Two Sparse Vectors 

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

