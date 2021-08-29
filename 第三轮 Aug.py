'''
LC 158. Read N Characters Given Read4 II - Call multiple times
'''
class Solution(object):
    def __init__(self):
        self.__buf4 = [''] * 4
        self.__i4 = 0
        self.__n4 = 0
 
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.__i4 < self.__n4:  # Any characters in buf4.
                buf[i] = self.__buf4[self.__i4]
                i += 1
                self.__i4 += 1
            else:
                self.__n4 = read4(self.__buf4)  # Read more characters.
                if self.__n4:
                    self.__i4 = 0
                else:  # Buffer has been empty.
                    break
 
        return i
 
if __name__ == "__main__":
    global file_content
    sol = Solution()
    buf = ['' for _ in xrange(100)]
    file_content = "ab"
    print(buf[:sol.read(buf, 1)])
    print(buf[:sol.read(buf, 2)])　