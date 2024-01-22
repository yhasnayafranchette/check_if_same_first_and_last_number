#Exercise 5: Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Compare the first and last numbers
def first_and_last_number(number_list):
    print("Given list:", number_list)
    if first_and_last_number:
        return first_and_last_number[0] == first_and_last_number[-1]
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

result_x = first_and_last_number(numbers_x)
result_y = first_and_last_number(numbers_y)

#Print output
print("For numbers_x:", result_x)
print("For numbers_y:", result_y) 