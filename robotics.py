from math import sin,cos,exp,sqrt,pi
from numpy import array,dot

wheel_angular_velocities=array([6*pi,2*pi,3*pi])
wheel_angular_velocities_bar=array([0.0,0.0,0.0])


def limit(wheel_angular_velocities):
    j=0
    while j<3:
        for i in wheel_angular_velocities:
            if i<-5*pi:
                wheel_angular_velocities_bar[j]=-5*pi
                j=j+1
            if -5*pi <= i <= 5*pi:
                wheel_angular_velocities_bar[j]=i
                j=j+1
            elif i>5*pi:
                wheel_angular_velocities_bar[j]=5*pi
                j=j+1
    return wheel_angular_velocities_bar

x=limit(wheel_angular_velocities)
print(x)



