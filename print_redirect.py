import sys

logfile = open("log.txt", 'a')
print >> logfile, 'Fatal error: invalid input!'
logfile.close()

filename = raw_input('Enter file name: ')
fobj = open(filename, 'r')

for eachLine in fobj:
    print eachLine,

fobj.close()

"""
try:
    filename = raw_input('Enter the file name: ')
    fobj = open(filename, 'r')
    for eachLine in fobj:
        print eachLine,
    fobj.close()
except IOError, e:
    print 'file open error:', e

def addMe2Me(x=1):
    return x + x

print addMe2Me(4.25)
print addMe2Me(13423)
print addMe2Me('Python')
print addMe2Me([-1, 'abc'])
print addMe2Me()
"""

class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1 #class (data) attribute
    x = 2
    def __init__(self, nm='John Doe'):
        self.name = nm
        print 'Created a class instance for', nm
        
    def showname(self):
        print "Your name is", self.name
        print "My name is", self.__class__.__name__

    def showver(self):
        print self.version

    def addMe2Me(self, x = 1):
        return x + x

foo = FooClass()
foo.showname()
foo.showver()
print foo.addMe2Me()
print foo.addMe2Me('xyz')
