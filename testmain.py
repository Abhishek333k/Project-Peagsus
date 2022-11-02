from PIL import Image
print(f''' Media Files :

1.Rose 
2.Water
3.Sky
''')

Envi = input("Select Environment")

if Envi == "1":
	print ("Roses are red")
img = Image.open(r"C:\Users\MARS\Desktop\TEMP IMP\27oct\rose.jfif") 
img.show()


elif Envi == "2":
	print("water fall from sky")
img = Image.open(r"C:\Users\MARS\Desktop\TEMP IMP\27oct\water.jpg") 
img.show()

elif Envi == "3":
	print("water fall from sky")
img = Image.open(r"C:\Users\MARS\Desktop\TEMP IMP\27oct\sky.jpg") 
img.show()


else:
	print("Please choose correct Option")
