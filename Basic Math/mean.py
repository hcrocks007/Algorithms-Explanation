def mean_calculator():
    # First we take the list of numbers 

    list_of_numbers = input('Enter numbers').split(' ')

    # Calculating sum

    sum_of_numbers = 0
    for i in range(0,len(list_of_numbers)):
        sum_of_numbers = sum_of_numbers + int(list_of_numbers[i])

    # Counting the numbers in the list

    count = len(list_of_numbers)

    # Calculating mean

    mean = sum_of_numbers / count
    
    # Returning mean
    
    return mean

