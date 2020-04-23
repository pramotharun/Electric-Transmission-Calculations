import numpy as np

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


line_model = input("Line model: short, nominal, pi, long?")
resistance_line_km = 0
gamma = (capacitive_reactance*inductive_reactance)**0.5

# NOTE: check if the reactances are found for per meter or complete line. and check km to m

z = inductive_reactance + (resistance_line_km*1000)

if line_model == "short": # short excludes capacitive effect
    a = 1
    b = z = resistance_line_km + inductive_reactance
    c = 0
    D = 1
elif line_model == "pi": #medium transmission, pi model, t is not considered anywhere
    a = ( 1 + (capacitive_reactance*inductive_reactance)*0.5)
    b = z
    c = capacitive_reactance + ((capacitive_reactance**2)*z*0.25)
    d = a
elif line_model == "nominal": #medium transmission, pi model, t is not considered anywhere
    a = (1+capacitive_reactance*z*0.5)
    b = z + ((capacitive_reactance*(z**2)))*0.25
    c = capacitive_reactance
    d = a
elif line_model == "long":
    a = np.cosh(gamma*line_length_km*1000) # *1000 to change to meters
    b = inductive_reactance* np.sinh(gamma*line_length_km*1000)
    c = (1/inductive_reactance)*np.sinh(gamma*line_length_km*1000)
    d = a
else:
    print("error in input\n")

print(a,"\n",b,"\n",c,"\n",d,"\n")

