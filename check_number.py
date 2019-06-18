def is_happy(num):
    ''' (int) -> bool

    Return if the number is happy number

    #TODO:
        >>> is_happy(13)
        True
        >>> is_happy(167)
        True
        >>> is_happy(89)
        False
    '''
    list_of_digit = []
    count = 1

    while (len(list_of_digit) >= 1) or (list_of_digit == []):
        list_of_digit = []
        sum = 0

        for each_digit in range(len(str(num))):
            list_of_digit.append(num % 10)
            num //= 10

        for each in list_of_digit:
            sum += each**2
        num = sum
        if num == 1:
            return True

        count +=1
        if count > 100:
            return False

    return False


def ulam_n(num):
    ''' (int) -> bool

    Return if the number is Ulam number

    #TODO:
        >>> ulam_n(18)
        True
        >>> ulam_n(131)
        True
        >>> ulam_n(5)
        False
    '''
    ulam_num = [1, 2, 3]

    for i in range(4, num + 1):
        count = 0
        for j in range(1, (i//2) + 1):
            if j in ulam_num and i-j in ulam_num:
                if j != i - j:
                    if count != 1:
                        ulam_num.append(i)
                    count += 1
                if count > 1:
                    ulam_num.pop()
                    break

    if ulam_num[-1] == num:
        return True
    else:
        return False

def is_even(num):
    '''
    (int) -> bool

    Return if the number is even  number

    #TODO:
        >>> is_even(4)
        True
        >>> is_even(25)
        False
    '''
    if num % 2 == 0:
        return True
    else:
        return False
