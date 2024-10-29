import matplotlib.pyplot as plt
bmi = []
for i in range(0, 40,1):
    bmi.append(i)
healthy = []
for x in bmi:
    if x < 18:
        healthy.append(0)
    else:
        if x >= 18 and x <= 20:
            healthy.append(round((x - 18) / 2,2))
        else:
            if (x > 20 and x < 25):
                healthy.append(1)
            else:
                if (x >=25 and x <= 27):
                    healthy.append(round((27-x)/2,3))
                else:
                    healthy.append(0)
print(healthy)
unhealthy = []
for i in healthy:
    unhealthy.append(1-i)
print(unhealthy)

plt.plot(bmi, healthy, label='Bmi zdrowy', color='blue', marker='o')
plt.title("BMI a Healthy")
plt.xlabel("Wartości bmi")
plt.ylabel("Wartości healthy(x)")
plt.legend()

plt.plot(bmi, unhealthy, label='Bmi nie zdrowy', color='red', marker='o')
plt.title("BMI a Healthy")
plt.xlabel("Wartości bmi")
plt.ylabel("Wartości healthy(x)")
plt.legend()
plt.show()