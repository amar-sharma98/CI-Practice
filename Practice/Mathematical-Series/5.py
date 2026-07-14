#Print first n terms of a geometric pregressionfor the given first term and common ratio

# Geometric Progression (GP) with:
# First term = a
# Common ratio = r
# ✅ First n Terms of GP
# The sequence is:
# a,  ar,  ar2,  ar3,  …,  arn−1a,\; ar,\; ar^2,\; ar^3,\; \dots,\; ar^{n-1}a,ar,ar2,ar3,…,arn−1

# ✅ General Formula for nth Term
# T = a * r ^ n−1

a = int(input("Enter the first term(a): "))
r = int(input("Enter the common ratio(r): "))
n = int(input("Enter the number of terms(n): "))

print("First", n, "terms of the GP are:")
for i in range(n):
    terms = a * (r ** i)
    print(terms, end=",")