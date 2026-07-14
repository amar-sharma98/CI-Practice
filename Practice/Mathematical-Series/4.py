#Print first n terms of an arithmetic progression of the given first term and common difference

#Sum: S=n/2​[2a+(n−1)d]
#Terms: a+(n−1)d => a + i * d because i starts from 0 so i == (n-1)

# Input values
a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter number of terms (n): "))

# Print AP
print("First", n, "terms of the AP are:")
for i in range(n):
    term = a + i * d
    print(term, end=" ")