import matplotlib.pyplot as plt

print(plt.matplotlib.__version__)

x= [1,2,3,4,5]
y = [1,3,2,5,4]

plt.plot(x,y, "o:r")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()