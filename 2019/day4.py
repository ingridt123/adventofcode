# six digits
# value in range
# two adjacent digits are same
# digits never decrease

# part 2: no more than 2 matching adjacent digits

string = "129334"
integer = int(string)

maxDigit = 9 + 1

def findPassword(min, max):
    count = 0
    for one in range(min//10**5, max//10**5+1):
    # for one in range(min//10**5, min//10**5+1):
        for two in range(one, maxDigit):
            for three in range(two, maxDigit):
                for four in range(three, maxDigit):
                    for five in range(four, maxDigit):
                        for six in range(five, maxDigit):
                            num = int(str(one) + str(two) + str(three) + str(four) + str(five) + str(six))
                            if num > max:
                                return count
                            checks = [one == two, two == three, three == four, four == five, five == six]
                            check_bool = False
                            for i in range(0,len(checks)):
                                if (checks[i] == True) and ((i == 0 and checks[i+1] != True) or (i == len(checks)-1 and checks[i-1] != True)):
                                    check_bool = True
                                    break
                                elif (checks[i-1] != True) and (checks[i] == True) and (checks[i+1] != True):
                                    check_bool = True
                                    break
                            if check_bool:
                                # print(num, checks)
                                count += 1
                            # else:
                            #     print(num)
                            # if one == two or two == three or three == four or four == five or five == six:
                            #     count += 1
    return count

min = 206938
max = 679128

print(findPassword(min, max))