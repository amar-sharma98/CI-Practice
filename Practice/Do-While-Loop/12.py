#Menu Driven Program

def factorial(num):
    if num < 0:
        return None
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result


def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    return original == rev


def is_armstrong(num):
    original = num
    n = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** n
        num //= 10
    return original == total


def hcf(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result


def minimum(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


# ✅ Menu-driven program
while True:
    print("\n--- MENU ---")
    print("1. Factorial")
    print("2. Palindrome Check")
    print("3. Armstrong Check")
    print("4. HCF of numbers")
    print("5. Minimum of numbers")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Factorial:", factorial(num))

    elif choice == 2:
        num = int(input("Enter a number: "))
        print("Palindrome" if is_palindrome(num) else "Not Palindrome")

    elif choice == 3:
        num = int(input("Enter a number: "))
        print("Armstrong Number" if is_armstrong(num) else "Not Armstrong")

    elif choice == 4:
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        print("HCF:", hcf(nums))

    elif choice == 5:
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        print("Minimum:", minimum(nums))

    elif choice == 0:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
