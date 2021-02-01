
# coding: utf-8

# In[12]:


from pynq.overlays.base import BaseOverlay

from pynq.lib import Pmod_PWM
base = BaseOverlay("base.bit") #Program the ZYNQ PL
#PMOD output and output pin:2
pwm= Pmod_PWM(base.PMODA,2)
input_v= Pmod_PWM(base.PMODB,2)
#PWM 
import time
import struct
import numpy as np
import matplotlib.pyplot as plt

T = 10  #period
resolution = 0.001  #how many point in T
start = 1  #the fist value of the wave
end = 20  #the end value of the wave
xout=[]
yout=[]
samples = []

for i in range(start,end,T):
    x = np.arange(i, i + T,  resolution)
    # y = np.where(x<start+0.5, x-start, 0)
    y = np.where(x >= i+ T/2, 1,0)
    yout.append(y)
    xout.append(x)
    
num = int((T/resolution)*((end-start+1)/T))
print(num)
yout1 = np.reshape(yout,(num,1))
xout1 = np.reshape(xout,(num,1))
for j in range(0,num,1):
    #set period in ms and duty cycle
    pwm.generate(T,50)
    #pwm.write()
    #pwm.append(yout1[j])
    #sample = input_v.read()
    #samples.append(sample[0])
    
    
print('xout:',xout1)
# print('samples:',samples)
#plt.plot(xout1,samples)
plt.show()    


#stop PWM
pwm.stop()





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




