from matplotlib import pyplot as plt

hight = [130,150,170,190,210]
small = [1,1,0.5,0,0]
medium = [0,0,1,0,0]
tall = [0,0,0.5,1,1]
#a Small ∩ Tall
a_ans = []
for i in range(len(small)):
    a_ans.append(min(small[i],tall[i]))
plt.plot(hight, a_ans, label='Small ∩ Tall', color='blue', marker='o')
plt.xlabel("Wysokosc")
plt.ylabel("Wartość")
plt.legend()
plt1 = plt
#b Small ∪ Medium
b_ans = []
for i in range(len(small)):
    b_ans.append(max(small[i],medium[i]))
plt.plot(hight, b_ans, label='Small ∪ Tall', color='red', marker='o')
plt.xlabel("Wysokosc")
plt.ylabel("Wartość")
plt.legend()
# plt.plot(hight, small, label='Small', color='orange', marker='o')
# plt.xlabel("Wysokosc")
# plt.ylabel("Wartość")
# plt.legend()
# plt.plot(hight, medium, label='Medium', color='purple', marker='o')
# plt.xlabel("Wysokosc")
# plt.ylabel("Wartość")
# plt.legend()
# plt.plot(hight, tall, label='Tall', color='green', marker='o')
# plt.xlabel("Wysokosc")
# plt.ylabel("Wartość")
# plt.legend()
plt.show()