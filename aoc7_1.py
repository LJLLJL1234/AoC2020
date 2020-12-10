import re

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def search_bag(testBag, bagDict, searchBag):
    found = False
    #print(testBag)
    for subBag in bagDict[testBag]:
        if subBag != 'no other':
            if subBag == 'shiny gold':
                #print("Löytyi!!!", testBag, ": ", subBag)
                found = True
            if search_bag(subBag, bagDict, searchBag):
                found = True
    return found

def main():
    input = read_input("input/7_1input.txt")
    bagDict = dict()
    for i in input:
        tempBag = re.findall('([a-z]+ [a-z]+) bag', i)
        bagDict[tempBag[0]] = tempBag[1:]

    check_counter = 0
    for i in bagDict:
        check = search_bag(i, bagDict, 'shiny gold')
        check_counter += check

    print(check_counter)

if __name__ == "__main__":
    main()

#while temp_bag not 'no other'
#    contents = find_bags(temp_bag)
#    if contents = shiny yellog:
#        stop
