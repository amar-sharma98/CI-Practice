#Calculate and print the value of the series 1 + 1/2 + 1/3 + .... + 1/n

def cal_factor_sum(n):
    result = 0.0

    for m in range(1, n+1):
        print(f"1/{m}", end=" + ")
        result += 1/m

    return result

print(cal_factor_sum(10))