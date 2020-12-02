def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def split_pw(input):
    rule = input.split(': ')[0]
    min_max = rule.split(' ')[0].split('-')
    char = rule.split(' ')[1]
    pw = input.split(': ')[1].rstrip()
    min_max.insert(2, char)
    min_max.insert(3, pw)
    return min_max

def count_letters(rule):
    char_count = rule[3].count(rule[2])
    return char_count

def main():
    input = read_input("input/2_1_input.txt")
    #print(split_pw(input[1]))
    #a = count_letters(split_pw(input[1]))
    #print (a)
    correct_count = 0
    for i in input:
        min = int(split_pw(i)[0])
        max = int(split_pw(i)[1])
        a = int(count_letters(split_pw(i)))
        if a in range(min, max+1):
            correct_count += 1


    print("Count of correct pws: ", correct_count)

if __name__ == "__main__":
    main()
