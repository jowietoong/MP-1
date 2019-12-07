from matplotlib import pyplot as plt
def fct (n):

    if n <= 9:
        return (n**2) - 7 
    else:
        return fct(n-10)

x = []
y = []

for i in range(0,100):
    x.append(i)
    y.append(fct(i))
    
plt.stem(x, y, use_line_collection=True)
plt.title('Graph of Function')
plt.xlabel('X Axis') 
plt.ylabel('Y Axis')
plt.show()
