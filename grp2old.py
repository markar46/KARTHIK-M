import matplotlib.pyplot as plt

# x-coordinate of left sides of bars
left = [1,2,3,4,5]

# heigts of bars 
height = [10,24,36,40,5]

#labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

#plotting a bar chart
plt.bar(left, height, tick_label = tick_label,width = 0.8, color = ['red', 'green'])

#naming the x-axix
plt.xlabel('x - axis')
#naming the y-axis
plt.ylabel('y - axis')
#plot title
plt.title('my bar chart!')

#function to show the plot
plt.show()