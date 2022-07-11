import numpy as np
import math

a,b,d = map(int,input().split())
 
y = np.array([a, b])
rad = np.radians(d)
cos = np.cos(rad)
sin = np.sin(rad)
 
rot_x = (y[0] * cos) - (y[1] * sin)
rot_y = (y[0] * sin) + (y[1] * cos)

print(rot_x,rot_y)