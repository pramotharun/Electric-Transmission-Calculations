import cmath
import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("MVAR")
plt.ylabel("MW")
plt.title("Sendine End Circle")

alpha = cmath.phase(a)
beta = cmath.phase(b)

#number of edges:
n = 60

#iterations
t = np.linspace(0,2*pi,n+1)


#Center of the sending end circle is located at the tip of phasor:
modulus = (abs(a)**2*(abs(sendingend_voltage))**2)/(abs(b)**2)

angle = beta - alpha

sendingend_centerx = np.sin(angle)*modulus
sendingend_centery = np.cos(angle)*modulus

radius_circle_sending = (abs(sendingend_voltage)*abs(nominal_system_voltage))/(abs(b))

print( "radius:", radius_circle_sending)
sendingend_x = radius_circle_sending * np.sin(t) + sendingend_centerx
sendingend_y = radius_circle_sending *np.cos(t) + sendingend_centery

#Display the circle:

plt.axis("equal")
plt.grid()
plt.plot(sendingend_x,sendingend_y)
plt.savefig("SendingEnd.png",bbox_inches="tight")

plt.close()

plt.xlabel("MVAR")
plt.ylabel("MW")
plt.title("Receivving End Circle")
alpha = cmath.phase(a)
beta = cmath.phase(b)

#number of edges:
n = 60

#iterations
t = np.linspace(0,2*pi,n+1)


#Center of the sending end circle is located at the tip of phasor:
modulus = (abs(a)**2*(abs(sendingend_voltage))**2)/(abs(b)**2)

angle = beta - alpha

#horizontal_cordinate_center_sendingend = (abs(d)*(sendingend_voltage**2)*np.cos(angle))/abs(b) #######

#vertical_cordinate_center_sendingend = (abs(d)*(sendingend_voltage**2)*np.sin(angle))/abs(b) #######


radius_circle_receiving = (abs(sendingend_voltage)*abs(nominal_system_voltage))/(abs(b))

receivingend_centerx = ((abs(a)**2)*(abs(nominal_system_voltage)**2) * (np.cos(angle)))/(abs(b))
receivingend_centery = ((abs(a)**2)*(abs(nominal_system_voltage)**2) * (np.sin(angle)))/(abs(b))

receivingend_x = radius_circle_receiving * np.sin(t) - receivingend_centerx
receivingend_y = radius_circle_receiving*np.cos(t) - receivingend_centery

plt.axis("equal")
plt.grid()
plt.plot(receivingend_x,receivingend_y)
plt.savefig("ReceivingEnd.png",bbox_inches="tight")

plt.close()
