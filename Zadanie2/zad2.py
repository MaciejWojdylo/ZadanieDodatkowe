Car = [0.5, 0.4, 0.3, 0.9, 0.1]
Truck = [1, 0.1, 0.4, 0.4, 0.2]
ans1 = []
for i in range(0,len(Car)):
    ans1.append(max(Car[i],Truck[i]))
print("odp1:",ans1)
ans2 = []
for i in range(0,len(Car)):
    ans2.append(min(Car[i],Truck[i]))
print("odp2:",ans2)
ans3 = []
for i in range(0,len(Car)):
    ans3.append(round(1-Car[i],2))
print("odp3:",ans3)
ans4 = []
for i in range(0,len(Car)):
    ans4.append(min(Car[i],1-Truck[i]))
print("odp4:",ans4)
ans5 = []
for i in range(0,len(Car)):
    ans5.append(round(max(Car[i],1-Car[i]),2))
print("odp5:",ans5)
ans6 = []
for i in range(0,len(Car)):
    ans6.append(round(min(Car[i],1-Car[i]),2))
print("odp6:",ans6)

