#!/usr/bin/env python
# coding: utf-8

# # 269. Alien Dictionary
# 
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
# 
# For example,
# Given the following words in dictionary,
# 
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#  
# 
# The correct order is: "wertf".
# 
# Note:
# 
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# In[ ]:


# BFS 入读为0的char先加入deque，其char的链接char入度都-1，变成0后加入deque，如此反复
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result, zero_in_degree_queue, in_degree, out_degree = [], collections.deque(), {}, {}
        nodes = sets.Set()
        for word in words:
            for c in word:
                nodes.add(c)
         
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and                 words[i-1][:len(words[i])] == words[i]:
                    return ""
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)
         
        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)
         
        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            result.append(precedence)
             
            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)
             
                del out_degree[precedence]
         
        if out_degree:
            return ""
 
        return "".join(result)
 
 
    # Construct the graph.
    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in range(str_len):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = sets.Set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = sets.Set()
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break　　


# In[ ]:


# DFS 把出度为0的先加入result
class Solution2(object):
    def alienOrder(self, words):
        # Find ancestors of each node by DFS.
        nodes, ancestors = sets.Set(), {}
        for i in range(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            ancestors[node] = []
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and                 words[i-1][:len(words[i])] == words[i]:
                    return ""
            self.findEdges(words[i - 1], words[i], ancestors)
 
        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""
         
        return "".join(result)
 
 
    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break
 
 
    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False


# # LeetCode 444. Sequence Reconstruction
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
# 
# Example 1:
# 
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
# 
# Output:
# false
# 
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# 
# ### 解法I 拓扑排序（Topological Sort）
# 将seqs中的各序列seq按照其中元素出现的先后顺序建立有向图g。
# 
# 例如seqs中的某序列seq = [1, 2, 3]，对应有向图，顶点为1, 2, 3；边为(1, 2), (2, 3)。
# 
# 利用数组indeg记录各顶点的入度（indegree），sucset记录各顶点的后继（边）。
# 
# 然后对图g执行拓扑排序，将得到的排序结果与原始序列org作比对即可。

# In[ ]:


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        size = len(org)
        indeg = [0] * size
        sucset = [set() for x in range(size)]
        if not seqs: return False
        for seq in seqs:
            if any(s > size or s < 1 for s in seq):
                return False
            for i in range(1, len(seq)):
                if seq[i] not in sucset[seq[i - 1] - 1]:
                    indeg[seq[i] - 1] += 1
                    sucset[seq[i - 1] - 1].add(seq[i])

        q = [i for i in org if not indeg[i - 1]]
        for x in range(size):
            if len(q) != 1 or q[0] != org[x]:
                return False
            nq = []
            for suc in sucset[q[0] - 1]:
                indeg[suc - 1] -= 1
                if not indeg[suc - 1]:
                    nq.append(suc)
            q = nq
        return True


# # 1500. Design a File Sharing System
# We will use a file-sharing system to share a very large file which consists of m small chunks with IDs from 1 to m.
# 
# When users join the system, the system should assign a unique ID to them. The unique ID should be used once for each user, but when a user leaves the system, the ID can be reused again.
# 
# Users can request a certain chunk of the file, the system should return a list of IDs of all the users who own this chunk. If the user receive a non-empty list of IDs, they receive the requested chunk successfully.
# 
# Implement the FileSharing class:
# 
# 1. FileSharing(int m) Initializes the object with a file of m chunks.
# 2. int join(int[] ownedChunks): A new user joined the system owning some chunks of the file, the system should assign an id to the user which is the smallest positive integer not taken by any other user. Return the assigned id.
# 3. void leave(int userID): The user with userID will leave the system, you cannot take file chunks from them anymore.
# 4. int[] request(int userID, int chunkID): The user userID requested the file chunk with chunkID. Return a list of the IDs of all users that own this chunk sorted in ascending order.

# In[ ]:


import heapq as h
class FileSharing:

    def __init__(self, m: int):
        self.id2chk = collections.defaultdict(set)# save id-{chunks they have}
        self.avaid = [i for i in range(1, 100)]# 1-100 userid
        h.heapify(self.avaid)
        

    def join(self, ownedChunks: List[int]) -> int:
        new_id = h.heappop(self.avaid)# get smallest available userid
        for oc in ownedChunks:
            self.id2chk[new_id].add(oc)
        return new_id

    def leave(self, userID: int) -> None:
        if(userID not in self.avaid):
            self.id2chk[userID] = set()# clean this user's chunks
            h.heappush(self.avaid, userID)# available this userid
        else:
            return

    def request(self, userID: int, chunkID: int) -> List[int]:
        temp = []
        for uid, chk in self.id2chk.items():
            if(chunkID in chk):
                temp.append(uid)
        if(temp != []):
            self.id2chk[userID].add(chunkID)
        return sorted(temp)

