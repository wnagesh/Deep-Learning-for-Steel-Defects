#softmax

scores= =[3.0, 1.0, 0.2]

import numpy as np
def softmax(x):
    #compute Softmax values for x
    pass
    #TODO:compute and return softmax(x)

print (softmax(scores))

#plot Softmax Curves

import matplotlib.pyplot as plt
x= np.arrange(-2.0, 6.0, 0.1)
scores=np.vstack([x.np.ones_like(x),0.2*np.ones_like(x)])

plt.plot(x, softmax(scores).T,linewidth=2)
plt.show()
