import numpy as np


#Radius of subconductor code:


# Variables from Radius of subconductors :
diameter_strand = int(input("diameter of strand?\n"))
number_of_strands = int(input("Input number of strands?\n"))
#number_of_layers = 2
#radius_subconductor = 0

layers_1 = ((3)+((9-(4*(3)*(1-number_of_strands)))**0.5))/6
layers_2 = ((3)-((9-(4*(3)*(1-number_of_strands)))**0.5))/6

if ((-1)*abs(layers_1) == layers_1):
    number_of_layers = layers_2
else:
    number_of_layers = layers_1

radius_subconductor = ((2*number_of_layers - 1) * diameter_strand)*0.5

##############################################################################

#Output 1 code


# Variables from Output 1

#SGMD, called later
distance_subconductors = int(input("input distance between subconductors?\n"))
#m = number_of_strands**2
resultant_radius = 0.7788 * radius_subconductor
number_subconductors = int(input("number of subconductors?\n"))

#Distance between the phase conductors:
symmetric_input = input("Is it symmentric? type 'yes' or 'no'.\n")
#MGMD, called later in if statement
#inductance, called in the end


if symmetric_input == "yes": 
    distances = int(input("What is the distance between phase conductors?\n"))
    MGMD = distances

else:
    distancex = int(input("Distance - x??\n"))
    distancey = int(input("Distance - y??\n"))
    distancez = int(input("Distance - z??\n"))
    MGMD = (distancex*distancey*distancez)**(1/3)

#SGMD calculation:
if number_subconductors == 2:
    # 2 subconductors:
    SGMD =  ( (resultant_radius**2) * (distance_subconductors**2) )**4
    print("2 is activated")
elif number_subconductors == 3:
    # 3 subconductors:
    SGMD = ( (resultant_radius**3) * (distance_subconductors**6) )**9
    print("3 is activated")
elif number_subconductors == 4:
    # 4 subconductors:
    SGMD = ( (resultant_radius**4) * (distance_subconductors**12) * ( (2**0.5)**4 ) )**16
    print("4 is activated")
elif number_subconductors == 6:
    # 6 subconductors:
    SGMD = ( ( resultant_radius * (3*2) * (distance_subconductors**5) ) ** 32)
    print("6 is activated")
else:
    print("please choose between 2,3,4 and 6\n\n")


inductance = 2*(10**(-7)) * np.log(MGMD/SGMD)
print("Inductance per phase conductor:\n")
print(inductance)
#########################################################################

#OUTPUT 2
pi = 3.14159
electric_permittivity = 8.85 * (10**(-12))
capacitance = (2*3.14159*electric_permittivity)/(np.log(MGMD/SGMD))
print ( capacitance )

#########################################################################

power_freequency = int(input("what is the power freequency?\n")) #HZ
line_length_km = int(input("what is the line length in km?\n"))
#Output 3
inductive_reactance  = 2*pi*power_freequency*inductance * line_length_km * 1000 #km to m

#Output 4
capacitive_reactance = (2*pi*power_freequency*capacitance)**(-1)

#Output 5
nominal_system_voltage = int(input("What is nominal system voltage?\n"))
charging_current = nominal_system_voltage / capacitive_reactance

#########################################################################

#Output 6

line_model = input("Line model: short, nominal pi, long?\n")
resistance_line_km = int(input("what is the resistance of line per km?\n"))
gamma = (capacitive_reactance*inductive_reactance)**0.5

# NOTE: check if the reactances are found for per meter or complete line. and check km to m
z = resistance_line_km + inductive_reactance
if line_model == "short": # short excludes capacitive effect
    a = 1
    b = z
    c = 0
    d = a
elif line_model == "nominal pi": #medium transmission, pi model, t is not considered anywhere
    a = ( 1 + (capacitive_reactance*inductive_reactance)*0.5)
    b = z + ( (capacitive_reactance*(z**2)*0.5))
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

#########################################################################

#Output 7 to 11:

receivingend_load_MW = int(input("what is the receiving end load in MW?\n"))
pf_receiving_load = float(input("what is the powerfactor of the receiving load?\n"))

receivingend_current = (receivingend_load_MW * (10**6))/(nominal_system_voltage*pf_receiving_load)
sendingend_voltage = (a*nominal_system_voltage) + (b* receivingend_current)
sendingend_current = (c*nominal_system_voltage) + (d*receivingend_current)
#outputs are in volts
print("sending end voltage = ", sendingend_voltage/1000,"\n") # Output 7
print("sending end current = ", sendingend_current/1000,"\n") # Output 8

voltage_regulation = ((sendingend_voltage-nominal_system_voltage)*100)/sendingend_voltage #Output 9
powerloss = 3*(sendingend_current**2)*resistance_line_km*1000*line_length_km # output 10
#check if you have multiplied line length in places involving distance and R per km.
powerloss_MW = powerloss / (10**6)
print("powerloss:\n",powerloss_MW,"\n")

transmission_efficiency = (receivingend_load_MW *100 )/ (receivingend_load_MW + powerloss_MW) #Output 11
print("transmission efficiency:\n",transmission_efficiency,"\n")

#########################################################################
#Last updated: 20:19 13/04