# initialise list
numbers = []

# stupid function to build list
def buildlist(num,numberlist):
    i = 0
    while i < num:
        print "At the top i is %d" % i
        numberlist.append(i)

        i = i + 1
        print "Number now: ", numberlist
        print "At the botton i is %d" % i

buildlist(10, numbers)

# print numbers in list
print "The numbers: "

for num in numbers:
    print num
