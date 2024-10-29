# Niech: A = 0.5/1 + 0.9/2 + 1/5, i B = 0.7/2 + 0.9/3 + 0.1/4.
# Oblicz A ∪ B i A ∩ B.
from collections import OrderedDict

A = {"1" : 0.5, "2" : 0.9, "5": 1}
B = {"2" : 0.7, "3" : 0.9, "4": 0.1}
AuB = OrderedDict()
for i in A:
    AuB[i] = A[i]
for i in B:
    if i in AuB:
        AuB[i] = max(AuB[i],B[i])
    else:
        AuB[i] = B[i]
sorted_AuB = OrderedDict(sorted(AuB.items()))
print("A ∪ B")
print(list(sorted_AuB.values()))
print(list(sorted_AuB))
print("A ∩ B")
AnB = OrderedDict()
ans = OrderedDict()
for i in A:
    AnB[i] = A[i]
for i in B:
    if i in AnB:
        ans[i] = min(AnB[i],B[i])
    else:
        AnB[i] = B[i]
sorted_AnB = OrderedDict(sorted(ans.items()))
print(list(sorted_AnB.values()))
print(list(sorted_AnB))
