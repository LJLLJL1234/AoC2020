import re

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def loop_bags(testBag, bagDict):
    counter = 0
    print("Testbag: ", testBag)
    for bag in bagDict[testBag]:
        if re.findall('([a-z]+ [a-z]+)', bag)[0].lstrip() != 'no other':
            print("bag: ", bag)
            subBag = re.findall('([a-z]+ [a-z]+)', bag)[0].lstrip()

            print("subBag: ", subBag)
            parentCount = re.findall('(^[0-9]*)',bag)[0]
            print("ParentCount :", parentCount)
            counter += int(parentCount)
            childCount = int(loop_bags(subBag, bagDict)) * parentCount
            print("childCount: ", childCount)
            #parentCount
            counter += childCount

    return counter

def main():
    input = read_input("input/7_1input.txt")
    bagDict = dict()
    for i in input:
        mainBag = re.findall('([a-z]+ [a-z]+) bags contain', i)
        childBags = re.findall('([0-9]* [a-z]+ [a-z]+) bag', i)
        bagDict[mainBag[0]] = childBags[0:]

    #print(bagDict)

    res = loop_bags('shiny gold', bagDict)
    #print(res)



if __name__ == "__main__":
    main()

#while temp_bag not 'no other'
#    contents = find_bags(temp_bag)
#    if contents = shiny yellog:
#        stop
