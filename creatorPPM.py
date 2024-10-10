import random

size = 100

text = "P3 \n" + str(size) + " " + str(size) + "\n15\n"


for height in range(0, size):
    for width in range(0, size):
        text += str(random.randint(0, 15)) + " "
        text += str(random.randint(0, 15)) + " "
        text += str(random.randint(0, 15)) + " "
    text += "\n"
    
with open("teste.ppm", "w") as file:
    file.write(text)
        
print(text)