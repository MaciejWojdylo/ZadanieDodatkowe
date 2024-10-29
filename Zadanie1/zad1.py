from math import ceil

temp = [20,35,40,50,60,70,80,90,100]
u_hot = []
for i in temp:
    if(i <= 20):
      u_hot.append(0)
    else:
        if i > 20 and i < 100:
            value = round((i-20)/80,3)
            u_hot.append(value)
        else:
            u_hot.append(1)
print(temp)
print(u_hot)