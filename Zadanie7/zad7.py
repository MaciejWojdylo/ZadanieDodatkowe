A = [6,7,8,9,10,11]
valuesA = [0.2,0.5,0.8,1,0.7,0.4]
heightA = []
supportA = []
coreA = []
cardA = []
heightA.append(max(valuesA))
print("heightA", heightA)
for i in range(len(A)):
    if(valuesA[i] > 0):
        supportA.append(A[i])
print("support",supportA)
for i in range(len(A)):
    if(valuesA[i] == 1):
        coreA.append(A[i])
print("core",coreA)
cardA = len(A)
print("card",cardA)