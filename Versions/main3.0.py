import numpy as np


#Radius of subconductor code:


# Variables from Radius of subconductors :
diameter_strand = float(input("diameter of strand?\n"))
number_of_strands = float(input("Input number of strands?\n"))
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
distance_subconductors = float(input("input distance between subconductors?\n")) #Q1
#m = number_of_strands**2
resultant_radius = 0.7788 * radius_subconductor
number_subconductors = float(input("number of subconductors?\n"))

#Distance between the phase conductors:
symmetric_input = input("Is it symmentric? type 'yes' or 'no'.\n")
#MGMD, called later in if statement
#inductance, called in the end


if symmetric_input == "yes": 
    distances = float(input("What is the distance between phase conductors?\n"))
    MGMD = distances

else:
    distancex = float(input("Distance - x??\n"))
    distancey = float(input("Distance - y??\n"))
    distancez = float(input("Distance - z??\n"))
    MGMD = (distancex*distancey*distancez)**(1/3)

#SGMD calculation:
if number_subconductors == 2:
    # 2 subconductors:
    SGMD =  ( (resultant_radius**2) * (distance_subconductors**2) )**(1/4)
elif number_subconductors == 3:
    # 3 subconductors:
    SGMD = ( (resultant_radius**3) * (distance_subconductors**6) )**(1/9)
elif number_subconductors == 4:
    # 4 subconductors:
    SGMD = ( (resultant_radius**4) * (distance_subconductors**12) * ( (2**0.5)**4 ) )**(1/16)
elif number_subconductors == 6:
    # 6 subconductors:
    SGMD = ( ( resultant_radius * (3*2) * (distance_subconductors**5) ) ** (1/6))
else:
    print("please choose between 2,3,4 and 6\n\n")


inductance = 2*(10**(-7)) * np.log(MGMD/SGMD) * 1000 # per km
print("Inductance per phase conductor:\n")
print("inductance",inductance)
#########################################################################

#OUTPUT 2
pi = 3.14159
electric_permittivity = 8.85 * (10**(-12))
capacitance = (2*pi*electric_permittivity)/(np.log(MGMD/SGMD)) * 1000 # per km
print ("capacitance:", capacitance )

#########################################################################

power_freequency = float(input("what is the power freequency?\n")) #HZ
line_length_km = float(input("what is the line length in km?\n"))
#Output 3
inductive_reactance  = ((-1)**0.5)* 2*pi*power_freequency*inductance * line_length_km
print("inductive reactance:",inductive_reactance)

#Output 4
capacitive_reactance =((-1) * ((-1)**0.5))/((2*pi*power_freequency*capacitance * line_length_km ))
print("Capacitive reactance", capacitive_reactance)

#Output 5
nominal_system_voltage = float(input("What is nominal system voltage?\n"))

#charging_current = (nominal_system_voltage)/ ( capacitive_reactance/((-1)**0.5))
#print("Charging Current:", abs(charging_current))

 
#########################################################################

#Output 6

line_model = input("Line model: short, nominal, pi, long?\n")
resistance_line_km = float(input("what is the resistance per kilometer\n"))
z = (inductive_reactance + (resistance_line_km*line_length_km))

gamma = (capacitive_reactance*z)**0.5

# NOTE: check if the reactances are found for per meter or complete line. and check km to m


if line_model == "short": # short excludes capacitive effect
    
    a = 1
    b = z
    c = 0
    d = 1
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
    b = inductive_reactance* np.sinh(gamma)#*line_length_km)
    c = (1/inductive_reactance)*np.sinh(gamma)#*line_length_km)
    d = a
else:
    print("error in input\n")

print("a = ",a,"\n","b = ",b,"\n","c = ",c,"\n","d = ",d,"\n")

charging_current = ((-1)**0.5)*nominal_system_voltage / capacitive_reactance

#########################################################################

#Output 7 to 11:

receivingend_load_MW = float(input("what is the receiving end load in MW?\n"))
pf_receiving_load = float(input("what is the powerfactor of the receiving load?\n"))

receivingend_current = (receivingend_load_MW * (10**6))/((3**0.5)*nominal_system_voltage*pf_receiving_load)
sendingend_voltage = (a*nominal_system_voltage) + (b* receivingend_current)
sendingend_current = (c*nominal_system_voltage) + (d*receivingend_current)
#outputs are in volts
print("sending end voltage kv = ", abs(sendingend_voltage)/1000,"\n") # Output 7
print("sending end current Amps= ", abs(sendingend_current),"\n") # Output 8

voltage_regulation = ((sendingend_voltage-nominal_system_voltage)*100)/sendingend_voltage #Output 9
powerloss = 3*(sendingend_current**2)*resistance_line_km*line_length_km # output 10
#check if you have multiplied line length in places involving distance and R per km.
powerloss_MW = powerloss / (10**6)
print("powerloss in MW:\n",powerloss_MW,"\n")

transmission_efficiency = (receivingend_load_MW *100 )/ (receivingend_load_MW + powerloss_MW) #Output 11
print("transmission efficiency:\n",transmission_efficiency,"\n")

#########################################################################
# Last Updated 19:43 14/04

#Notes:
# 1) All outputs are in km
# 2) Verify gamma values
# 3) Both the reactances have been calculated for the complete line length

#To- Do:
# 1) Complete charging current output
# 2) 12/13 Output
# 3) Complete integration
# 4) Final Testing


from reportlab.pdfgen import canvas


pdf = canvas.Canvas("Output_dd_mm")

pdf.setTitle("Assignment3_Output")
#the answers have to be assigned to the correct variables

answer1 = inductance
answer2 = capacitance
answer3 = inductive_reactance
answer4 = capacitive_reactance
answer5 = charging_current

answer7 = sendingend_voltage
answer8 = sendingend_current
answer9 = voltage_regulation
answer10 = powerloss_MW
answer11 = transmission_efficiency
answer12 = 12
answer13 = 13

textLines = ["1. Inductance per phase per km in H/km:" + " "*3 + str(answer1),
"2. Capacitance per phase per km in F/km:" + " "*3 + str(answer2),
"3. Inductive reactance of the line in Ohm:" + " "*3 + str(answer3),
"4. Capacitive reactance of the line in Ohm:" + " "*3 + str(answer4),
"5. Charging current drawn from the sending end substation:" + " "*2 + str(answer5),
"6. Calculate ABCD parameters of the line:" + " "*3 + str(a)+ str(b)+ str(c)+ str(d),
"7. Calculate the sending end voltage in kV:" + " "*3 + str(answer7),
"8. Calculate the sending end current in A:" + " "*3 + str(answer8),
"9. Calculate the percentage voltage regulation:" + " "*3 + str(answer9),
"10. Calculate the power loss in the line in MW:" + " "*3 + str(answer10),
"11. Calculate the transmission efficiency:"+ " "*3 + str(answer11),
"The graph for 12 & 13 has been saved as image"
]
#Title:
pdf.drawCentredString(300,770,"Assignment 3 Output")
pdf.setFont("Courier",12)
pdf.drawCentredString(290,720,"Darshan (107118090), Shubham (107118094) & Pramoth (107118074)")
pdf.line(30, 710, 550, 710)

text = pdf.beginText(40, 680)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)

pdf.save()
