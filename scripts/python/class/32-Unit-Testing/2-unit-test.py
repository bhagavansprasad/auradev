import sys
#sys.path.append('/home/bhagavan/training/scripts/python/class/05-Utilities')

import unittest
#import obj_dump_help

def dump_object_help(obj):
    for word in obj:
        print "print \"%-20s :\", cell.%s" %  (word, word)
        print word

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(5))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

#print dir(unittest)
#obj_dump_help.dump_object_help(dir(unittest))
dump_object_help(dir(unittest))
if __name__ == '__main__':
    main()
