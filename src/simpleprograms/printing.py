__author__ = 'PBrossier'

# Code from https://wiki.python.org/moin/SimplePrograms
print 'Hello, world!\n'


# To get input from user
inputName = raw_input('What is your name?\n')
print 'Hi, %s \n' % inputName


print 'With format method -- Hi, {} \n'.format(inputName)


friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iterationPlaceHolder} is {namePlaceHolder}".format(iterationPlaceHolder=i, namePlaceHolder=name)