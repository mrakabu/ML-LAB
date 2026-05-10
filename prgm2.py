
import matplotlib.pyplot as plt

x = [24, 56, 86, 53]
labels = ['A', 'B', 'C', 'D']

plt.bar(labels, x, color='skyblue')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Graph")
plt.tight_layout()
plt.show()
