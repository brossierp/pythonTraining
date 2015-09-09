__author__ = 'PBrossier'


import glob # Unix style pathname pattern expansion
import re   # Regular expressions
import sys  # System-specific parameters and functions
from time import localtime


# Code from https://wiki.python.org/moin/SimplePrograms
print 'Hello, world!\n'


# To get input from user
#inputName = raw_input('What is your name?\n')
#print 'Hi, %s \n' % inputName
#print 'With format method -- Hi, {} \n'.format(inputName)


# The for loop
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iterationPlaceHolder} is {namePlaceHolder}".format(iterationPlaceHolder=i, namePlaceHolder=name)
print '\n'


# The while loop and Tuple
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


# Using the re module
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'
print '\n'


# Data type dictionary
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
print 'I owe the grocer $%.3f' % grocery_bill
print 'I owe the grocer ${:.3f}'.format(grocery_bill)
print 'Is orange a key of the dictionay prices?', 'orange' in prices
print 'Is apple a key of the dictionay prices?', 'apple' in prices
print 'Give me all keys of the dictionay prices', prices.keys()
print '\n'


# Grab script parameters and Exception handling
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print 'sum =', total
except ValueError:
    print 'Please supply integer arguments'
print '\n'


# Read from file
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print '------' + file_name

    with open(file_name) as f:
        for line in f:
            print line.rstrip()

    print
print '\n'


# Import specific function and If test
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}
time_now = localtime()
hour = time_now.tm_hour
for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
print '\n'


# Triple-quoted string and While loop
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 99
while bottles_of_beer > 1:
    print REFRAIN % (bottles_of_beer, bottles_of_beer,
                     bottles_of_beer - 1)
    bottles_of_beer -= 1
print '\n'
