import re
from collections import Counter
from itertools import chain
hcl = '#asf453'
valid = re.match('^[\w-]+$', hcl[1:]) is not None
print(valid)

teststr = "muted coral bags contain 1 bright magenta bag, 1 dim aqua bag."
teststr2 = 'dotted black bags contain no other bags.'

match = re.match('(.*) bag(.*) bag(.*)', teststr)
print(match.group(2))

step1 = re.sub('bag', '', teststr)
print(step1)
step2 = re.sub('(s contain [0-9])*', '', step1)
print(step2)
step3 = re.sub('(, [0-9])*', '', step2)
print(step3)

input = (re.findall('([a-z]+ [a-z]+) bag', teststr))
print(input)

bagDict = dict()
bagDict[input[0]] = input[1:]
print(bagDict)
for subBag in bagDict['muted coral']:
    print(subBag)
teststr = '14 bright magenta bag'
print(teststr)
print(re.findall('([a-z]+ [a-z]+) bag', teststr))
print(re.findall('(^[0-9]*)', teststr)[0])

