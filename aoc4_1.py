import re

def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out

def data_check(input, test_strs):
    checkcount = 0
    for i in test_strs:
        if i in input:
            checkcount += 1
    return checkcount == len(test_strs)

def byr_test(byr):
    retval = False
    try:
        if int(byr) >= 1920 and int(byr) <= 2002:
            retval = True
    except:
        print("byr Virhe! ", byr)
    return retval

def iyr_test(iyr):
    retval = False
    try:
        if int(iyr) >= 2010 and int(iyr) <= 2020:
            retval = True
    except:
        print("Iyr Virhe! ", iyr)
    return retval

def eyr_test(eyr):
    retval = False
    try:
        if int(eyr) >= 2020 and int(eyr) <= 2030:
            retval = True
    except:
        print("Eyr Virhe! ", eyr)
    return retval

def hgt_test(hgt):
    retval = False
    match = re.match(r"([0-9]+)([a-z]+)", hgt, re.I)
    if match:
        items = match.groups()
    try:
        if items[1] == "cm":
            if int(items[0].strip()) >= 150 and int(items[0].strip()) <= 193:
                retval = True
        elif items[1] == "in":
            if int(items[0].strip()) >= 59 and int(items[0].strip()) <= 76:
                retval = True
    except:
        print("hgt Virhe! ", hgt, " ", retval)
    return retval

def hcl_test(hcl):
    retval = False
    try:
        if len(hcl) == 7:
            if hcl[0] == "#":
                if re.match('^[\w-]+$', hcl[1:]) is not None:
                    retval = True
    except:
        print("Hcl Virhe! ", hcl)
    return retval

def ecl_test(ecl):
    retval = False
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    try:
        if ecl in ecl_list:
            retval = True
    except:
        print("Ecl Virhe! ", ecl)
    return retval

def pid_test(pid):
    retval = False
    try:
        if re.match('^[0-9]{9}$', pid) is not None:
            retval = True
    except:
        print("Pid Virhe! ", pid)
    return retval

def main():
    input = read_input("input/4_1_input.txt")
    #input = read_input("4_1testinput.txt")
    #print(input)
    test_strs = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

    id_data = ""
    id_array = []
    for i in input:
        if i != "\n":
            # print(i.rstrip())
            id_data += str(i.rstrip())
            id_data += " "
        else:
            #print(id_data)
            id_array.append(id_data)
            id_data = ""

    id_array.append(id_data)

    #print(id_array)
    testres = data_check(id_array[0], test_strs)
    #print(id_array[0])
    #print(testres)
    print("array on näin pitkä: ", len(id_array))
    #pw_test = []
    ok_ids = 0
    for i in range(0, len(id_array)):

        testres = data_check(id_array[i], test_strs)
        if testres == False:
            continue
        pw_split = id_array[i].split()

        fieldtest = 0
        for j in pw_split:
            fields = j.split(":")
            #print(fields)
            if fields[0] == "byr":
                fieldtest += int(byr_test(fields[1]))
            elif fields[0] == 'iyr':
                fieldtest += int(iyr_test(fields[1]))
            elif fields[0] == 'eyr':
                fieldtest += int(eyr_test(fields[1]))
            elif fields[0] == 'hgt':
                fieldtest += int(hgt_test(fields[1]))
            elif fields[0] == 'hcl':
                fieldtest += int(hcl_test(fields[1]))
            elif fields[0] == 'ecl':
                fieldtest += int(ecl_test(fields[1]))
            elif fields[0] == 'pid':
                fieldtest += int(pid_test(fields[1]))
        #print(fieldtest)
        if fieldtest == 7:
            ok_ids += 1

    print("Good ids: ", ok_ids)

if __name__ == "__main__":
    main()
