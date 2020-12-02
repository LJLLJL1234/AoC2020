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

def count_letters_2(rule):
    char1 = rule[3][int(rule[0])-1]
    char2 = rule[3][int(rule[1])-1]
    chars = [char1, char2]
    charcount = 0
    for c in chars:
        if c == rule[2]:
            charcount +=1
    return charcount

def main():
    input = read_input("input/2_1_input.txt")

    correct_count = 0

    for i in input:
        pw_split = split_pw(i)
        charcount = count_letters_2(pw_split)
        if charcount == 1:
            correct_count += 1

    print("Count of correct pws: ", correct_count)

if __name__ == "__main__":
    main()
