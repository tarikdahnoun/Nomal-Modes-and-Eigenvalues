import numpy as np
import pylab as py

k=15 #N/m
m=.3 #kg

A=np.matrix([[2*k,-k],[-k,k]])

eval,evec=np.linalg.eig(A)
print "The Eigenvalue is",eval
print
print "The Eigen Vector is"
print evec
print

omega1=np.sqrt(eval[0]/m)
omega2=np.sqrt(eval[1]/m)

tmin=0
tmax=10
nts=10000
t=np.linspace(tmin,tmax,nts)
n1=evec[0,0]*np.cos(omega1*t[tmax])
n2=evec[1,0]*np.cos(omega1*t[tmax])
n3=evec[0,1]*np.cos(omega2*t[tmax])
n4=evec[1,1]*np.cos(omega2*t[tmax])

print "The first component of the first normal mode is",n1
print "The second component of the first normal mode is",n2
print "The first component of the second normal mode is",n3
print "The second component of the second normal mode is",n4

#The interpretation of the first and second mode might best be described as where the masses are either moving in directly opposite directions or the exact same direction.
#These are special because we can understand them directly, all other possibilities will be some combination of the two normal modes.
py.figure(1)
N1=evec[0,0]*np.cos(omega1*t)
N2=evec[1,0]*np.cos(omega1*t)
py.plot(t,N1,'.-',label=r"component 1")
py.plot(t,N2,'.-',label=r"component 2")
py.title("First Normal Mode")

py.figure(2)
N3=evec[0,1]*np.cos(omega2*t)
N4=evec[1,1]*np.cos(omega2*t)
py.plot(t,N3,'.-',label=r"component 1")
py.plot(t,N4,'.-',label=r"component 2")
py.title("Second Normal Mode")



py.xlabel("Time [s]",fontsize=16)
py.ylabel("Position [m]",fontsize=16)

py.show()

py.legend(loc='top',fontsize=11)