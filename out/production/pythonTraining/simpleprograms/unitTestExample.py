__author__ = 'PBrossier'


import unittest

def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size/2 - 1] + copy[size/2]) / 2

class TestMedian(unittest.TestCase):
    def testMedian(self):
        print median([2, 9, 9, 7, 9, 2, 4, 5, 8])
        print '\n'
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

if __name__ == '__main__':
    unittest.main()