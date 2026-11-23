
import statistics

# 1. Function to calculate the sum of a list of numbers
def sum_of_numbers(numbers):
    return sum(numbers)


# 2. Function to calculate the average (mean)
def average(numbers):
    return statistics.mean(numbers)


# 3. Function to return the median and mode
def median_and_mode(numbers):
    median = statistics.median(numbers)
    mode = statistics.multimode(numbers)

    return median, mode


# Testing the functions
numbers = [2, 4, 4, 6, 8, 10]

print("Sum:", sum_of_numbers(numbers))
print("Average:", average(numbers))
print("Median and Mode:", median_and_mode(numbers))
