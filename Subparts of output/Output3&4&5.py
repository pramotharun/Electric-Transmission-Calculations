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
power_freequency = 50 #HZ
line_length_km = 0 
#Output 3
inductive_reactance  = 2*pi*power_freequency*inductance * line_length_km * 1000 #km to m

#Output 4
capacitive_reactance = (2*pi*power_freequency*capacitance)**(-1)

#Output 5
nominal_system_voltage = 0
charging_current = nominal_system_voltage / capacitive_reactance