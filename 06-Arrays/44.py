import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
    x.append(n)

# create y values
for n in x:
    y.append(n**2 - 3)
    
plt.plot(x, y, linewidth=2)
    
plt.show()
