# Pie chart example
import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [25, 30, 15, 30]
explode = (0.1, 0, 0, 0)  # explode the first slice

plt.pie(sizes, explode= explode, labels=labels, autopct='%1.1f%%', startangle=140, shadow = True)
plt.show()