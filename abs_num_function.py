def abs_num(num):
    """
    This function make to find meter of the numbers
    :param num:
    :return:
    """
    if num>0:
        return num
    else:
        num=num*(-1)
        return num

print(abs_num.__doc__)
