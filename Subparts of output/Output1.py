import numpy as np
#GLOBAL VARIABLES

# Radius of subconductors :
diameter_strand = 2
number_of_strands = 12
number_of_layers = 2
radius_subconductor = 0

# Output 1:
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

#Output 1 code


# Variables from Output 1

#SGMD, called later
distance_subconductors = int(input("input distance between subconductors?\n"))
m = number_of_strands**2
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
############################################################################################