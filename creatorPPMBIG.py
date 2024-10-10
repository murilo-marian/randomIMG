import random
#teste

size = 1000

text = "P3 \n" + str(size) + " " + str(size) + "\n255\n"

file = open("testeBIG.ppm", "a")
for height in range(0, size):
    for width in range(0, size):
        text += str(random.randint(0, 255)) + " "
        text += str(random.randint(0, 255)) + " "
        text += str(random.randint(0, 255)) + " "
    text += "\n"
    file.write(text)
    text = ""
    

        
print(text)