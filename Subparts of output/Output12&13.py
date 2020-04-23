#GLOBAL VARIABLES

# Radius of subconductors :
diameter_strand = 2
number_of_strands = 12
number_of_layers = 2
radius_subconductor = 0

############################################################################################

### OUTPUT 1:

distance_subconductors = 0
SGMD  = 0
distance_subconductors = 0
m = number_of_strands**2
resultant_radius = 0.7788 * radius_subconductor
number_subconductors = 0
symmetric_input = 0
MGMD = 0
inductance = 0

#Distance between the phase conductors:
distancex = 0
distancey = 0
distancez = 0

distances = 0

############################################################################################

#OUTPUT 2:

electric_permittivity = 0
capacitance = 0
pi = 3.14159

############################################################################################

#OUTPUT 3,4 & 5:

power_freequency = 50 #HZ
line_length_km = 0 
inductive_reactance  = 0

#Output 4
capacitive_reactance = 0

#Output 5
nominal_system_voltage = 0
charging_current = 0

############################################################################################

#OUTPUT 6:
line_model = 0
resistance_line_km = 0
gamma = 0
a = 0
b = 0
c = 0
d = 0
z = 0

############################################################################################


#OUTPUT 7 TO 11:

receivingend_load_MW = 0
pf_receiving_load = 0

receivingend_current = 0
sendingend_voltage = 0 #Output 7
sendingend_current = 0 #Output 8

voltage_regulation = 0 #Output 9
powerloss =0 # output 10
powerloss_MW = 0

transmission_efficiency = 0 #Output 11


############################################################################################
import cmath
import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sendine End Circle")
alpha = cmath.phase(a)
beta = cmath.phase(b)

#number of edges:
n = 60

#iterations
t = np.linspace(0,2*pi,n+1)


#Center of the sending end circle is located at the tip of phasor:
#modulus = (abs(a)**2*(abs(sendingend_voltage))**2)/(abs(b)**2)
modulus = 1
angle = 45
#angle = beta - alpha
sendingend_centerx = np.sin(angle)*modulus
sendingend_centery = np.cos(angle)*modulus

#radius_circle_sending = (abs(sendingend_voltage)*abs(nominal_system_voltage))/(abs(b))
radius_circle_sending = 1
sendingend_x = radius_circle_sending * np.sin(t) +sendingend_centerx
sendingend_y = radius_circle_sending *np.cos(t) +sendingend_centery

#Display the circle:

plt.axis("equal")
plt.grid()
plt.plot(sendingend_x,sendingend_y)
plt.savefig("SendingEnd.png",bbox_inches="tight")

plt.show()

#radius_circle_receiving = (abs(sendingend_voltage)*abs(nominal_system_voltage))/(abs(b))
receivingend_centerx = ((abs(a)**2)*(abs(nominal_system_voltage)**2) * (np.cos(angle)))/(abs(b))
receivingend_centery = ((abs(a)**2)*(abs(nominal_system_voltage)**2) * (np.sin(angle)))/(abs(b))

receivingend_x = radius_circle_sending * np.sin(t) - receivingend_centerx
receivingend_y = radius_circle_sending *np.cos(t) - receivingend_centery

plt.axis("equal")
plt.grid()
plt.plot(receivingend_x,receivingend_y)
plt.savefig("ReceivingEnd.png",bbox_inches="tight")

plt.show()