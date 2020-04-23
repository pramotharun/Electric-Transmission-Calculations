from reportlab.pdfgen import canvas
from datetime import date
from datetime import datetime
import os

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%b-%d-%Y_%H:%M:%S")
print("date and time =", dt_string)	

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
filename = "Output:"+str(d4) ########

save_name = os.path.join('/home/pramoth/Desktop',filename) ########

pdf = canvas.Canvas(save_name)

pdf.setTitle("Assignment3_Output")
#the answers have to be assigned to the correct variables

answer1 = 1
answer2 = 2
answer3 = 3
answer4 = 4
answer5 = 5
answer6 = 6
answer7 = 7
answer8 = 8
answer9 = 9
answer10 = 10
answer11 = 11
answer12 = 12
answer13 = 13

textLines = ["1. Inductance per phase per km in H/km:" , "      " + str(answer1),
"2. Capacitance per phase per km in F/km:"   , "      " + str(answer2),
"3. Inductive reactance of the line in Ohm:  "   , "      " +str(answer3),
"4. Capacitive reactance of the line in Ohm:  "   , "      " +str(answer4),
"5. Charging current drawn from the sending end substation: " , "      " + str(answer5),
"6. Calculate ABCD parameters of the line:   "   , "      " + " A :" +str(answer6),
"      " + " B :" +str(answer6), "      " + " C :" +str(answer6),"      " + " D :" +str(answer6),
"7. Calculate the sending end voltage in kV:   "   , "      " + str(answer7),
"8. Calculate the sending end current in A:   "   , "      " + str(answer8),
"9. Calculate the percentage voltage regulation:  "   ,  "      " +str(answer9),
"10. Calculate the power loss in the line in MW:  "   , "      " + str(answer10),
"11. Calculate the transmission efficiency:  "  ,  "      " +str(answer11),
"12. Draw the sending end circle diagram:  "  ,  "      " +str(answer12),
"13. Draw the receiving end circle diagram:  "  , "      " + str(answer13)]




pdf.drawCentredString(300,770,"Assignment 3 Output")
pdf.setFont("Courier",12)
pdf.drawCentredString(290,720,"Darshan (1071180), Shubham (1071180) & Pramoth (107118074)")
pdf.line(30, 710, 550, 710)

text = pdf.beginText(40, 680)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)

pdf.save()
