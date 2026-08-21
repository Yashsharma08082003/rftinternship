# Check if a number is prime
def check_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Find the largest number from any number of inputs
def find_largest(*numbers):
    if len(numbers) == 0:
        return None

    return max(numbers)

# Display student details
def show_student_info(**details):
    print("\nStudent Details:")
    
    for key, value in details.items():
        print(key.capitalize(), ":", value)

# Find maximum, minimum, average and sum of a list
def get_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return max(numbers), min(numbers), average, total

# Checking whether a number is prime
number = 17

if check_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# Finding the largest number
largest = find_largest(10, 45, 23, 89, 67)
print("\nLargest number:", largest)

# Displaying student information
show_student_info(
    name="Yash",
    age=20,
    course="Python Internship",
    college="Gyan Ganga Institute"
)

# Finding statistics of a list
numbers = [10, 20, 30, 40, 50]

maximum, minimum, average, total = get_statistics(numbers)
print("\nList Statistics:")
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Sum:", total)