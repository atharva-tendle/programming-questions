def is_leap(year):
    """
    This function takes in a year(integer) and checks if it is a leap year 
    params:
        - year: integer describing the year
    returns:
        - True/False based on if the year is a leap year or not
    """
    
    leap = False
    # check if year is divisible by 4
    if year % 4 == 0:
        # check if its divisible by 100
        if year % 100 == 0:
            # check if its divisible by 400
            if year % 400 ==0:
                leap = True
            else:
                leap = False
        else:
            leap = True

    return leap