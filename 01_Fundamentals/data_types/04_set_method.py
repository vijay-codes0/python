# MORE SET METHODS

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)


# 1 union() – combine both sets
print("Union:", a.union(b))


# 2 intersection() – common elements
print("Intersection:", a.intersection(b))


# 3 difference() – elements in A not in B
print("Difference A-B:", a.difference(b))


# 4 symmetric_difference() – elements not common
print("Symmetric Difference:", a.symmetric_difference(b))


# 5 issubset() – check if A is subset of B
print("Is subset:", a.issubset(b))


# 6 issuperset() – check if A is superset of B
print("Is superset:", a.issuperset(b))


# 7 isdisjoint() – check if sets have no common elements
print("Is disjoint:", a.isdisjoint(b))
