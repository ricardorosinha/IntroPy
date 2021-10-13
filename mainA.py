# 1 - import / libraries


# 2 - Classes


# 3 - Methods and Functions
# def = definition
def print_hi(name):
    print(f'Hi, {name}') # only in Python3+
    print('Hello, ' + name) # before Python3

def calculate_rectangle_area(width, length):
    return width * length

def calculate_square_area(side):
    return side * side # ou side **

def calculate_triangle_area(width, height):
    return (width * height) / 2

def progressive_counting(end):
    for number in range(end): # repeats from number (starts in 0) the block until it reaches end number
        print(number) # print number in console

def support_candidate(name, times):
    for number in range(times):
        # counter = number + 1
        # print(f'{counter} - {name}')

        if number < 9:
            print(f'00{number + 1} - {name}')
        elif number < 99:
            print(f'0{number + 1} - {name}')
        else:
            print(number + 1, '-', name)

def plim_play(end):
    for number in range(1, end + 1):
        if number % 4 == 0: # searching for multiples of 4
            print('PLIM!')
        else:
            print('{:0>4}'.format(number)) # number format

def display_week_day_if(number):
    print('Execution with IF - ELIF - ELSE')
    if number == 1:
        print('The day is Monday')
    elif number == 2:
        print('The day is Tuesday')
    elif number == 3:
        print('The day is Wednesday')
    elif number == 4:
        print('The day is Thursday')
    elif number == 5:
        print('The day is Friday')
    elif number == 6:
        print('The day is Saturday')
    elif number == 7:
        print('The day is Sunday')
    else:
        print('Not a week day! Number must be within 1 (Monday) - 7 (Sunday)')

''' ONLY WORKS AFTER PYTHON 3.10+
def display_week_day_match(number):
    print('Execution with Match')
    match number.:
        case 1:
            print('The day is Monday')
            exit()
        case 2:
            print('The day is Tuesday')
            exit()
        case 3:
            print('The day is Wednesday')
            exit()
        case 4:
            print('The day is Thursday')
            exit()
        case 5:
            print('The day is Friday')
            exit()
        case 6:
            print('The day is Saturday')
            exit()
        case 7:
            print('The day is Sunday')
            exit()
        case _:
            print('Not a week day! Number must be within 1 (Monday) - 7 (Sunday)')
'''

def stop_or_continue_play():
    response = 'C' # C to continue

    #while response == 'C' or response == 'c':
    while response.upper() == 'C':
        response = input('Input C to Continue or any other character to stop: ')

    print('You have decided to stop with the play')

# Press the green button in the gutter to run the script. Above we write the functions/methods and below we call them
if __name__ == '__main__':
    print_hi('Ricardo Rosinha')

    # call function calculate rectangle area
    result = calculate_rectangle_area(3,4)
    print(f'The rectangle area is {result} m²!')

    # call function calculate square area
    result = calculate_square_area(5)
    print(f'The square area is {result} m²!')

    # call function calculate triangle area
    result = calculate_triangle_area(6, 7)
    print(f'The triangle area is {result} m²!')

    # call function progressive counting
    progressive_counting(11)

    # call function to support candidate
    support_candidate('Ricardo Rosinha', 100)

    # call PLIM function
    plim_play(100)

    # week day example with "if - elif - else" - week day starts on Monday
    display_week_day_if(7)

    # ONLY FOR PYTHON 3.10+
    # week day example with "match - case" - week day starts on Monday
    # display_week_day_match(1)

    # While example - stop or continue
    stop_or_continue_play()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
