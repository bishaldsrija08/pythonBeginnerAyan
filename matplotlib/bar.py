import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [1, 3, 2, 5, 4]

plt.bar(x, y, color='blue', alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Chart')
plt.show()