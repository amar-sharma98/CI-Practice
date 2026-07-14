#Find the number between 1 and n that has the maximum digit sum, and print the number along with digit sum

def digit_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n//=10
    return total

def max_digit_sum(end):
    max_sum = -1
    max_num = 0
    for i in range(1, end + 1):
        current_sum = digit_sum(i)
        if current_sum > max_sum:
            max_sum = current_sum
            max_num = i
    return max_num, max_sum

# Example usage
n = int(input("Enter n: "))
number, digit_sum_value = max_digit_sum(n)
print("Number:", number)
print("Digit Sum:", digit_sum_value)