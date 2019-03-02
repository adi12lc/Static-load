print("A plain carbon steel of grade 45c8(σyt) is subjected to tensile load F (in N)."
      " Calculate the diameter of rod using safety of factor FOS ")

F = float(input('F = '))
FOS = int(input('FOS = '))
σyt = float(input('σyt = ')) 
pi = 22/7
σ = (σyt/FOS)
unit = "N/mm2"
print('Working Stress = ',σ,unit)
d2 = ((F*4)/(pi*σ))
da = math.sqrt(d2)
d = (round(da))
print("diameter of rod = ",d,unit)

if 20.1<da<24.99:
    print("Size of shaft = 25mm")
elif 25.1<da<29.99:
    print("Size of shaft = 30mm")
elif 30.1<da<34.99:
    print("Size of shaft = 35mm")
elif 35.1<da<39.99:
    print("Size of shaft = 40mm")
elif 40.1<da<44.99:
    print("Size of shaft = 45mm")
elif 45.1<da<49.99:
    print("Size of shaft = 50mm")
elif 50.1<da<54.99:
    print("Size of shaft = 55mm")
elif 55.1<da<59.99:
    print("Size of shaft = 60mm")
elif 60.1<da<64.99:
    print("Size of shaft = 65mm")
elif 65.1<da<69.99:
    print("Size of shaft = 70mm")
elif 70.1<da<74.99:
    print("Size of shaft = 75mm")
elif 75.1<da<79.99:
    print("Size of shaft = 80mm")
elif 80.1<da<84.99:
    print("Size of shaft = 85mm")
elif 85.1<da<89.99:
    print("Size of shaft = 90mm")
elif 90.1<da<94.99:
    print("Size of shaft = 95mm")
elif 95.1<da<99.99:
    print("Size of shaft = 100mm")
