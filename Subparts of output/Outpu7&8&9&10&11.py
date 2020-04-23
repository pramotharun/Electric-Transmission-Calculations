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

receivingend_load_MW = 0
pf_receiving_load = 0

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

transmission_efficiency = (receivingend_load_MW *100 )/ (receivingend_load_MW + powerloss_MW) #Output 11
