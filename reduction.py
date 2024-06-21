
'''
This script "reduces" a number (i.e., adds the digits together until it yields a single digit.)

Reduction is practiced in numerology on numbers of significance such as birth dates. See
"life path numbers".

Presently the script can only handle positive integer inputs of values greater than 10, though
added functionality is planned to test and reject nonhandleable inputs.

'''

'''
COMING SOON
a function for testing if input is a positive integer with no non-numeric characters
def acceptable_number(number):
    number=int(number)
    if number<0:
    print("Sorry, this script does not presently handle negative values.")
    if number // 10 = 0:
        print("Input number is already reduced")
'''

'''
The function "reduction" calls this function to perform one round of adding digits together. If
the returned value is not a single digit, reduction will call this function again.
Input:
    subnumber (integer): the number supplied from the "reduction" function
Output:
    running_total (integer): the value after one round of having all digits added together
'''
def subreduction(subnumber):
    power_of_ten=1
    #begin with value of the last digit
    running_total=subnumber % 10
    while (subnumber // (10 ** power_of_ten)) > 0:
        #take the last digit of the floor division for 10^power_of_ten
        last_digit=(subnumber // 10 ** power_of_ten) % 10
        running_total+=last_digit
        power_of_ten+=1
    return running_total

'''
This function tests if the number is fully reduced and calls "subreduction" until the number is
fully reduced.
Input:
    number (string): the number input from the user
        note: in the future, this ideally will have gone through a test function to ensure the input
        is a positive integer
Output:
    None
'''
def reduction(number):
    temp_number=int(number)
    while temp_number > 10:
        temp_number=subreduction(temp_number)
    print("Your reduced value is " + str(temp_number) + ".")


'''
Prompts the user for an input number, calls the reduction function, then prints the reduced value.
'''
def main():
    input_number=input("Welcome!\
    \n\nThis script \"reduces\" a number (i.e., adds the digits together until it yields a single digit.)\
    \n\nEnter the number you wish to reduce:")
    print("Your input number is " + str(input_number) + ".")
    reduction(input_number)

main()
