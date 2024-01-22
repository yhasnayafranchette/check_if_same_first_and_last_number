#Exercise 5: Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Compare the first and last numbers
def first_and_last_number(number_list):
    print("Given list:", number_list)

    first_number = number_list[0]
    last_number = number_list[-1]

    if first_number == last_number:
        return True
    else:
        return False

#Print output
numbers_x = [10, 20, 30, 40, 10]
print("For numbers_x:", first_and_last_number(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("For numbers_y:", first_and_last_number(numbers_y)) 