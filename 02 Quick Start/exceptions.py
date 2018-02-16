#!/usr/bin/python3 If only on linex

#try:
#    fh = open('xlines.txt')
#    for line in fh.readlines():
#        print(line)

#except:
#    print('Something wrong happened!!!! {}'.format("really bad"))

#This Try will print out the error
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)

except IOError as ex:
    print('Something wrong happened!!!! {}'.format(ex))


print("After the mess up")

