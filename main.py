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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
