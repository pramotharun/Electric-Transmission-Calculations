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

electric_permittivity = 8.85 * (10**(-12))
capacitance = (2*3.14159*electric_permittivity)/(np.log(MGMD/SGMD))
print ( capacitance )