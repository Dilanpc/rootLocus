import matplotlib.pyplot as plt


def sigma(resistance, capacitance):
    return 1/(2*resistance * capacitance)

def omega(inductance, capacitance):
    return 1/(inductance * capacitance)**0.5

def polos(sigma, omega):
    s1 = -sigma + (sigma**2 - omega**2)**0.5
    s2 = -sigma - (sigma**2 - omega**2)**0.5
    return s1, s2 
    

capacitance = 1e-2
inductance = 1

x_axis = []
y_axis = []
values = []

for resistance in [0.5*x for x in range(1, 100)]:
    roots = polos(sigma(resistance, capacitance), omega(inductance, capacitance))
    values.append([resistance, roots[0], roots[1]])
    x_axis.append(roots[0].real)
    y_axis.append(roots[0].imag)
    x_axis.append(roots[1].real)
    y_axis.append(roots[1].imag)


plt.plot(x_axis, y_axis, 'o')
plt.xlabel('Real')
plt.ylabel('Imag')
plt.title('Root Locus Plot')
plt.grid(True)

for value in values:
    print(value)

plt.show()
