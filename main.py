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

    selection = 'C'

    while selection.upper() != 'Z':

        print('##################################')
        print('#                                #')
        print('#    O P T I O N S    M E N U    #')
        print('#                                #')
        print('#    1 - Hello World             #')
        print('#    2 - Rectangle Area          #')
        print('#    3 - Square Area             #')
        print('#    4 - Triangle Area           #')
        print('#    5 - Progressive Counting    #')
        print('#    6 - Support Candidate       #')
        print('#    7 - PLIM                    #')
        print('#                                #')
        print('#    Z - Exit                    #')
        print('#                                #')
        print('##################################')

        selection = input('Select your option: ')
        print(f'You have selected option: {selection}')

        if selection.upper() != 'Z':
            if selection == '1':
                print_hi('Ricardo Rosinha')
            elif selection == '2':
                result = calculate_rectangle_area(8, 9)
                print(f'The rectangle is {result} m²!')
            elif selection == '3':
                result = calculate_square_area(7)
                print(f'The square is {result} m²!')
            elif selection == '4':
                result = calculate_triangle_area(5, 4)
                print(f'The triangle is {result} m²!')
            elif selection == '5':
                progressive_counting(11)
            elif selection == '6':
                support_candidate('Ricardo Rosinha', 10)
            elif selection == '7':
                plim_play(20)
            else:
                print('Invalid option, please select a valid option.')
        else:
            print('You have selected to exit. Thank you and return soon')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
