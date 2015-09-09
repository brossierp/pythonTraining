__author__ = 'PBrossier'


# Import module regular expression
import re


# Code from https://wiki.python.org/moin/SimplePrograms
print 'Hello, world!\n'


# To get input from user
inputName = raw_input('What is your name?\n')
print 'Hi, %s \n' % inputName


print 'With format method -- Hi, {} \n'.format(inputName)


friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iterationPlaceHolder} is {namePlaceHolder}".format(iterationPlaceHolder=i, namePlaceHolder=name)
print '\n'

parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)
print '\n'


# Defining a function
def greet(name):
    print 'Hello', name
greet('Jack')
greet('Jill')
greet('Bob')
print '\n'


for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'
print '\n'