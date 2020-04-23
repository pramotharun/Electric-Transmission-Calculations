import numpy as np
import cmath
import matplotlib.pyplot as plt
import numpy as np

# Note: the code is split into blocks for different output parameters.

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

charging_current = (((3)**0.5)*nominal_system_voltage)/ ( capacitive_reactance/((-1)**0.5))
print("Charging Current:", abs(charging_current))

 
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


############################################################################################


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
############################################################################################

#Exporting as PDF:

from reportlab.pdfgen import canvas
from datetime import date
from datetime import datetime
import os


now = datetime.now()

dt_string = now.strftime("%b-%d-%Y_%H:%M:%S")
#print("date and time =", dt_string)	
filename = "Output:"+str(dt_string) ########
save_name = os.path.join('/home/pramoth/Desktop',filename) ########
pdf = canvas.Canvas(save_name)

pdf.setTitle("Result:")
#the answers have to be assigned to the correct variables


textLines = ["1. Inductance per phase per km in mH/km:" , "      " + str(inductance*1000),# in mh
"2. Capacitance per phase per km in nF/km:"   , "      " + str(capacitance*(10**9)), # in nF
"3. Inductive reactance of the line in Ohm:  "   , "      " +str(inductive_reactance),
"4. Capacitive reactance of the line in Ohm:  "   , "      " +str(capacitive_reactance),
"5. Charging current drawn from the sending end substation: " , "      " + str(charging_current),
"6. ABCD parameters of the line:   "   , "      " + " A :" +str(a),
"      " + " B :" +str(b), "      " + " C :" +str(c),"      " + " D :" +str(d),
"7. Sending end voltage in kV:   "   , "      " + str(sendingend_voltage/1000), #in kV
"8. Sending end current in A:   "   , "      " + str(sendingend_current),
"9. Percentage voltage regulation:  "   ,  "      " +str(voltage_regulation),
"10. Power loss in the line in MW:  "   , "      " + str(powerloss_MW),
"11. Transmission efficiency:  "  ,  "      " +str(transmission_efficiency),
"Sending and receiving end circles has been saved in the folder",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" Export Details:  " + str(dt_string)]
 #Title:
pdf.drawCentredString(300,770,"Results")
pdf.setFont("Courier",12)
pdf.drawCentredString(290,720,"Report generated using github pramotharun repository")
pdf.line(30, 710, 550, 710)
text = pdf.beginText(40, 680)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)
pdf.save()

############################################################################################