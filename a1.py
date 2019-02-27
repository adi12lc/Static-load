print("A plain carbon steel of grade 45c8(σyt) is subjected to tensile load F (in N)."
      " Calculate the diameter of rod using safety of factor FOS ")

import math

F = float(input('F = '))
FOS = int(input('FOS = '))
σyt = int(input('σyt = '))
pi = 22/7
σ = (σyt/FOS)
print('Working Stress = ',σ)
d2 = ((F*4)/(pi*σ))
da = math.sqrt(d2)
d = (round(da))
print("diameter of rod = ",d)
