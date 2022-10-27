set1 = {"j", "a" , "y"}
set2 = {1, 3, 5}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

x = {"badminton", "hockey", "football"}
y = {"google", "microsoft", "badminton"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
