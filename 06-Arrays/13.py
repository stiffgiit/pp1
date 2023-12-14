import numpy as np
import matplotlib.pyplot as plt

employees = [25, 19, 32, 7]

transport = ['car', 'public transport', 'bike', 'on foot']

plt.bar(transport, employees)
plt.title('People and their way of commute to work')
plt.show()