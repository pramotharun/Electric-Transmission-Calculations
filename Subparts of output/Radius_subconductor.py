diameter_strand = 2
number_of_strands = 12
number_of_layers = 2
radius_subconductor = 0

layers_1 = ((3)+((9-(4*(3)*(1-number_of_strands)))**0.5))/6
layers_2 = ((3)-((9-(4*(3)*(1-number_of_strands)))**0.5))/6

if ((-1)*abs(layers_1) == layers_1):
    number_of_layers = layers_2
else:
    number_of_layers = layers_1

radius_subconductor = ((2*number_of_layers - 1) * diameter_strand)*0.5

print(radius_subconductor)