import random

text = "P2 \n100 100\n14\n"

h = 100
w = 100

for height in range(0, h):
    for width in range(0, w):
        text += str(random.randint(0, 15)) + " "
    text += "\n"
    
with open("teste.pgm", "w") as file:
    file.write(text)
        
print(text)