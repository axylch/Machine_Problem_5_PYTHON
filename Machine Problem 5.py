#Machine Problem 5 (Piecewise Function 2)
import numpy as np
import matplotlib.pylab as plot
#Creating Numeric Sequence
n = np.linspace(0,199,200)    
#Defining the Function
#Input np.sin(((3*n*np.pi)/100))
def Piecewise(n): 
      
    evaluate=eval(functionx)  
    return evaluate 
#Input the Sin Function
functionx = (input("Input your function, Piecewise(n):")) 
#Looping the Function
for i in range(0,200):
    
    if i==0: #First Function
        y=(-1.5*Piecewise(n))+(2*Piecewise(n+1))-(0.5*Piecewise(n+2))
        
    elif i==199: #Third Function
        y=(1.5*Piecewise(n))-(2*Piecewise(n-1))+(0.5*Piecewise(n-2))
        
    else: #Second Function
        y= (0.5*Piecewise(n+1))-(0.5*Piecewise(n-1))

plot.plot(Piecewise(n), 'b-', label = 'Function X Values' )
plot.title('Graph of the Functions X and Y')
plot.legend()
plot.plot(y, 'y-', label = 'Y Values')
plot.legend()
plot.grid()
plot.show()