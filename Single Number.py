import unittest

class unitest(unittest.TestCase):
    def testSample(self):
        Input = [1,1,2]
        Output = 2
        self.assertEqual(Solution().singleNumber(Input),Output);

class Solution():
    def singleNumber(self, nums):
        Ans = 0
        for i in nums:
            Ans ^= i
        return Ans

if __name__ == '__main__':
    unittest.main()
